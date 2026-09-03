---
name: feature-generator
description: Create concise Korean 기능명세서 Markdown or XLSX files from Figma screens, raw text, existing XLSX, or MD tables. Use for a new service or feature and for improvements to an existing product when the user wants 목적·범위, a short 핵심 기획 규칙 table, a 기능명세서 table whose first column is 요구사항 ID, complete screen/function coverage, optional exception-policy review, peer feature-MD consistency review, Figma-to-spec alignment review, and standard XLSX export.
---

# Feature Generator

Create concise Korean 기능명세서 files.

## Workflow

1. Identify whether the source is Figma, text, an existing document, or a combination.
2. Determine whether the work is a blank-slate service/feature or a change to an existing product.
3. Read `references/coverage_exception_review.md` and build an internal coverage inventory before drafting.
4. Write the initial MD from source-confirmed scope and rules. Include exception behavior already defined by the source, but do not invent unspecified policy.
5. Verify that every in-scope screen, function, action, and explicitly shown state maps to a requirement row or a documented out-of-scope decision.
6. After the initial MD is complete, read `references/post_draft_reviews.md` and separately offer all three reviews: exception-policy gaps, consistency with other MD files in the feature folder, and Figma-to-MD alignment.
7. When commit/push was requested, do not commit or push until the user answers all three review offers and any approved changes are reflected.

## Input Context

- For Figma-based work, inspect all in-scope screens, variants, overlays, tabs, actions, and explicitly designed states. Keep the source link near the top of the MD.
- For text-based work, extract screens, roles, actions, states, data, results, and stated exception paths from the source.
- For an existing product change, inspect relevant neighboring feature documents and linked policies before treating a rule as missing. Search the repository's feature or feature-spec documentation area when it is available.
- If the required product context is unavailable or conflicting and would materially change the recommendation, ask for the missing source or decision. Do not criticize the user for rules that may exist outside the provided context.

## Output Principle

- Keep each MD short. Split by page (see Document Split) rather than growing one file.
- Use easy, clear Korean. Prefer short noun-style endings such as `데이터 출처 정의`, not long `~한다` prose.
- Write only planning information needed for implementation.
- Do not repeat the same rule in both the top section and the table unless it prevents misunderstanding.
- FE/BE-owned details belong in FE/BE documents. Feature MD keeps only planning meaning.

## Document Split

- One MD per page or screen. A flow with several screens becomes several MDs, not one long MD.
- Give a shared component (a dropdown, a card, a GNB element used by several pages) its own MD.
- Add one overview MD per flow only when there are two or more page MDs. It holds the flow order, cross-page rules, open decisions (`기획 결정 현황`), and links to every page MD. It does not repeat page rows.
- A single-screen feature stays in one MD. Do not split for the sake of splitting.
- Name page MDs `<flow>-<page>.md`, the component MD `<flow>-<component>.md`, the overview `<flow>.md`.

## No Duplication Across MDs

- Write each rule, copy string, and value once, in the MD that owns it. Other MDs link to it as `[file](file.md) REQ-ID` instead of restating it.
- Reason: when the same sentence lives in two files, one copy gets edited and the other goes stale.
- Allowed duplication is only what prevents a row from being misread on its own, for example a one-line state definition next to the row that depends on it. Keep it to a phrase and add the owner link in the same cell.
- Never duplicate: 문구표 rows, design values, permission tables, open-decision lists.
- Before finishing, search the page MDs for sentences that also appear in the overview MD and replace one side with a link.

## Copy (i18n) Table

- Multilingual copy (한국어 SSOT + English, Tiếng Việt, ...) goes in a separate MD, `<flow>-i18n.md`, in the same folder as the page MDs. It is the only place copy strings appear with their translations.
- Structure: metadata block, one table with columns `화면 | 요소 | 한국어 (SSOT) | English | ...`, a `번역 제외` list, change history.
- Page MDs name the element (`타이틀`, `버튼`) and link to the i18n MD. They may quote the Korean string once when the row is unreadable without it, never the translations.
- Tools that replace copy (Figma language plugin, i18n JSON export) read the i18n MD directly, so keep its table headers exactly as the language names.

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

## Figma Scroll Frames

- When a Figma frame name contains `scroll` (case-insensitive), always define scrolling in the relevant feature requirement.
- Determine the scroll container from the frame hierarchy and screen layout. Specify the scrolling area, direction, overflow condition, and elements that remain fixed.
- Place the scroll area on the actual content region represented by the named frame; do not automatically apply full-page scrolling.
- Do not omit scrolling only because the mockup does not show a scrollbar.
- If the named frame's location makes scrolling structurally unusual, or the intended scroll container is ambiguous, ask the user whether scrolling there is correct before finalizing the document.

## Naming

- Use concise lowercase kebab-case: `<topic>.md`, `<topic>.xlsx`.
- Do not include `feature`, `기능명세서`, dates, versions, `draft`, or `final`.

## Metadata

- Always write `owner_team: AI Platform Team` in the metadata block.
- Never copy another team name (for example `AI Research team`) from neighboring or older documents. When editing an existing document whose metadata has a different `owner_team`, change it to `AI Platform Team`.

## Guardrails

- Preserve source meaning; do not invent scope.
- Do not invent API, DB, enum, event, state machine, component architecture, or permission models.
- Treat the exception checklist as a coverage and recommendation tool, not permission to add unsupported policy to the MD.
- Describe missing context neutrally as `현재 자료에서 확인되지 않음`, `추가 정의 권장`, or `맥락 확인 필요`. Do not frame it as the user's mistake.
- Use `TBD` or `원문 기준 추가 정의 필요` only when needed.
- For Figma references, do not expose raw Figma URLs. Put the real URL behind Markdown link text near the top source link and in `## 4. 연관 링크`.
- When editing an existing document, preserve every existing change-history row.
- Add the current work as the newest row at the top. Combine changes made on the same date into one complete row unless the user requests separate rows.
- Never delete, shorten, reorder, or rewrite previous history without an explicit user request.
- Write `Codex, 김혜연` in change history.
