---
name: component-generator
description: Create concise Korean design-system component Markdown documents from Figma mockups, screenshots, notes, or existing MD files for planner/designer handoff. Use when the user wants a component spec focused on purpose/scope, service usage locations, visual structure, display rules, states, interactions, content, accessibility, and a short checklist, with no code, API, CSS, props, FE/BE architecture, or duplicated implementation detail.
---

# Component Generator

Create concise Korean component design documents.

This skill is for 기획자·디자이너가 개발자에게 전달하는 디자인 컴포넌트 기준 문서. The document should explain what the component is, where it appears in the service, how it looks, and how it behaves. Development design belongs to developers.

## Output Principle

- Keep the MD short.
- Use easy, clear Korean.
- Prefer short noun-style endings such as `공통 미디어 뷰어 컴포넌트`, not long `~한다` prose.
- Write only planning/design information needed for implementation handoff.
- Make `서비스 내 적용 위치` and `컴포넌트 자체 구조` the strongest parts of the document.
- Describe user-visible behavior and interaction, not internal implementation.
- Do not repeat the same rule in multiple sections unless it prevents misunderstanding.
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
- Long abstract wording that increases reading load.

Technical terms are allowed only when they are user-facing gestures or UI labels in the design, such as `pinch-to-zoom`, `double tap`, `progress bar`, or `Close button`.

## MD Structure

Use this order. Keep numbering contiguous.

1. Header
2. Metadata block
3. `## 1. 목적·범위`
4. `## 2. 서비스 내 적용 위치`
5. `## 3. 컴포넌트 구조`
6. `## 4. 표시 규칙`
7. `## 5. 상태·인터랙션`
8. `## 6. 콘텐츠·접근성`
9. `## 7. 핵심 확인 체크리스트`
10. `## 8. 연관 링크`
11. `## 9. 변경이력`

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

- Include only real service locations from the source.
- Mark uncertain usage as `시안 확정 필요`.
- If a screen does not use this component, write the reason briefly.
- Prefer service meaning over internal routing or rendering details.

## 컴포넌트 구조

Describe the visible parts of the component.

Recommended table:

| 영역 | 구성 요소 | 설명 |
| --- | --- | --- |

Rules:

- Focus on what the user sees.
- Include Figma node IDs only when they help confirm the source.
- Do not use class names, props, architecture names, or code-style state keys.
- Keep Figma frame names readable. If a technical name is needed for handoff, keep it short and human-readable.

## 표시 규칙

Write visual and content display rules.

Good subjects:

- Photo/video display ratio.
- Modal size behavior shown in the design.
- Close button location and touch/click area.
- Player control visibility.
- Media type by risk level or service context.
- Whether a Figma control is only a reference and may use a similar player library.

Rules:

- Use tables for repeated rules.
- Do not write CSS values or implementation properties.
- Do not invent tokens.
- If the design does not define a value, write `시안 기준 추가 정의 필요`.

## 상태·인터랙션

Write only user actions and visible results.

Recommended table:

| 상황 | 사용자 액션 | 화면 반응 |
| --- | --- | --- |

Rules:

- Focus on click/selection, close, zoom, pan, play/pause, progress movement, and dim-area close.
- Use `선택` for Korean user action wording.
- Keep gesture names such as `pinch-to-zoom`, `double tap`, and `drag/pan` when they are the clearest labels.
- Do not mention internal state machines or lifecycle behavior.

## 콘텐츠·접근성

Include only content labels and accessibility rules that matter for handoff.

Recommended table:

| 항목 | 기준 |
| --- | --- |

Rules:

- Include icon labels, button labels, and focus/keyboard needs when relevant.
- Do not create a `Figma 최신 텍스트 샘플` section.
- Do not duplicate unrelated page text.
- Keep accessibility wording practical and short.

## 핵심 확인 체크리스트

Use a short checklist when it helps QA or handoff.

Recommended table:

| 체크 항목 | PC Web | Mobile App |
| --- | --- | --- |

Rules:

- Keep only core user-visible checks.
- Do not include code, internal reset logic, or developer-owned cleanup.
- Use `필수`, `권장`, `해당 없음`, or `시안 확정 필요`.

## 변경이력

- Write the section title as `## 9. 변경이력` or the correct contiguous number.
- Keep only the latest row unless the user asks to preserve all history.
- Sort newest rows first when multiple rows are needed.
- Use `Claude, 김혜연` as Author for user-requested component document changes.

## Writing Rules

- Write in Korean unless the user asks otherwise.
- Use short sentences.
- Use familiar words before specialist terms.
- Remove repeated sections.
- Preserve source meaning.
- Do not invent scope, screen behavior, or design values.
- Use `TBD` or `시안 기준 추가 정의 필요` only when needed.
- Keep file names concise lowercase kebab-case, such as `media-viewer-modal.md`.
