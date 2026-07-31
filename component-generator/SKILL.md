---
name: component-generator
description: Create concise Korean design-system component Markdown documents from Figma mockups, screenshots, notes, or existing MD files for planner/designer handoff. Use when the user wants a component spec organized by service usage and function-level behavior, with only necessary design definitions, no code, API, CSS, props, FE/BE architecture, or duplicated tables.
---

# Component Generator

Create concise Korean component design documents.

This skill is for 기획자·디자이너가 개발자에게 전달하는 디자인 컴포넌트 기준 문서. The document should explain what the component is, where it appears in the service, and what each user-facing function must do. Development design belongs to developers.

## Output Principle

- Keep the MD short.
- Use easy, clear Korean.
- Prefer short noun-style endings such as `공통 미디어 뷰어 컴포넌트`, not long `~한다` prose.
- Write only planning/design information needed for implementation handoff.
- Make `서비스 내 적용 위치` and `기능 단위 명세` the strongest parts of the document.
- Describe user-visible behavior, display rules, and interaction in function units.
- Do not repeat the same rule in multiple sections unless it prevents misunderstanding.
- Do not split one idea into many tables.
- Remove tables or sections that do not add a decision or implementation handoff value.
- Do not create `적용 범위` or `제외 범위` sections.
- Do not create `Implementation Notes`.
- Do not create `Figma 최신 텍스트 샘플`.
- Use `Do & Don't` only when a misuse risk is important enough to call out.

## Forbidden Content

Do not include:

- Code blocks or code snippets.
- API, DB, enum, event, state machine, props, class names, CSS, z-index, mount/unmount, player instance, or FE/BE architecture.
- Developer-owned component architecture.
- Implementation guesses not shown in the source.
- Duplicate summaries that restate table rows.
- Long separate tables for structure, display, interaction, and labels when one function table is enough.
- Long abstract wording that increases reading load.

Technical terms are allowed only when they are user-facing gestures or UI labels in the design, such as `pinch-to-zoom`, `double tap`, `progress bar`, or `Close button`.

## MD Structure

Use this order. Keep numbering contiguous.

1. Header
2. Metadata block
3. `## 1. 목적·범위`
4. `## 2. 서비스 내 적용 위치`
5. `## 3. 기능 단위 명세`
6. `## 4. 핵심 확인 체크리스트`
7. `## 5. 연관 링크`
8. `## 6. 변경이력`

Use `---` between top-level sections.

## Header & Metadata

Start every file with the component name as the H1, then a metadata block:

```md
# {{Component Name}}

> **Figma:** [{{시안명}}](figma://link/REPLACE_WITH_NODE_ID)
> **Status:** `Draft` · **Last updated:** {{YYYY-MM-DD}}
> **Owner:** Design System Team
```

- `Status`: `Draft`, `Review`, `Stable`, `Deprecated` 중 하나.
- `Last updated`: current date or user-provided date.
- `Figma`: use provided links only. Do not invent links.

## 목적·범위

Write only two bullets:

- `목적:` one short noun-style phrase.
- `범위:` included media, platforms, screens, or design rules.

Rules:

- End with a noun phrase where possible.
- Do not write an `적용 범위` table.
- Do not write an `제외 범위` section.
- Keep the wording easy and direct.

Example:

```md
- 목적: 사진과 영상을 큰 화면으로 확인하는 공통 미디어 뷰어 컴포넌트
- 범위: PC Web·Mobile App의 사진 확대, 영상 확대, 닫기, 재생 컨트롤 노출 기준
```

## 서비스 내 적용 위치

This is a core section.

Use a table that shows where the component appears in the service:

| 서비스 | 화면 위치 | PC Web | Mobile App | 표시 미디어 | 기준 |
| --- | --- | --- | --- | --- | --- |

Rules:

- Include only real or strongly relevant service locations from the source.
- Remove non-use rows unless they prevent a likely misunderstanding.
- Mark uncertain usage as `시안 확정 필요` only when the user needs that decision.
- Prefer service meaning over internal routing or rendering details.

## 기능 단위 명세

This is the main section.

Write a function-level table that helps developers understand the component behavior without code:

| 기능 | 사용 위치 | 조건·대상 | 사용자 액션 | 화면 반응 | 핵심 기준 |
| --- | --- | --- | --- | --- | --- |

Rules:

- One row should describe one user-facing function.
- Merge visual structure, display rules, interaction, and content labels into this table when possible.
- Include only rows needed to build or review the component.
- Use function names such as `사진 확대 열기`, `사진 확대·이동`, `영상 재생`, `영상 컨트롤`, `모달 닫기`.
- Keep platform differences in `사용 위치`, `조건·대상`, or `핵심 기준`.
- Use `선택` for Korean user action wording.
- Keep gesture names such as `pinch-to-zoom`, `double tap`, and `drag/pan` when they are the clearest labels.
- Include Figma node IDs only when they help confirm the source.
- Do not use class names, props, architecture names, or code-style state keys.
- Do not add a separate section for every state unless the component is too complex for one table.
- Do not write CSS values or implementation properties.
- Do not invent tokens.
- If the design does not define a value, write `시안 기준 추가 정의 필요`.

Add a short `기본 구조` bullet list before the table only when the component cannot be understood from the function table alone.

## 핵심 확인 체크리스트

Use a short checklist when it helps QA or handoff.

Recommended table:

| 체크 항목 | PC Web | Mobile App |
| --- | --- | --- |

Rules:

- Keep only core user-visible checks that are not already obvious from the function table.
- Do not include code, internal reset logic, or developer-owned cleanup.
- Use `필수`, `권장`, `해당 없음`, or `시안 확정 필요`.

## 변경이력

- Write the section title with the correct contiguous number, such as `## 6. 변경이력`.
- Keep only the latest row unless the user asks to preserve all history.
- Sort newest rows first when multiple rows are needed.
- Use `Claude, 김혜연` as Author for user-requested component document changes.

## Writing Rules

- Write in Korean unless the user asks otherwise.
- Use short sentences.
- Use familiar words before specialist terms.
- Remove repeated sections.
- Prefer one strong function table over many small tables.
- Preserve source meaning.
- Do not invent scope, screen behavior, or design values.
- Use `TBD` or `시안 기준 추가 정의 필요` only when needed.
- Keep file names concise lowercase kebab-case, such as `media-viewer-modal.md`.
