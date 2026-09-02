# Post-Draft Reviews

Use this reference after the initial feature-spec MD is complete. Consistency is part of document quality, but each review remains user-selectable because it can require additional sources and time.

## 1. Mandatory Review Gate

Always ask all three questions after completing the initial MD:

1. `예외 케이스 및 누락 정책의 추가 작성을 검토해드릴까요?`
2. `feature 폴더 내 다른 MD들과의 일관성을 검토해드릴까요?`
3. `Figma 화면과 기능명세 MD가 일치하는지 확인해드릴까요?`

The user may approve all, selected items, or none.

- If commit/push was requested, ask before committing or pushing and wait for answers to all three questions.
- If the user approves a review, perform it and present findings before changing source-unsupported content.
- If a required folder, document, Figma link, node, or access is unavailable, say what is missing and request only that source. Do not claim the review passed.
- After presenting findings, ask which proposed changes to reflect. Modify the current MD only after confirmation.
- Do not modify peer MD files or Figma unless the user separately authorizes those changes.

For the exception review, follow `coverage_exception_review.md`.

## 2. Feature-Folder Consistency Review

Review the current MD against the other relevant feature-spec Markdown files in the repository's feature documentation folder.

### Source Selection

- Locate the current document's feature folder or the repository's established `feature`, `features`, or feature-spec documentation area.
- Inventory every other `.md` file in that folder before selecting comparison evidence.
- Skip unrelated README, template, changelog, or generated files unless they explicitly define the folder's conventions.
- When the folder is reasonably bounded, inspect every peer feature-spec MD directly.
- When the folder is large, mechanically extract metadata, headings, table columns, IDs, and recurring product terms from all peer MDs, then deeply inspect the same service/domain and convention-defining documents. State both the inventory scope and deep-review scope.

### Comparison Points

Check:

- heading order, metadata keys, table columns, links, image placement, and change-history style;
- file naming, document IDs, version format, requirement ID pattern, and IA depth usage;
- Korean terminology, role names, status names, data-object names, button/action labels, and noun-style writing tone;
- requirement granularity and how behavior is divided among 기능·프로세스·화면·보안·데이터 columns;
- shared permission boundaries, validation rules, save timing, deletion/recovery behavior, notification rules, error handling, and audit conventions;
- overlap, contradiction, or accidental duplication with an existing feature requirement.

Do not copy a neighboring rule solely because it is common. Prefer current product evidence and flag outdated or conflicting conventions for a user decision.

### Findings

Use a compact table:

| 비교 항목 | 현재 MD | 비교 문서·근거 | 결과 | 권장 조치 |
| --- | --- | --- | --- | --- |

Use these result labels:

- `일치`
- `불일치`
- `충돌 가능`
- `판단 필요`

Report only meaningful inconsistencies or a concise `중요 불일치 없음` conclusion. Cite the peer filename and relevant heading or requirement ID. Recommend changes to the current MD first; do not silently normalize unrelated documents.

## 3. Figma-to-MD Alignment Review

Compare the completed MD with the in-scope Figma source in both directions.

### Required Source

- Use the Figma file/link and exact in-scope pages, sections, or nodes used to create the MD.
- If no Figma source is available, ask the user to provide it or decline this review. Do not infer visual agreement from text alone.
- State any pages, nodes, hidden variants, or prototype interactions that could not be inspected.

### Figma to MD

Verify that every in-scope screen, meaningful variant, overlay, tab, visible control, interaction, destination, and explicitly designed state maps to a requirement ID or documented exclusion.

### MD to Figma

Verify that each screen or UI-specific claim in the MD has support in Figma. Planning-only policy, security, data, and nonvisual process rules may have no visual counterpart; label them `비시각 기획 규칙` rather than mismatches.

### Comparison Points

Check:

- screen, tab, modal, drawer, popup, and overlay coverage;
- labels, field names, options, ordering, required/optional indicators, and default values;
- visible/hidden, enabled/disabled, selected/unselected, and role-specific variants;
- loading, empty, error, success, partial-success, permission-limited, and offline states;
- validation messages, confirmation steps, cancel/close behavior, navigation destinations, and follow-up screens;
- fixed and scrolling regions, especially frames whose names contain `scroll`;
- bulk-action behavior, duplicate execution prevention, and progress feedback when represented in Figma.

### Findings

Use a compact table:

| Figma 화면·노드 | 요구사항 ID | 비교 결과 | 차이 | 권장 조치 |
| --- | --- | --- | --- | --- |

Use these result labels:

- `일치`
- `Figma에만 있음`
- `MD에만 있음`
- `내용 불일치`
- `확인 필요`
- `비시각 기획 규칙`

Report both omissions and contradictions. Reference exact frame/node names and requirement IDs when available. Do not decide that Figma or MD is the source of truth when the sources conflict; recommend a resolution and request the user's decision.

## 4. Apply Approved Changes

After the user selects findings to reflect:

- update only the current feature MD unless broader edits were explicitly requested;
- preserve the standard MD structure and all previous change-history rows;
- add the review-driven changes to the current change-history entry;
- rerun source coverage and any selected review affected by the edit;
- proceed with commit/push only after the selected reviews and approved corrections are complete.
