from collections import Counter
from dataclasses import replace

import pytest

from app.assignment import assign_greedy, assign_hungarian
from app.evaluation import evaluate
from app.scoring import Params, Recommender, to_unit
from app.seed import build_world


@pytest.fixture(scope='module')
def rec():
    return Recommender(build_world().dataset)


@pytest.mark.parametrize(('student', 'placement', 'rule'), [
    ('E001', 'P01', 'R4'), ('E001', 'P23', 'R2'), ('E001', 'P28', 'R3'),
    ('E003', 'P05', 'R6'), ('E004', 'P22', 'R7'), ('E002', 'P10', 'R5'),
])
def test_exclusion_visible(rec, student, placement, rule):
    result = rec.recommend(rec.ds.student(student), Params(top_n=50))
    assert placement not in {item.placement.id for item in result.ranking}
    exclusion = next(item for item in result.excluded if item.placement.id == placement)
    assert rule in {violation.rule_id for violation in exclusion.violations}


def test_health_requirement_changes_eligibility(rec):
    student = replace(rec.ds.student('E003'), vaccinated=True)
    ranking = rec.recommend(student, Params(top_n=50)).ranking
    assert 'P05' in {item.placement.id for item in ranking}


def test_logistics_can_reorder_results(rec):
    student = rec.ds.student('E001')
    params = Params(weights={'logistica': 1}, top_n=50)
    ranking = rec.recommend(student, params).ranking
    assert [item.placement.id for item in ranking] != [item.placement.id for item in rec.recommend(student, Params(top_n=50)).ranking]
    assert ranking[0].org.municipality == student.municipality
    assert ranking[0].placement.modality == student.modality_pref


def test_new_placement_uses_prior(rec):
    ranking = rec.recommend(rec.ds.student('E001'), Params(top_n=50)).ranking
    item = next(item for item in ranking if item.placement.id == 'P24')
    assert item.cold_start
    assert item.factors['calidad'].value == pytest.approx(to_unit(rec.global_rating))
    assert item.factors['similares'].value == pytest.approx(to_unit(rec.global_performance))


def test_weights_are_normalized_and_explain_score(rec):
    result = rec.recommend(rec.ds.student('E001'), Params(weights={'area': 3, 'competencias': 2}))
    first = result.ranking[0]
    assert first.score == pytest.approx(0.6 * first.factors['area'].value + 0.4 * first.factors['competencias'].value)
    assert first.score == pytest.approx(sum(f.contribution for f in first.factors.values()))


def test_cohort_respects_capacity_and_eligibility(rec):
    params = Params()
    result = assign_hungarian(rec, rec.ds.students, params)
    greedy = assign_greedy(rec, rec.ds.students, params)
    counts = Counter(a.placement_id for a in result.assignments)
    assert all(count <= rec.ds.placement(pid).available for pid, count in counts.items())
    assert len({a.student_id for a in result.assignments}) == len(result.assignments)
    assert all(not rec.exclusions(rec.ds.student(a.student_id), rec.ds.placement(a.placement_id), params) for a in result.assignments)
    assert (len(result.assignments), result.total_score) >= (len(greedy.assignments), greedy.total_score)


def test_simulation_reports_quality_and_catalog_concentration():
    result = evaluate(n_test=30)
    metrics = result['metodos']
    assert metrics['hibrido']['ndcg_at_5'] > metrics['popularidad']['ndcg_at_5']
    assert metrics['hibrido']['precision_at_5'] > metrics['aleatorio']['precision_at_5']
    bias = result['sesgo_popularidad']
    assert bias['hibrido']['concentracion_top20'] < bias['popularidad']['concentracion_top20']


def test_no_eligible_placement(rec):
    result = rec.recommend(rec.ds.student('E005'))
    assert not result.ranking and result.message.startswith('No hay plazas elegibles')


def test_repeatable_ranking(rec):
    student = rec.ds.student('E001')
    rebuilt = Recommender(build_world().dataset)
    assert rebuilt.recommend(student) == rec.recommend(student)
