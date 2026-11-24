const get = id => document.getElementById(id);
const text = (tag, value) => {
  const node = document.createElement(tag);
  node.textContent = value;
  return node;
};
const number = n => Number(n).toFixed(3);
const row = values => {
  const tr = document.createElement('tr');
  tr.append(...values.map(value => text('td', value)));
  return tr;
};
async function api(path, payload) {
  const response = await fetch(`/api/${path}`, payload === undefined ? {} : {
    method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(payload),
  });
  const value = await response.json();
  if (!response.ok) throw new Error(typeof value.detail === 'string' ? value.detail : 'Revisa los valores ingresados.');
  return value;
}
const labels = {hibrido: 'Híbrido', solo_contenido: 'Solo contenido', popularidad: 'Popularidad', aleatorio: 'Aleatorio'};
async function init() {
  const [meta, students] = await Promise.all([api('meta'), api('students')]);
  const weights = new Map();
  let overrides = {};
  let revision = 0;
  for (const student of students) get('student').add(new Option(student.name, student.id));
  for (const factor of meta.factors) {
    const input = document.createElement('input');
    Object.assign(input, {type: 'number', min: '0', max: '1', step: '0.05', value: factor.default_weight});
    const label = text('label', factor.label);
    label.className = 'row';
    label.append(input);
    get('weights').append(label);
    weights.set(factor.id, input);
  }
  get('rules').append(...meta.rules.map(rule => text('p', `${rule.name} · ${rule.reference}`)));
  const params = () => ({weights: Object.fromEntries([...weights].map(([id, input]) => [id, Number(input.value)])),
    ...Object.fromEntries(['k', 'm', 'top_n'].map(id => [id, Number(get(id).value)]))});
  function showProfile() {
    overrides = {};
    const student = students.find(s => s.id === get('student').value);
    const municipality = document.createElement('input');
    municipality.value = student.municipality;
    municipality.addEventListener('change', () => { overrides.municipality = municipality.value; });
    const locality = text('label', 'Municipio ');
    locality.append(municipality);
    const modality = document.createElement('select');
    for (const option of ['presencial', 'remota', 'cualquiera']) modality.add(new Option(option));
    modality.value = student.modality_pref;
    modality.addEventListener('change', () => { overrides.modality_pref = modality.value; });
    const preference = text('label', 'Modalidad ');
    preference.append(modality);
    get('student-form').replaceChildren(locality, preference, text('p', `Áreas preferidas: ${student.area_prefs.join(', ')}`));
  }
  async function recommend() {
    const current = ++revision;
    get('summary').textContent = 'Calculando…';
    get('ranking').replaceChildren();
    get('excluded').replaceChildren();
    get('excluded-title').textContent = 'Plazas excluidas';
    try {
      const result = await api('recommend', {...params(), student_id: get('student').value, overrides});
      if (current !== revision) return;
      get('summary').textContent = result.message || `${result.student.name}: ${result.eligible_count} plazas elegibles`;
      get('ranking').replaceChildren(...result.ranking.map(item => {
        const card = document.createElement('article');
        card.append(text('h3', `#${item.rank} · ${item.organization} · ${number(item.score)}`),
          text('p', `${item.area} · ${item.municipality} · ${item.modality} · ${item.available} cupos`));
        if (item.cold_start) card.append(text('p', 'Escenario sin historial: usa el promedio general.'));
        for (const factor of Object.values(item.factors)) {
          const meter = document.createElement('meter');
          meter.max = 1;
          meter.value = factor.contribution;
          const label = text('label', `${factor.label}: +${number(factor.contribution)} — ${factor.text} `);
          label.append(meter);
          card.append(label);
        }
        return card;
      }));
      get('excluded-title').textContent = `Plazas excluidas (${result.excluded.length})`;
      get('excluded').replaceChildren(...result.excluded.flatMap(p => p.violations.map(v =>
        row([p.placement_id, p.organization, v.rule_name, v.reason, v.reference]))));
    } catch (error) { if (current === revision) get('summary').textContent = error.message; }
  }
  get('student').addEventListener('change', showProfile);
  get('recomendar').addEventListener('change', recommend);
  get('reset').onclick = () => {
    for (const f of meta.factors) weights.get(f.id).value = f.default_weight;
    for (const [id, value] of Object.entries(meta.defaults)) get(id).value = value;
    showProfile();
    recommend();
  };
  get('run-cohort').onclick = async () => {
    const summary = get('cohort-summary');
    const table = get('cohort-table');
    table.classList.add('hidden');
    summary.textContent = 'Calculando…';
    try {
      const {hungaro, greedy} = await api('cohort', params());
      const lookup = result => new Map(result.assignments.map(a => [a.student_id, a]));
      const h = lookup(hungaro), g = lookup(greedy);
      summary.textContent = `Húngaro: ${hungaro.assigned} asignados (${number(hungaro.total_score)} puntos) · Greedy: ${greedy.assigned} asignados (${number(greedy.total_score)} puntos)`;
      table.tBodies[0].replaceChildren(...students.map(s => {
        const a = h.get(s.id), b = g.get(s.id);
        return row([s.name, a?.organization ?? 'Sin plaza', a ? number(a.score) : '—', b?.organization ?? 'Sin plaza', b ? number(b.score) : '—']);
      }));
      table.classList.remove('hidden');
    } catch (error) { summary.textContent = error.message; }
  };
  const loaded = new Set();
  for (const button of get('tabs').querySelectorAll('button')) button.onclick = async () => {
    const tab = button.dataset.tab;
    for (const node of document.querySelectorAll('.tab, #tabs button')) node.classList.toggle('active', node.id === tab || node === button);
    if (loaded.has(tab)) return;
    try {
      if (tab === 'evaluacion') {
        const result = await api('evaluation');
        get('eval-n').textContent = result.estudiantes_prueba;
        get('eval-table').replaceChildren(...Object.entries(result.metodos).map(([id, m]) => row([labels[id], m.ndcg_at_5, m.precision_at_5, m.nota_top1])));
        get('bias-table').replaceChildren(...['hibrido', 'popularidad'].map(id => {
          const m = result.sesgo_popularidad[id];
          return row([labels[id], `${(100*m.cobertura).toFixed(1)} %`, `${(100*m.concentracion_top20).toFixed(1)} %`]);
        }));
      }
      if (tab === 'plazas') get('placements').replaceChildren(...(await api('placements')).map(p => row([
        p.id, p.organization, p.sector, p.municipality, p.area, p.modality, p.available, p.agreement_until, p.history_count, p.mean_rating ?? '—',
      ])));
      loaded.add(tab);
    } catch (error) { get(tab === 'plazas' ? 'placements' : 'eval-table').replaceChildren(row([error.message])); }
  };
  showProfile();
  await recommend();
}
init().catch(error => { get('summary').textContent = error.message; });
