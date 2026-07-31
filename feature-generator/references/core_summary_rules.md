# Core Planning Rules

Use these rules whenever generating the `## 2. 핵심 기획 규칙` section of a 기능명세서 MD.

## Goal

The feature MD must be easy for humans and LLMs to scan. The requirement table is the main implementation source. The core section exists only to give developers a quick planning map before reading the table.

## Required Format

Use one concise table by default:

| 구분 | 핵심 기획 규칙 | 적용 범위 | 요구사항 연결 |
| --- | --- | --- | --- |
| {{권한/흐름/화면/알림/데이터 등}} | {{개발자가 구조를 잡을 때 필요한 기획 규칙 1개}} | {{적용 화면·단계·사용자 범위}} | {{REQ ID 또는 IA 경로}} |

Keep the table short. Prefer 3–8 rows. If there is only one important rule, write one row. If there are no cross-cutting planning rules, write:

| 구분 | 핵심 기획 규칙 | 적용 범위 | 요구사항 연결 |
| --- | --- | --- | --- |
| 공통 | 본 문서는 요구사항 테이블 기준으로 구현한다. 별도 핵심 기획 규칙 없음 | 전체 | 3. 요구사항 테이블 |

## What Belongs Here

Include planning rules that prevent developers from misreading the requirement table:

- screen-level branching that affects several rows
- permission or role rule that changes visible actions
- required/optional distinction that affects flow design
- one source of truth for wording, validation, or save timing
- exception rule that applies across multiple requirements

## What Does Not Belong Here

Do not add long summaries or role-owned implementation details:

- BE-owned API, DB, enum, event, state machine, error code, or persistence design
- FE-owned component architecture, props, store shape, route design, or event handler names
- QA checklist
- repeated copies of every row in the requirements table
- separate mandatory tables such as `권한 요약`, `알림·위험알림 요약`, `단계/상태 요약`, `백엔드 핵심 로직 요약`

If the source includes BE/FE-specific information and the user asks to keep this document planning-focused, translate it only into the planning implication needed to understand the feature. Otherwise leave it to the relevant BE/FE document.

## Writing Rules

- Use short, direct Korean.
- One row = one planning rule.
- Prefer nouns that match the product UI and planning terminology.
- Do not invent missing rules. Use `원문 기준 추가 정의 필요` only when the planning rule is essential but missing.
- Avoid paragraphs above or below the table unless a short note is needed to prevent misunderstanding.
