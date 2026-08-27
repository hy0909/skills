# UX Flow JSON Schema

The plugin server accepts this JSON at `POST http://localhost:3765/ux-flow`. One JSON = one 페이지+기능 flow.

## Top level

| field | type | required | description |
|---|---|---|---|
| `page` | string | ✅ | 페이지명 (예: `QR 주문`). 파일명과 섹션 제목에 사용 |
| `feature` | string | ✅ | 기능명 (예: `주문 생성`) |
| `title` | string | | 플로우 제목. 없으면 `page > feature` |
| `figmaLinks` | array | | 참고한 피그마 링크. `{ "label": string, "url": string }` — 섹션 **우측 상단**에 라벨 텍스트만 표기하고 라벨에 하이퍼링크를 건다(URL 문자열은 캔버스에 노출하지 않음). label은 짧게 |
| `nodes` | array | ✅ | 아래 Node 참조 |
| `edges` | array | ✅ | 아래 Edge 참조 |

## Node

| field | type | required | description |
|---|---|---|---|
| `id` | string | ✅ | 고유 id (영문/숫자, 예: `n1`, `check_stock`) |
| `type` | string | ✅ | `start` `end` `screen` `action` `decision` `api` `note` |
| `label` | string | ✅ | 노드 제목, ≤ 16자. decision은 짧은 질문형 (`재고 있음?`) |
| `details` | string[] | | 짧은 문장/단어 3~6개, 각 ≤ 22자. 노드 아래 `·` 리스트로 표기. api는 첫 줄에 `METHOD /path` |
| `role` | string | | 권한 (예: `관리자`, `게스트`) — 노드 안 뱃지 `👤` |
| `state` | string | | 상태 조건 (예: `로그인됨`, `데이터 없음`) |
| `owner` | string | | 구현 주체: `FE` `BE` `FE·BE` — 노드 안 `[FE]` 뱃지 |
| `case` | string | | `happy`(기본, 회색) `error`(빨강) `exception`(주황) |
| `col` | number | ✅ | 열 (0부터, 시간 순서 왼→오른쪽) |
| `row` | number | ✅ | 행 (0 = 해피 패스, 1+ = 분기/에러/예외/메모) |

노드 모양: start/end=타원(초록/회색), screen=사각형, action=둥근사각형, decision=마름모(노랑), api=평행사변형(파랑), note=스티커(노랑, label+details가 스티커 본문).

플러그인은 매 플로우 상단에 이 도형 규칙 **범례**를 자동으로 그린다(시작·종료/화면/액션/분기/API/에러·예외 색). 모든 도형은 1px 테두리, 텍스트는 Inter 폰트로 렌더링된다 — JSON에서 별도로 지정할 필요 없음.

## Edge

| field | type | required | description |
|---|---|---|---|
| `from` | string | ✅ | 출발 노드 id |
| `to` | string | ✅ | 도착 노드 id |
| `label` | string | decision 분기는 ✅ | `YES`/`NO`/`401`/`중복` 등. YES·성공=초록 화살표, NO·실패=빨강 |

## Complete example

```json
{
  "page": "QR 주문",
  "feature": "주문 생성",
  "title": "QR 주문 생성 플로우",
  "figmaLinks": [
    { "label": "주문 폼 디자인", "url": "https://www.figma.com/design/abc?node-id=1-2" },
    { "label": "에러 상태", "url": "https://www.figma.com/design/abc?node-id=3-4" }
  ],
  "nodes": [
    { "id": "start", "type": "start", "label": "QR 스캔", "col": 0, "row": 0 },
    { "id": "auth", "type": "decision", "label": "로그인 상태?", "role": "게스트 허용", "col": 1, "row": 0 },
    { "id": "form", "type": "screen", "label": "주문 폼", "owner": "FE",
      "details": ["필수: 메뉴, 수량", "옵션: 요청사항", "수량 최대 99"], "col": 2, "row": 0 },
    { "id": "submit", "type": "action", "label": "주문하기 탭", "owner": "FE",
      "details": ["유효성 검사", "중복 탭 방지"], "col": 3, "row": 0 },
    { "id": "create", "type": "api", "label": "주문 생성 API", "owner": "BE",
      "details": ["POST /orders", "201: 주문번호 반환", "409: 품절"], "col": 4, "row": 0 },
    { "id": "done", "type": "end", "label": "주문 완료 화면", "col": 5, "row": 0 },
    { "id": "guest_form", "type": "screen", "label": "게스트 정보 입력", "case": "exception",
      "state": "비로그인", "details": ["휴대폰 번호 필수"], "col": 1, "row": 1 },
    { "id": "invalid", "type": "action", "label": "인라인 오류 표시", "case": "error", "owner": "FE",
      "details": ["필드별 메시지", "첫 오류로 스크롤"], "col": 3, "row": 1 },
    { "id": "soldout", "type": "action", "label": "품절 토스트", "case": "error", "owner": "FE",
      "details": ["409 응답 시", "수량 초기화"], "col": 4, "row": 1 },
    { "id": "policy", "type": "note", "label": "정책",
      "details": ["게스트 주문은 30분 내 미결제 시 자동 취소"], "col": 1, "row": 2 }
  ],
  "edges": [
    { "from": "start", "to": "auth" },
    { "from": "auth", "to": "form", "label": "YES" },
    { "from": "auth", "to": "guest_form", "label": "NO" },
    { "from": "guest_form", "to": "form" },
    { "from": "form", "to": "submit" },
    { "from": "submit", "to": "create", "label": "YES" },
    { "from": "submit", "to": "invalid", "label": "NO" },
    { "from": "invalid", "to": "form" },
    { "from": "create", "to": "done", "label": "201" },
    { "from": "create", "to": "soldout", "label": "409" },
    { "from": "soldout", "to": "form" }
  ]
}
```

주의: `submit`처럼 action에서 분기해도 되지만, 조건이 복잡하면 별도 `decision` 노드로 빼는 편이 개발자가 읽기 쉽다. edge label이 있는 분기가 2개 이상이면 decision 노드 사용을 우선 고려할 것.
