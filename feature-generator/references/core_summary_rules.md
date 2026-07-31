# Core Planning Rules

The `핵심 기획 규칙` section is a short planning map, not a summary document.

Use one table:

| 구분 | 핵심 기획 규칙 | 적용 범위 | 요구사항 연결 |
| --- | --- | --- | --- |

Write max 5 rows by default.

Include only:

- rules affecting multiple requirement rows
- required/optional distinctions
- permission rules that change visible actions
- validation/save timing rules that developers can easily miss
- wording/source-of-truth rules

Do not include:

- repeated row summaries
- FE/BE implementation details
- API/DB/enum/status-machine definitions unless the user explicitly says this feature MD owns them
- separate 권한/알림/상태/백엔드 요약 tables

Fallback row:

| 구분 | 핵심 기획 규칙 | 적용 범위 | 요구사항 연결 |
| --- | --- | --- | --- |
| 공통 | 본 문서는 요구사항 테이블 기준으로 구현한다. 별도 핵심 기획 규칙 없음 | 전체 | 2. 요구사항 테이블 |
