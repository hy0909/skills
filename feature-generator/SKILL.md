---
name: feature-generator
description: Create concise Korean 기능명세서 Markdown or XLSX files from raw text, existing XLSX, or MD tables. Use when the user wants a table-first feature spec with only essential planning rules above the requirements table, no duplicated FE/BE summaries, and the standard feature XLSX export.
---

# Feature Generator

Create table-first Korean 기능명세서 files.

## Output Principle

- Keep the MD short. The `요구사항 테이블` is the implementation source of truth.
- Above the table, write only `## 1. 핵심 기획 규칙`.
- Do not generate `목적·범위`, `IA 요약`, `본문`, `권한 요약`, `알림 요약`, `상태 요약`, or `백엔드 핵심 로직 요약` by default.
- Do not copy the same rule into both a summary section and a requirement row unless it prevents real misunderstanding.
- FE/BE-owned details belong in FE/BE docs. In this feature MD, include only planning meaning needed to implement the feature.

## MD Structure

Use this order:

1. Header
2. Metadata block
3. `## 1. 핵심 기획 규칙`
4. `## 2. 요구사항 테이블`
5. `## 3. 연관 링크`
6. `## 4. 변경 이력`

Use three `<br>` lines before each `##` heading.

## 핵심 기획 규칙

Read `references/core_summary_rules.md`.

Default table:

| 구분 | 핵심 기획 규칙 | 적용 범위 | 요구사항 연결 |
| --- | --- | --- | --- |

Rules:

- Max 5 rows unless the user explicitly asks for more.
- One row = one cross-cutting planning rule.
- Include only rules that affect multiple requirement rows or prevent implementation misunderstanding.
- If there is no meaningful cross-cutting rule, write one `공통` row saying the requirements table is the source of truth.

## 요구사항 테이블

Read `references/feature_content_rules.md`.

Always use columns:

`1depth`, `2depth`, `3depth`, `요구사항 ID`, `요구사항명`, `요청목적`, `기능 요구사항`, `프로세스 요구사항`, `화면 요구사항`, `보안 요구사항`, `데이터 요구사항`

Keep rows concise. Put detailed behavior in the relevant row, not in a repeated narrative section.

## XLSX

- For XLSX output, use `assets/feature_xlsx_template.xlsx`.
- For MD/Table to XLSX, use `scripts/md_table_to_feature_xlsx.py`.
- For XLSX to MD, use `scripts/xlsx_to_feature_md.py`.
- Preserve the standard XLSX design. Read `references/xlsx_design_rules.md` only when creating XLSX.

## Images

- Keep screenshots near the relevant requirement.
- Add a 1px `#D9DEE7` outer border without resizing/cropping/redrawing the original.
- Store assets in `assets/<topic>/`.

## Naming

- Use concise lowercase kebab-case: `<topic>.md`, `<topic>.xlsx`.
- Do not include `feature`, `기능명세서`, dates, versions, `draft`, or `final`.

## Guardrails

- Preserve source meaning; do not invent scope.
- Do not invent API, DB, enum, event, state machine, component architecture, or permission models.
- Use `TBD` or `원문 기준 추가 정의 필요` only when needed.
- Write `Codex, 김혜연` in change history.
