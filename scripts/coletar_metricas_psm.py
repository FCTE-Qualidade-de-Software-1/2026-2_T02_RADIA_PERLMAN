#!/usr/bin/env python3
"""Coleta PSM/CID de múltiplos milestones; horas no corpo das Issues."""
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

API = 'https://api.github.com'
TOKEN = os.getenv('GH_TOKEN') or os.getenv('GITHUB_TOKEN', '')
REPO = os.getenv('GITHUB_REPOSITORY', '')
TITLES = [s.strip() for s in os.getenv('PSM_MILESTONES', 'Entrega 1 — Fases 1 e 2;Entrega 2 — Fases 3 e 4').split(';') if s.strip()]
OUTPUT = Path(os.getenv('PSM_OUTPUT_DIR', 'relatorios/psm'))
HOURS_PATTERN = re.compile(r'^\s*[-*]?\s*(\d{1,2}/\d{1,2}/\d{4})\s*[-–]\s*(.+?)\s*[-–]\s*(\d+(?:[.,]\d+)?)\s*h\s*$', re.I)


def get_json(path):
    url = path if path.startswith('https://') else API + path
    headers = {'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28', 'User-Agent': 'qs1-psm-metrics'}
    if TOKEN:
        headers['Authorization'] = f'Bearer {TOKEN}'
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=40) as response:
        return json.load(response)


def pages(path):
    page = 1
    while True:
        join = '&' if '?' in path else '?'
        batch = get_json(f'{path}{join}per_page=100&page={page}')
        if not isinstance(batch, list):
            raise ValueError('A API não retornou uma lista paginada')
        yield from batch
        if len(batch) < 100:
            return
        page += 1


def field(body, name):
    pattern = (
        r'^\s*#{2,3}\s+' + re.escape(name) +
        r'\s*\n(.*?)(?=^\s*#{1,6}\s+|\Z)'
    )

    match = re.search(
        pattern,
        body or '',
        re.I | re.M | re.S
    )

    return match.group(1).strip() if match else ''


def parse_hours(issue):
    body = issue.get('body') or ''
    estimate_text = field(body, 'Estimativa (horas)').replace(',', '.').strip()
    try:
        estimate = float(re.fullmatch(r'(\d+(?:\.\d+)?)\s*h?', estimate_text, re.I).group(1))
    except (AttributeError, ValueError):
        estimate = None
    entries, errors = [], []
    for line in field(body, 'Horas reais').splitlines():
        if not line.strip() or line.strip() in ('-', '*'):
            continue
        m = HOURS_PATTERN.fullmatch(line)
        if not m:
            errors.append(line.strip())
            continue
        raw_date, person, raw_hours = m.groups()
        try:
            day = datetime.strptime(raw_date, '%d/%m/%Y').date().isoformat()
            hours = float(raw_hours.replace(',', '.'))
            if hours <= 0 or not person.strip():
                raise ValueError('Horas ou integrante inválidos')
        except ValueError:
            errors.append(line.strip())
            continue
        entries.append({'data': day, 'integrante': person.strip(), 'horas': hours, 'issue': issue['number']})
    return estimate, entries, errors


def percent(a, b):
    return round(a * 100 / b, 2) if b else None


def ratio(a, b):
    return round(a / b, 3) if b else None


def plot_series(data, title, ylabel, filename):
    fig, ax = plt.subplots(figsize=(10, 4.8))
    if data:
        keys = sorted(data)
        ax.plot(keys, [data[k] for k in keys], marker='o')
        ax.tick_params(axis='x', rotation=45)
    else:
        ax.text(.5, .5, 'Sem dados disponíveis', ha='center', va='center', transform=ax.transAxes)
    ax.set(title=title, ylabel=ylabel)
    ax.grid(axis='y', alpha=.3)
    fig.tight_layout()
    fig.savefig(filename, dpi=160)
    plt.close(fig)


def plot_bars(data, title, ylabel, filename):
    fig, ax = plt.subplots(figsize=(10, 4.8))
    if data:
        keys = list(sorted(data, key=data.get, reverse=True))
        ax.bar(keys, [data[k] for k in keys])
        ax.tick_params(axis='x', rotation=35)
    else:
        ax.text(.5, .5, 'Sem dados disponíveis', ha='center', va='center', transform=ax.transAxes)
    ax.set(title=title, ylabel=ylabel)
    fig.tight_layout()
    fig.savefig(filename, dpi=160)
    plt.close(fig)


def progress_history(issues, event_map):
    """Série de issues concluídas por dia; reaberturas reduzem total."""
    events = []
    for issue in issues:
        for ev in event_map[issue['number']]:
            if ev.get('event') in ('closed', 'reopened') and ev.get('created_at'):
                events.append((ev['created_at'][:10], issue['number'], ev['event']))
    events.sort()
    state = set()
    history = {}
    for day, number, action in events:
        if action == 'closed':
            state.add(number)
        else:
            state.discard(number)
        history[day] = len(state)
    return history


def evaluate(title, issues, event_map, folder):
    folder.mkdir(parents=True, exist_ok=True)
    reopened, reopened_closed, entries, missing, invalid = [], [], [], [], []
    estimate_total = 0.0
    for issue in issues:
        n = issue['number']
        if any(ev.get('event') == 'reopened' for ev in event_map[n]):
            reopened.append(n)
            if issue['state'] == 'closed':
                reopened_closed.append(n)
        estimate, logs, errors = parse_hours(issue)
        if estimate is None:
            missing.append(n)
        else:
            estimate_total += estimate
        entries.extend(logs)
        if errors:
            invalid.append({'issue': n, 'linhas': errors})
    closed = sum(i['state'] == 'closed' and i.get('state_reason') != 'not_planned' for i in issues)
    closed_for_rework = sum(i['state'] == 'closed' for i in issues)
    real_total = sum(e['horas'] for e in entries)
    effort = ratio(real_total, estimate_total) if not missing else None
    daily, people = defaultdict(float), defaultdict(float)
    for e in entries:
        daily[e['data']] += e['horas']
        people[e['integrante']] += e['horas']
    progress = progress_history(issues, event_map)
    plot_series(daily, f'Horas registradas por dia — {title}', 'Horas', folder / 'horas_ao_longo_do_tempo.png')
    plot_series(progress, f'Issues concluídas ao longo do tempo — {title}', 'Issues concluídas', folder / 'issues_concluidas_ao_longo_do_tempo.png')
    plot_bars(people, f'Esforço por integrante — {title}', 'Horas', folder / 'esforco_por_integrante.png')
    metric = {
        'milestone': title, 'total_issues': len(issues), 'issues_concluidas': closed,
        'psm_1_retrabalho_pct': percent(len(reopened_closed), closed_for_rework),
        'psm_2_progresso_pct': percent(closed, len(issues)),
        'psm_3_razao_esforco': effort,
        'horas_estimadas': round(estimate_total, 2), 'horas_reais': round(real_total, 2),
        'issues_sem_estimativa': missing, 'linhas_de_horas_invalidas': invalid,
        'issues_reabertas': reopened, 'issues_reabertas_atualmente_fechadas': reopened_closed,
        'horas_por_integrante': dict(sorted(people.items())), 'horas_por_dia': dict(sorted(daily.items())),
        'issues_concluidas_por_dia': progress, 'registros_horas': entries,
    }
    (folder / 'metricas.json').write_text(json.dumps(metric, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    def fmt(x, suffix=''):
        return 'N/A' if x is None else f'{x:.2f}{suffix}'
    report = f'''# Relatório automático PSM/CID — {title}

- **Repositório:** `{REPO}`
- **Coleta (UTC):** {datetime.now(timezone.utc).isoformat()}

| Indicador | Resultado |
|---|---:|
| PSM-1 — Retrabalho (fotografia atual) | {fmt(metric['psm_1_retrabalho_pct'], '%')} |
| PSM-2 — Progresso | {fmt(metric['psm_2_progresso_pct'], '%')} |
| PSM-3 — Razão de esforço (horas reais / estimadas) | {fmt(effort)} |

- **Issues:** {len(issues)}; concluídas: {closed}
- **Horas estimadas:** {estimate_total:.2f} h; **reais:** {real_total:.2f} h
- **Issues sem estimativa válida:** {', '.join('#'+str(n) for n in missing) or 'Nenhuma'}
- **Issues com linhas de horas inválidas:** {', '.join('#'+str(i['issue']) for i in invalid) or 'Nenhuma'}
- **Issues reabertas:** {', '.join('#'+str(n) for n in reopened) or 'Nenhuma'}

## Gráficos

![Horas ao longo do tempo](horas_ao_longo_do_tempo.png)

![Issues concluídas ao longo do tempo](issues_concluidas_ao_longo_do_tempo.png)

![Esforço por integrante](esforco_por_integrante.png)

## Limitações

- O PSM-1 considera apenas issues atualmente fechadas que já foram reabertas; não é uma taxa por período.
- O PSM-2 usa a composição atual do Milestone, não uma linha de base fixa.
- O PSM-3 fica N/A se alguma Issue não tiver estimativa válida. Horas reais ausentes são tratadas como zero registrado, **não** como prova de ausência de trabalho.
- Datas de horas são as informadas manualmente no corpo das Issues. Registros podem ser alterados e devem ser conferidos pela equipe.
- O gráfico de conclusão usa eventos de fechamento e reabertura do GitHub; não mede horas de produtividade.
'''
    (folder / 'relatorio.md').write_text(report, encoding='utf-8')
    return metric


def main():
    if not TOKEN:
        raise ValueError('Defina GH_TOKEN (ou GITHUB_TOKEN)')
    if not REPO or '/' not in REPO:
        raise ValueError('Defina GITHUB_REPOSITORY')
    milestones = list(pages(f'/repos/{REPO}/milestones?state=all'))
    OUTPUT.mkdir(parents=True, exist_ok=True)
    all_issues, all_events, summaries = [], {}, []
    for idx, title in enumerate(TITLES, 1):
        milestone = next((m for m in milestones if m['title'] == title), None)
        if milestone is None:
            print(f'AVISO: Milestone {title!r} não encontrado; ignorado.', file=sys.stderr)
            continue
        issues = [i for i in pages(f'/repos/{REPO}/issues?state=all&milestone={milestone["number"]}&sort=created&direction=asc') if 'pull_request' not in i]
        event_map = {i['number']: list(pages(f'/repos/{REPO}/issues/{i["number"]}/events')) for i in issues}
        summary = evaluate(title, issues, event_map, OUTPUT / f'entrega_{idx}')
        summaries.append(summary)
        all_issues.extend(issues)
        all_events.update(event_map)
        print(f'{title}: {len(issues)} issues; {summary["horas_reais"]} h reais')
    if not summaries:
        raise ValueError('Nenhum dos Milestones configurados foi encontrado')
    # Consolidado: somente issues únicas, sem somar porcentagens.
    unique = {i['number']: i for i in all_issues}
    consolidated = evaluate('Consolidado das entregas', list(unique.values()), all_events, OUTPUT / 'consolidado')
    index = {'coletado_em_utc': datetime.now(timezone.utc).isoformat(), 'repositorio': REPO, 'entregas': summaries, 'consolidado': consolidated}
    (OUTPUT / 'metricas.json').write_text(json.dumps(index, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    lines = ['# PSM/CID — Entregas', '', '| Escopo | Issues | Progresso | Horas previstas | Horas registradas | Razão esforço |', '|---|---:|---:|---:|---:|---:|']
    for s in summaries + [consolidated]:
        f = lambda x: 'N/A' if x is None else str(x)
        lines.append(f'| {s["milestone"]} | {s["total_issues"]} | {f(s["psm_2_progresso_pct"])}% | {s["horas_estimadas"]} | {s["horas_reais"]} | {f(s["psm_3_razao_esforco"])} |')
    lines += ['', 'Relatórios detalhados nas pastas `entrega_1/`, `entrega_2/` e `consolidado/` (se os marcos existirem).', '']
    (OUTPUT / 'relatorio.md').write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))

if __name__ == '__main__':
    try:
        main()
    except (ValueError, urllib.error.HTTPError, urllib.error.URLError) as exc:
        print(f'ERRO: {exc}', file=sys.stderr)
        sys.exit(1)
