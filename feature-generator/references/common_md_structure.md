# Common MD Structure

Every feature specification MD must include the following sections in this order.

| 순서 | 항목 | 필수 여부 | 작성 내용 | 필드/구성 | 예시 | 위치 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 헤더 | 필수 | 파일명 + 한 줄 설명 | 문서명, 한 줄 설명 | `# 프로젝트 설정`<br>`프로젝트 기본정보, 구성원, 권한 설정 요구사항을 정리한 기능명세서입니다.` | 최상단 |
| 2 | 메타 블록 | 필수 | 문서 식별 및 관리 정보 | `id`, `version`, `status`, `owner_team`, `effective_date` | `id: FEAT-PROJECT-SETTINGS-001`<br>`version: 1.0.0`<br>`status: draft` | 상단 |
| 3 | 목적·범위 | 필수 | 이 문서가 왜 존재하는지, 어디까지 다루는지 | 목적, 포함 범위, 제외 범위 | `프로젝트 설정 화면의 요구사항을 정의한다.` | 상단 |
| 4 | 핵심 기획 규칙 | 필수 | 개발자가 요구사항 테이블을 오해하지 않도록 필요한 최상위 기획 규칙만 표로 정리 | 구분, 핵심 기획 규칙, 적용 범위, 요구사항 연결 | `3단계 알림 수신은 필수이며 OFF 불가` | 상단 |
| 5 | 요구사항 테이블 | 필수 | 구현 기준이 되는 기능명세 테이블 | IA, 요구사항 ID, 기능/프로세스/화면/보안/데이터 요구사항 | `REQ-...` 행 단위 요구사항 | 중간 |
| 6 | 연관 링크 | 선택 | 관련 문서, 정책, 기능명세서, 외부 링크 | 관련 PRD, 관련 정책, 관련 기능명세서, 외부 링크 | `관련 정책: ../policy/...` | 변경 이력 바로 위 |
| 7 | 변경 이력 | 필수 | 최초 작성일, 수정일, 버전별 변경 내용, 작성자 | 버전, 일자, 변경 내용, 작성자 | `v1.0.0: 최초 작성` | 최하단 |

## Required Section Template

````md
# {{문서명}}

{{한 줄 설명}}

```yaml
id: {{문서_ID}}
version: 1.0.0
status: draft
owner_team: AI Research team
effective_date: {{YYYY-MM-DD}}
```

<br>
<br>
<br>

## 1. 목적·범위

- 목적:
- 포함 범위:
- 제외 범위:

<br>
<br>
<br>

## 2. 핵심 기획 규칙

| 구분 | 핵심 기획 규칙 | 적용 범위 | 요구사항 연결 |
| --- | --- | --- | --- |

<br>
<br>
<br>

## 3. 요구사항 테이블

| 1depth | 2depth | 3depth | 요구사항 ID | 요구사항명 | 요청목적 | 기능 요구사항 | 프로세스 요구사항 | 화면 요구사항 | 보안 요구사항 | 데이터 요구사항 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

<br>
<br>
<br>

## 4. 연관 링크

| 구분 | 링크 |
| --- | --- |
| 관련 PRD | TBD |
| 관련 정책 | TBD |
| 관련 기능명세서 | TBD |
| 외부 링크 | TBD |

<br>
<br>
<br>

## 5. 변경 이력

| 버전 | 일자 | 변경 내용 | 작성자 |
| --- | --- | --- | --- |
| 1.0.0 | {{YYYY-MM-DD}} | 최초 작성 | Codex, 김혜연 |
````

## Change History Author

- When writing a feature specification for the current user, always use `Codex, 김혜연` in the `작성자` column for the initial creation row and every revision row.

## File Naming

- Use the same concise English kebab-case topic for MD and XLSX: `<topic>.md`, `<topic>.xlsx`.
- Omit `feature`, `기능명세서`, dates, versions, status labels, and redundant directory context.
- Match document-specific assets to the same topic: `assets/<topic>/`.

## Status Values

| 상태 | 의미 | 사용 기준 |
| --- | --- | --- |
| `draft` | 초안 | 작성 중이거나 검토 전인 문서 |
| `active` | 활성 | 확정되어 현재 기준으로 사용하는 문서 |
| `deprecated` | 폐기 예정/비권장 | 히스토리용으로 남기지만 신규 작업 기준으로 사용하지 않는 문서 |

## Concise Planning Rule

- 기능명세서는 요구사항 테이블 중심 문서입니다.
- `## 2. 핵심 기획 규칙`은 개발에 필수인 최상위 기획 규칙만 담습니다.
- 본문 앞에 긴 설명, 중복 요약, 직군별 구현 문서를 추가하지 않습니다.
- BE/FE의 확정 상태값, API, DB, 컴포넌트 구조는 각 직군 문서에서 관리합니다. 기능명세서에는 사용자가 경험하는 기획 규칙과 요구사항만 작성합니다.

## No Speculative Development Design

- 기능명세서는 요구사항을 정리하는 문서이며, 개발 구조를 상상해서 미리 설계하지 않습니다.
- 원문에 없는 enum, error code, API 구조, DB schema, state machine, class name, component name, backend architecture를 임의로 작성하지 않습니다.
- 원문에 없는 개발 코드, pseudo-code, API endpoint, DB table/field, analytics event, tracking event, 내부 상태머신, 컴포넌트명도 작성하지 않습니다.
- 사용자가 명시한 개발 정보가 있는 경우에도 기능명세서에는 기획상 필요한 의미만 간결히 정리하고, 세부 구현 기준은 해당 직군 문서로 분리합니다.
