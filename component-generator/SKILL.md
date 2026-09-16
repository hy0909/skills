---
name: component-generator
description: Create concise Korean design-system component Markdown documents from Figma mockups, screenshots, notes, or existing MD files for planner/designer handoff. Use when the user wants a reader-friendly component spec organized by service usage, platform differences, common visual rules, and function-level behavior, with no code, API, CSS, props, FE/BE architecture, or confusing duplicated tables.
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
- When a control or visual effect appears only in some areas, clearly separate `있음` and `없음`.
- Include state changes such as `replay` when the visible label or button changes.
- Optimize for reader understanding before optimizing for table count.
- Do not repeat the same rule in multiple sections unless it prevents misunderstanding.
- Do not split one idea into many tables unless platform differences improve readability.
- Split PC Web and Mobile App into separate tables when their usage, gestures, or required checks differ.
- Split behavior, visual display rules, and QA checks when combining them makes rows long or hard to scan.
- Remove tables or sections that do not add a decision or implementation handoff value.
- Add a `Figma 화면` section only when the user asks for synced previews, screenshots, or visual references in the MD.
- Keep Figma previews to one or two core screens that directly support the described component rules.
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
- Wide tables with many long text cells that make the document harder to scan.
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
7. Optional `## n. Figma 화면` when visual previews are requested
8. `## n. 연관 링크`
9. `## n. 변경이력`

Use `---` between top-level sections.

## Header & Metadata

Start every file with the component name as the H1, then a metadata block:

```md
# {{Component Name}}

> **Figma:** [PC Web → {{시안명}}]({{PC Figma URL}})<br>
> **Figma:** [Mobile App → {{시안명}}]({{Mobile Figma URL}})<br>
> **Status:** Draft<br>
> **Last updated:** {{YYYY-MM-DD}}<br>
> **Owner:** AI Research Team
```

- `Status`: `Draft`, `Review`, `Stable`, `Deprecated` 중 하나.
- `Last updated`: current date or user-provided date.
- `Figma`: use provided links only. Do not invent links.
- `Owner`: always write `AI Research Team` unless the user explicitly provides another owner.
- Use a blockquote metadata block with clickable Markdown links.
- Add `<br>` at the end of every metadata line except the last line so GitHub renders each item on a separate line.
- Do not use fenced `yaml` metadata blocks because Figma URLs are not clickable inside code blocks.
- Do not combine two metadata items into one line.
- Use separate PC Web and Mobile App Figma lines when both platform links exist.

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

Write the clearest mix of short bullets and function-level tables that helps developers understand the component behavior without code.

Use a separate `공통 표시 기준` table when visual rules are shared across PC Web and Mobile App:

| 항목 | 기준 |
| --- | --- |

Use compact function tables for platform-specific behavior:

| 기능 | 대상 | 동작 | 기준 |
| --- | --- | --- | --- |

Rules:

- One row should describe one user-facing function.
- Merge visual structure, display rules, interaction, and content labels only when it helps understanding.
- Include only rows needed to build or review the component.
- When both PC Web and Mobile App are in scope, prefer `### PC Web` and `### Mobile App` tables inside `## 3. 기능 단위 명세`.
- Do not force platform columns into one table when the reader must compare many PC/Mobile differences.
- Prefer 3-4 table columns for function flow. Avoid 5-6 columns unless each cell stays short.
- Use function names such as `사진 확대 열기`, `사진 확대·이동`, `영상 재생`, `영상 컨트롤`, `모달 닫기`.
- Keep platform differences in `사용 위치`, `조건·대상`, or `핵심 기준`.
- Use `선택` for Korean user action wording.
- Keep gesture names such as `pinch-to-zoom`, `double tap`, and `drag/pan` when they are the clearest labels.
- Include Figma node IDs only when they help confirm the source.
- Do not use class names, props, architecture names, or code-style state keys.
- Do not add a separate section for every state unless the component is too complex for one table.
- Do not write CSS properties or implementation properties.
- Design values such as direction, area size, color, and opacity are allowed when needed for visual handoff.
- If the user asks for button presence, visual effects, or state changes, state where it appears and where it does not appear.
- For gradients, write the area, direction, height, color, and opacity when those values are provided.
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
- Split checklist into `### PC Web` and `### Mobile App` tables when `해당 없음` rows increase reading load.
- Do not include code, internal reset logic, or developer-owned cleanup.
- Use `필수`, `권장`, `해당 없음`, or `시안 확정 필요`.

## Figma 화면

Add this section only when the user asks to show or sync Figma screens inside the document.

Recommended table:

| 구분 | 화면 | Figma 원본 |
| --- | --- | --- |

Rules:

- Include only one or two representative screens.
- Choose screens that explain the component usage or a recently changed rule.
- Use local repo image paths for images, not expiring Figma image URLs.
- Keep the original Figma link next to each image.
- Do not paste sync commands, API notes, or development setup details into the component MD.
- If image files cannot be generated because the Figma token is unavailable, add the image references only when the user accepts that the files will appear after sync.
- Do not invent screenshots or describe screens that were not provided.

## 변경이력

- Write the section title with the correct contiguous number, such as `## 6. 변경이력`.
- Keep all change history rows.
- Add the newest change as a new row at the top.
- Sort newest rows first.
- Do not delete old rows unless the user explicitly asks to remove them.
- Use `Claude, hy0909` as Author for user-requested component document changes.

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

## 문체 규칙 (공통)

이 스킬이 만드는 모든 한국어 산문은 `human-writing` 스킬을 따른다 (같은 저장소의 `human-writing/SKILL.md`. Claude Code는 `~/.claude/skills/human-writing`, Codex는 `~/.codex/skills/human-writing`). 핵심만 요약:

- 한 문장에 생각 하나, 60자 안팎. 대조·원인은 `~지만`, `~기 때문에`로 한 문장에 잇고, 짧은 문장을 문두 `하지만/그래서`로 툭툭 끊지 않는다. 핵심 먼저.
- 개발·디자인을 모르는 사람도 읽게 일상 동사(쓰다·적어 두다·손보다·나누다)로 쓴다. 한자어 명사구는 `언제 쓰는지, 어디까지 바꿀 수 있는지`처럼 푼다. 용어는 우리말이 있으면 바꾸고(베리언트→형태별 구분), 팀이 매일 쓰는 말은 그대로 둔다. 서술 문장 한가운데 괄호 설명을 끼우지 않는다. 억지 동의어·도치·조각 문장 금지. 문단 첫 문장은 결론.
- 번역투 금지: `~를 통해`, `~에 있어서`, `~에 의해`, `~되어지다`, `위치해 있다`, `~함에도 불구하고`, `~를 가지고 있다`.
- 상투·기계적 표현 금지: `결론적으로`, `시사하는 바가 크다`, `~하는 것이 중요합니다`, `~할 필요가 있다`, `단순한 ~가 아니라`, `~뿐만 아니라 ~도`, `첫째·둘째·셋째` 나열, 형용사·명사 3개 나열, 문두 `또한/따라서/아울러` 연속, 대시(—), `혁신적인·원활한·강력한·다양한·효과적으로`, `파고들어 봅시다`, `잠재력을 발휘하다`.
- `~습니다`가 세 문장 연속이면 하나는 바꾼다. `-적/-성/-화`는 절반으로.
- `많은·다양한·최근·크게 개선`은 숫자·사례로 바꾼다. 정보가 없으면 지어내지 말고 `TBD` 또는 `[확인 필요]`.
- 비교·대조 가능한 항목은 표로 쓴다. 표로 할지 줄글로 할지 판단이 서지 않으면 사용자에게 묻는다(Claude Code에서는 AskUserQuestion 도구).
- 다 쓴 뒤 한 번 더 읽고 "여전히 AI 같아 보이는 곳"을 한 군데 찾아 고친다.
- 이 스킬의 예외: 표 셀·`목적`·`범위`·기능 단위 명세 행은 기존 명사형 종결 규칙(`공통 미디어 뷰어 컴포넌트`)을 유지한다. 어미 변주·도치·문장 길이 변주는 설명 문단에만 적용. 반론·`[내 경험]` 같은 관점 규칙은 명세 문서에 넣지 않는다. 미정 표기는 기존 `TBD` / `시안 기준 추가 정의 필요`를 쓴다.
