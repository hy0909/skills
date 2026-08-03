---
name: feature-generator
description: Create concise Korean 기능명세서 Markdown or XLSX files from raw text, existing XLSX, or MD tables. Use when the user wants a feature spec with 목적·범위, a short 핵심 기획 규칙 table, a 기능명세서 table whose first column is 요구사항 ID, no duplicated FE/BE summaries, and standard XLSX export.
---

# Feature Generator

Create concise Korean 기능명세서 files.

## Output Principle

- Keep the MD short.
- Use easy, clear Korean. Prefer short noun-style endings such as `데이터 출처 정의`, not long `~한다` prose.
- Write only planning information needed for implementation.
- Do not repeat the same rule in both the top section and the table unless it prevents misunderstanding.
- FE/BE-owned details belong in FE/BE documents. Feature MD keeps only planning meaning.

## MD Structure

Use this order:

1. Header
2. Metadata block
3. Top source links, only when needed
4. `## 1. 목적·범위`
5. `## 2. 핵심 기획 규칙`
6. `## 3. 기능명세서`
7. `## 4. 연관 링크`
8. `## 5. 변경 이력`

Use three `<br>` lines before each `##` heading.

## Top Source Links

- When a Figma source exists, place it immediately below the metadata block as a clickable Markdown link.
- Do not put Figma URLs or Figma labels inside the metadata code block because links do not render there.
- Use this format: `> Figma: [조달과제 건축현장안전관리 — 화면명](https://...)`

## 목적·범위

Write only two bullets:

- `목적:` one short noun-style phrase
- `범위:` included screens, data, or rules

Write only `목적` and `범위` bullets.

## 핵심 기획 규칙

Read `references/core_summary_rules.md`.

Default table:

| 구분 | 핵심 기획 규칙 | 적용 범위 | 요구사항 연결 |
| --- | --- | --- | --- |

Rules:

- Max 5 rows unless the user explicitly asks for more.
- One row = one cross-cutting planning rule.
- Include only rules that affect multiple 기능명세서 rows or prevent implementation misunderstanding.
- If there is no meaningful cross-cutting rule, write one `공통` row saying the 기능명세서 table is the source of truth.

## 기능명세서

Read `references/feature_content_rules.md`.

Always use columns in this exact order:

`요구사항 ID`, `1depth`, `2depth`, `3depth`, `요구사항명`, `요청목적`, `기능 요구사항`, `프로세스 요구사항`, `화면 요구사항`, `보안 요구사항`, `데이터 요구사항`

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
- For Figma references, do not expose raw Figma URLs. Put the real URL behind Markdown link text near the top source link and in `## 4. 연관 링크`.
- Write only the latest change-history row unless the user asks to preserve all history.
- Write `Codex, 김혜연` in change history.
