#!/usr/bin/env python3
"""Coleta PSM/CID de Issues do Milestone e gera relatório e gráficos."""
import json
import os
import re
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import datetime, date, timezone, timedelta
from pathlib import Path

API = 'https://api.github.com'
TOKEN = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN', '')
REPO = os.environ.get('GITHUB_REPOSITORY', '')
MILESTONE_TITLE = os.environ.get('PSM_MILESTONE', 'Entrega 1 — Fases 1 e 2')
OUTPUT = Path(os.environ.get('PSM_OUTPUT_DIR', 'relatorios/psm'))
TZ_BR = timezone(timedelta(hours=-3))


def get_json(path):
    url = path if path.startswith('https://') else API + path
    headers = {'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28', 'User-Agent': 'qs1-psm-metrics'}
    if TOKEN:
        headers['Authorization'] = f'Bearer {TOKEN}'
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as response:
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


def field(body, title):
    """Extrai conteúdo sob heading Markdown ###, até o próximo heading."""
    pattern = r'^\s*#{2,6}\s+' + re.escape(title) + r'\s*\r?\n(.*?)(?=^\s*#{1,6}\s+|\Z)'
    match = re.search(pattern, body or '', re.I | re.M | re.S)
    return match.group(1).strip() if match else None


def parse_estimate(body):
    raw = field(body, 'Estimativa (horas)')
    if raw is None:
        return None
    match = re.fullmatch(r'\s*(\d+(?:[.,]\d+)?)\s*(?:h|horas?)?\s*', raw, re.I)
    if not match:
        return None
    return float(match.group(1).replace(',', '.'))


def parse_actual(body):
    raw = field(body, 'Horas reais')
    if raw is None or not raw.strip():
        return [], []
    entries, invalid = [], []
    pattern = re.compile(r'^\s*(?:[-*]\s*)?(\d{1,2}/\d{1,2}/\d{4})\s*[-–]\s*(.+?)\s*[-–]\s*(\d+(?:[.,]\d+)?)\s*h\s*$', re.I)
    for line in raw.splitlines():
        if not line.strip() or line.strip() in ('—', '-', '_No response_'):
            continue
        match = pattern.fullmatch(line.strip())
        if not match:
            invalid.append(line.strip())
            continue
        when, person, hours = match.groups()
        try:
            day = datetime.strptime(when, '%d/%m/%Y').date()
            amount = float(hours.replace(',', '.'))
            if amount <= 0 or day > datetime.now(TZ_BR).date():
                raise ValueError('horas inválidas ou data futura')
            entries.append({'data': day.isoformat(), 'integrante': person.strip(), 'horas': amount})
        except ValueError:
            invalid.append(line.strip())
    return entries, invalid


def parse_dt(value):
    return datetime.fromisoformat(value.replace('Z', '+00:00')) if value else None


def closed_series(issues, events_by_issue, end_day):
    """Reconstrói fechamentos líquidos por dia, inclusive reaberturas."""
    changes = defaultdict(int)
    for issue in issues:
        number = issue['number']
        events = sorted((e for e in events_by_issue[number] if e.get('event') in ('closed', 'reopened') and e.get('created_at')), key=lambda e: e['created_at'])
        if events:
            for e in events:
                day = parse_dt(e['created_at']).astimezone(TZ_BR).date().isoformat()
                changes[day] += 1 if e['event'] == 'closed' else -1
        elif issue['state'] == 'closed' and issue.get('closed_at'):
            day = parse_dt(issue['closed_at']).astimezone(TZ_BR).date().isoformat()
            changes[day] += 1
    start = min([parse_dt(i['created_at']).astimezone(TZ_BR).date() for i in issues] + [end_day])
    days, values, count = [], [], 0
    cursor = start
    while cursor <= end_day:
        count += changes[cursor.isoformat()]
        days.append(cursor.isoformat())
        values.append(count)
        cursor += timedelta(days=1)
    return days, values


def make_charts(records, issues, events_by_issue, end_day):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'figure.dpi': 130, 'font.size': 10})
    by_day = defaultdict(float)
    by_person = defaultdict(float)
    for r in records:
        by_day[r['data']] += r['horas']
        by_person[r['integrante']] += r['horas']
    dates, completed = closed_series(issues, events_by_issue, end_day)
    def save(name):
        plt.tight_layout()
        plt.savefig(OUTPUT / name, bbox_inches='tight')
        plt.close()
    # Série diária, inclusive dias sem registro.
    hours = [by_day.get(day, 0) for day in dates]
    plt.figure(figsize=(11, 4.4))
    plt.bar(range(len(dates)), hours)
    step = max(1, len(dates) // 10)
    plt.xticks(range(0, len(dates), step), [dates[i][5:] for i in range(0, len(dates), step)], rotation=35)
    plt.title('Horas registradas por dia (Milestone)')
    plt.ylabel('Horas')
    plt.xlabel('Data (MM-DD)')
    save('horas_ao_longo_do_tempo.png')
    plt.figure(figsize=(11, 4.4))
    plt.plot(range(len(dates)), completed, marker='.', markersize=3)
    plt.xticks(range(0, len(dates), step), [dates[i][5:] for i in range(0, len(dates), step)], rotation=35)
    plt.title('Issues concluídas ao longo do tempo (saldo após reaberturas)')
    plt.ylabel('Issues concluídas')
    plt.xlabel('Data (MM-DD)')
    save('issues_concluidas_ao_longo_do_tempo.png')
    names = sorted(by_person, key=lambda p: (-by_person[p], p.lower()))
    plt.figure(figsize=(max(7, len(names) * 1.1), 4.5))
    if names:
        plt.bar(names, [by_person[p] for p in names])
        plt.xticks(rotation=30, ha='right')
    else:
        plt.text(.5, .5, 'Sem registros de horas', ha='center', va='center', transform=plt.gca().transAxes)
    plt.title('Horas realizadas por integrante')
    plt.ylabel('Horas')
    save('esforco_por_integrante.png')
    # Comparação por Issue; sem estimativa não é tratada como zero.
    pairs = [(i['number'], i['estimativa'], i['horas']) for i in issues if i['estimativa'] is not None]
    plt.figure(figsize=(max(8, len(pairs) * .65), 4.8))
    if pairs:
        xs = list(range(len(pairs)))
        plt.bar([x - .2 for x in xs], [p[1] for p in pairs], width=.4, label='Estimado')
        plt.bar([x + .2 for x in xs], [p[2] for p in pairs], width=.4, label='Realizado')
        plt.xticks(xs, [f'#{p[0]}' for p in pairs], rotation=45)
        plt.legend()
    else:
        plt.text(.5, .5, 'Nenhuma estimativa válida', ha='center', va='center', transform=plt.gca().transAxes)
    plt.title('Esforço estimado x realizado por Issue (com estimativa)')
    plt.ylabel('Horas')
    save('estimado_vs_realizado_por_issue.png')


def main():
    if not TOKEN:
        raise ValueError('Defina GH_TOKEN (ou GITHUB_TOKEN)')
    if not REPO or '/' not in REPO:
        raise ValueError('Defina GITHUB_REPOSITORY como organizacao/repositorio')
    milestone_list = list(pages(f'/repos/{REPO}/milestones?state=all'))
    milestone = next((m for m in milestone_list if m['title'] == MILESTONE_TITLE), None)
    if milestone is None:
        found = ', '.join(m['title'] for m in milestone_list) or '(nenhum)'
        raise ValueError(f'Milestone {MILESTONE_TITLE!r} não encontrado. Disponíveis: {found}')
    issues = [i for i in pages(f'/repos/{REPO}/issues?state=all&milestone={milestone["number"]}&sort=created&direction=asc') if 'pull_request' not in i]
    planned = len(issues)
    closed = sum(i['state'] == 'closed' and i.get('state_reason') != 'not_planned' for i in issues)
    assigned = sum(bool(i.get('assignees')) for i in issues)
    reopened, reopened_closed, events_by_issue = [], [], {}
    entries, invalid_lines, missing_estimates, per_issue = [], {}, [], []
    for issue in issues:
        number = issue['number']
        events = list(pages(f'/repos/{REPO}/issues/{number}/events'))
        events_by_issue[number] = events
        if any(e.get('event') == 'reopened' for e in events):
            reopened.append(number)
            if issue['state'] == 'closed':
                reopened_closed.append(number)
        estimate = parse_estimate(issue.get('body'))
        actual, invalid = parse_actual(issue.get('body'))
        if estimate is None:
            missing_estimates.append(number)
        if invalid:
            invalid_lines[str(number)] = invalid
        for row in actual:
            entries.append({'issue': number, **row})
        issue['estimativa'] = estimate
        issue['horas'] = round(sum(x['horas'] for x in actual), 3)
        per_issue.append({'issue': number, 'titulo': issue.get('title', ''), 'estimativa_horas': estimate, 'realizado_horas': issue['horas'], 'registros': len(actual), 'linhas_invalidas': invalid})
    estimated = sum(i['estimativa'] for i in issues if i['estimativa'] is not None)
    realized = sum(x['horas'] for x in entries)
    # Não publicar indicador potencialmente enganoso se falta estimativa ou há linhas inválidas.
    valid_effort = not missing_estimates and not invalid_lines and estimated > 0
    ratio = round(realized / estimated, 3) if valid_effort else None
    now = datetime.now(timezone.utc)
    metrics = {
        'coletado_em_utc': now.isoformat(), 'repositorio': REPO, 'milestone': MILESTONE_TITLE,
        'total_issues': planned, 'issues_fechadas_atualmente': closed, 'issues_com_responsavel': assigned,
        'issues_reabertas_historicamente': reopened, 'issues_fechadas_atualmente_que_foram_reabertas': reopened_closed,
        'psm_1_retrabalho_pct': round(100 * len(reopened_closed) / closed, 2) if closed else None,
        'psm_2_progresso_pct': round(100 * closed / planned, 2) if planned else None,
        'psm_3_razao_esforco': ratio, 'horas_estimadas': round(estimated, 3), 'horas_realizadas': round(realized, 3),
        'issues_sem_estimativa': missing_estimates, 'linhas_horas_invalidas': invalid_lines,
        'horas_por_issue': per_issue, 'registros_horas': entries,
    }
    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / 'metricas.json').write_text(json.dumps(metrics, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    make_charts(entries, issues, events_by_issue, now.astimezone(TZ_BR).date())
    def pct(x):
        return 'N/A' if x is None else f'{x:.2f}%'
    def h(x):
        return f'{x:.2f} h'
    report = f'''# Relatório automático PSM/CID

- **Repositório:** `{REPO}`
- **Milestone:** {MILESTONE_TITLE}
- **Coleta (UTC):** {metrics['coletado_em_utc']}

| Indicador | Numerador | Denominador | Resultado |
|---|---:|---:|---:|
| PSM-1 — Retrabalho* | {len(reopened_closed)} | {closed} | {pct(metrics['psm_1_retrabalho_pct'])} |
| PSM-2 — Progresso | {closed} | {planned} | {pct(metrics['psm_2_progresso_pct'])} |
| PSM-3 — Razão de esforço | {h(realized)} | {h(estimated)} | {f'{ratio:.3f}' if ratio is not None else 'N/A (dados incompletos)'} |

**Issues com reabertura histórica:** {', '.join('#'+str(n) for n in reopened) or 'Nenhuma'}.

**Issues atualmente fechadas que foram reabertas:** {', '.join('#'+str(n) for n in reopened_closed) or 'Nenhuma'}.

## Qualidade dos dados

- Issues sem estimativa válida: {', '.join('#'+str(n) for n in missing_estimates) or 'Nenhuma'}.
- Issues com linhas inválidas no campo Horas reais: {', '.join('#'+n for n in invalid_lines) or 'Nenhuma'}.
- Registros de horas válidos: {len(entries)}.
- Total de horas realizadas válidas: {h(realized)}.

## Esforço por Issue

| Issue | Estimado | Realizado | Registros |
|---|---:|---:|---:|
'''
    for i in per_issue:
        report += f"| [#{i['issue']}](https://github.com/{REPO}/issues/{i['issue']}) | {h(i['estimativa_horas']) if i['estimativa_horas'] is not None else 'Não informado'} | {h(i['realizado_horas'])} | {i['registros']} |\n"
    report += '''
## Gráficos

![Horas registradas por dia](horas_ao_longo_do_tempo.png)

![Issues concluídas ao longo do tempo](issues_concluidas_ao_longo_do_tempo.png)

![Esforço por integrante](esforco_por_integrante.png)

![Estimado versus realizado por Issue](estimado_vs_realizado_por_issue.png)

## Definições e limites

- Escopo: Issues do Milestone, excluindo Pull Requests.
- PSM-1: fotografia acumulada de Issues atualmente fechadas que já foram reabertas. **Não** é taxa por período; Issues reabertas ainda abertas não entram no numerador.
- PSM-2: proporção de Issues atualmente fechadas como concluídas. Milestone atual não é uma linha de base imutável.
- PSM-3: soma de horas realizadas / soma de horas estimadas das Issues do Milestone. É **N/A** se faltar qualquer estimativa, houver linhas inválidas ou o total estimado for zero. Horas realizadas não registradas não podem ser detectadas automaticamente.
- Registros de horas são lidos do campo `### Horas reais` do corpo atual das Issues. Datas declaradas pelos integrantes são usadas no gráfico; edições posteriores podem alterar séries históricas.
- As datas do gráfico de Issues concluídas vêm dos eventos de fechamento e reabertura do GitHub, no fuso de Brasília.
- Gráficos de horas mostram **esforço registrado**, não produtividade individual nem qualidade do trabalho.
- Atualizar manualmente interpretação, decisões e evidências no documento da disciplina.
'''
    if invalid_lines:
        report += '\n### Linhas de horas não reconhecidas\n\n'
        for n, lines in invalid_lines.items():
            for line in lines:
                report += f'- Issue #{n}: `{line}`\n'
    (OUTPUT / 'relatorio.md').write_text(report, encoding='utf-8')
    print(report)


if __name__ == '__main__':
    try:
        main()
    except (ValueError, urllib.error.HTTPError, urllib.error.URLError) as exc:
        print(f'ERRO: {exc}', file=sys.stderr)
        sys.exit(1)
