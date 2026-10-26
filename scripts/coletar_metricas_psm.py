#!/usr/bin/env python3
"""Coleta PSM/CID de issues de um milestone usando apenas a API REST do GitHub."""
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

API = 'https://api.github.com'
TOKEN = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN', '')
REPO = os.environ.get('GITHUB_REPOSITORY', '')
MILESTONE_TITLE = os.environ.get('PSM_MILESTONE', 'Entrega 1 — Fases 1 e 2')
OUTPUT = Path(os.environ.get('PSM_OUTPUT_DIR', 'relatorios/psm'))


def get_json(path):
    url = path if path.startswith('https://') else API + path
    req = urllib.request.Request(url, headers={
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {TOKEN}',
        'X-GitHub-Api-Version': '2022-11-28',
        'User-Agent': 'qs1-psm-metrics',
    })
    with urllib.request.urlopen(req, timeout=30) as response:
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
            break
        page += 1


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

    issues = [i for i in pages(f'/repos/{REPO}/issues?state=all&milestone={milestone["number"]}&sort=created&direction=asc')
              if 'pull_request' not in i]
    planned = len(issues)
    closed = sum(i['state'] == 'closed' for i in issues)
    assigned = sum(bool(i.get('assignees')) for i in issues)

    # A API de eventos identifica reaberturas mesmo quando a issue já foi fechada novamente.
    reopened = []
    for issue in issues:
        events = pages(f'/repos/{REPO}/issues/{issue["number"]}/events')
        if any(event.get('event') == 'reopened' for event in events):
            reopened.append(issue['number'])

    # PSM-1: entre as issues atualmente fechadas, quantas já foram reabertas.
    reopened_closed = [n for n in reopened if any(i['number'] == n and i['state'] == 'closed' for i in issues)]
    metrics = {
        'coletado_em_utc': datetime.now(timezone.utc).isoformat(),
        'repositorio': REPO,
        'milestone': MILESTONE_TITLE,
        'total_issues': planned,
        'issues_fechadas_atualmente': closed,
        'issues_com_responsavel': assigned,
        'issues_reabertas_historicamente': reopened,
        'issues_fechadas_atualmente_que_foram_reabertas': reopened_closed,
        'psm_1_retrabalho_pct': round(100 * len(reopened_closed) / closed, 2) if closed else None,
        'psm_2_progresso_pct': round(100 * closed / planned, 2) if planned else None,
        'psm_3_atribuicao_pct': round(100 * assigned / planned, 2) if planned else None,
    }
    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / 'metricas.json').write_text(json.dumps(metrics, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

    def fmt(value):
        return 'N/A (denominador zero)' if value is None else f'{value:.2f}%'

    report = f'''# Relatório automático PSM/CID

- **Repositório:** `{REPO}`
- **Milestone:** {MILESTONE_TITLE}
- **Coleta (UTC):** {metrics['coletado_em_utc']}

| Indicador | Numerador | Denominador | Resultado |
|---|---:|---:|---:|
| PSM-1 — Retrabalho* | {len(reopened_closed)} | {closed} | {fmt(metrics['psm_1_retrabalho_pct'])} |
| PSM-2 — Progresso | {closed} | {planned} | {fmt(metrics['psm_2_progresso_pct'])} |
| PSM-3 — Cobertura de atribuição | {assigned} | {planned} | {fmt(metrics['psm_3_atribuicao_pct'])} |

**Issues atualmente fechadas que foram reabertas:** {', '.join('#'+str(n) for n in reopened_closed) or 'Nenhuma'}.

**Todas as Issues com evento de reabertura:** {', '.join('#'+str(n) for n in reopened) or 'Nenhuma'}.

## Definições e limites

- Escopo: somente Issues do Milestone, excluindo Pull Requests.
- PSM-1*: fotografia acumulada do Milestone, **não** a taxa de reabertura em um período. O numerador conta Issues atualmente fechadas com pelo menos um evento histórico de reabertura; o denominador conta Issues atualmente fechadas. Para o indicador original definido *por período*, seria necessário fixar datas e implementar a apuração histórica correspondente.
- PSM-2: percentual de Issues atualmente fechadas. Pressupõe que as Issues do Milestone correspondam à linha de base; mudanças no conjunto alteram o denominador.
- PSM-3: percentual de Issues com pelo menos um responsável, não esforço efetivo.
- Atualizar manualmente a interpretação e as decisões de gestão no documento da disciplina.
'''
    (OUTPUT / 'relatorio.md').write_text(report, encoding='utf-8')
    print(report)


if __name__ == '__main__':
    try:
        main()
    except (ValueError, urllib.error.HTTPError, urllib.error.URLError) as exc:
        print(f'ERRO: {exc}', file=sys.stderr)
        sys.exit(1)
