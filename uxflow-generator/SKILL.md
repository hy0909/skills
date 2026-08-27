---
name: uxflow-generator
description: Create developer-friendly UX flow diagrams on FigJam so FE/BE developers can check business logic and branch handling at a glance. Use whenever the user asks for a UX flow, 유저 플로우, 화면 흐름도, 플로우차트, FigJam/피그잼 flow, 분기 정리, or wants to hand developers a page/feature-level flow with happy/error/exception paths, 권한(role), 상태(state), and yes/no branch arrows. Takes 기획 내용 (text or spec md) plus Figma design links, produces flow JSON, and sends it to the local plugin server (localhost:3765) so the UX 플로우 생성기 FigJam plugin draws it.
---

# UX Flow Generator

Turn planning text and Figma designs into a FigJam flow diagram that FE/BE developers use to implement business logic and branch handling. The reader is a developer asking "이 화면에서 무슨 일이 일어나고, 어떤 조건에서 어디로 가는가?" — every rule below exists to answer that question at a glance.

## Pipeline

1. **Collect input.** Planning text, spec markdown, or a conversation description — plus Figma design links when available. md는 붙여넣은 텍스트·로컬 파일·GitHub 링크 어느 형태든 받는다. GitHub 링크(블랍/트리/브랜치 포함)면 `gh api "repos/{owner}/{repo}/contents/{path}?ref={branch}" --jq .content | base64 -d`로 원문을 받아서 쓴다(프라이빗 레포도 gh 인증으로 동작). **Spec md가 있으면 md가 최우선 기준이다**: 요구사항 ID(REQ-*)·필수/선택·에러 케이스를 md에서 그대로 가져오고, md의 GitHub URL을 `docLinks`에 넣는다(플러그인이 우측 상단에 📄 링크로 그린다). 사용자가 말로 준 정책(한도·개수 제한 등)은 md에 없어도 반영하되 note로 "정책 확정 필요" 표시 가능.
2. **Read the design.** For each Figma link, use the Figma MCP (`get_metadata` first, then `get_screenshot` / `get_design_context` for the needed nodes) to identify screens, buttons, empty/error states, and permission-gated UI. Every link you consulted goes into `figmaLinks` — developers jump from the flow to the design through these.
3. **Split by page/feature — page names come from the IA.** One flow = one 페이지 + one 기능 (e.g. `QR 발주 내역 > 발주 승인`). `page` must match the product IA so developers can map flows to routes/menus. IA 출처 우선순위: ① 사용자가 준 IA 링크/문서 ② spec md의 1depth 컬럼 ③ `references/ia.md`(현재 프로젝트 캐시 — 다른 프로젝트면 무시). 참조한 IA 링크는 `figmaLinks`에 넣는다. If a flow needs more than ~9 columns or ~18 nodes, split it into two features rather than shrinking text.
4. **Author the flow JSON.** Schema and a complete example: `references/flow-schema.md`. Writing rules below.
5. **Validate.** `python3 scripts/validate_flow.py <flow.json>` — fix every ERROR, review every WARN.
6. **Send.** `python3 scripts/validate_flow.py <flow.json> --send` (POSTs to `http://localhost:3765/ux-flow`). If the server is down, run `./start-server.sh` in the plugin folder — the folder is a clone of [hy0909/uxflow-figjam-plugin](https://github.com/hy0909/uxflow-figjam-plugin) (없으면 클론해서 세팅, 세팅법은 그 레포 README). 그 후 재전송.
7. **Tell the user how to draw it:** open a **FigJam** file → run the `UX 플로우 생성기` plugin → `UX Flow` tab → click the flow. Mention the flow name you saved.

## Writing rules — developer's point of view

**Form fields are parallel, not a chain.** 한 화면(폼/모달)에서 입력하는 필드들은 시간 순서가 없다 — 수량 → 수출국 → 제품처럼 순차 체인으로 그리지 말 것. 같은 col에 세로로 나란히 배치해 화면 노드에서 병렬로 분기시키고(edge label `병렬`), 모두 "버튼 활성 조건" decision(예: `필수 모두 입력?`)으로 모은다. **필수 입력 노드는 라벨 끝에 `*`, 선택 입력은 라벨에 `(선택)`을 붙인다** — 플러그인이 타이틀 영역에서 `*`를 **`(필수항목)`**(빨간색), `(선택)`을 **`(선택항목)`**으로 변환해 명확히 표기하고, 범례에도 `(필수항목) 필수 입력 · (선택항목) 선택 입력`을 자동 표기한다. JSON 라벨은 짧게 `*`/`(선택)`으로 쓰면 된다(16자 제한은 변환 전 기준). 디자인이 실제로 입력 순서를 강제할 때만 체인을 쓴다.

**Spec에 정의된 에러 케이스는 하나도 빠짐없이 red로.** 유효성 에러가 여러 종류면(예: 단위 오류/개수 초과/총량 초과) 각각 별도 `error` 노드로 쪼개고 decision에서 조건별 edge label로 분기시킨다 — 뭉뚱그린 "오류 표시" 하나로 합치면 개발자가 케이스를 놓친다.

**모든 엣지는 인접 셀만 잇는다 — 선 겹침의 유일한 예방법.** FigJam 커넥터는 경유점 제어가 불가능해서, 2칸 이상 떨어진 노드를 잇는 엣지는 중간 노드를 관통하고 라벨이 다른 라벨·노드와 겹친다. 규칙: ① 엣지는 가로/세로/대각 1칸 이내로만 ② 유효성 검증이 여러 개면 decision 하나에서 부챗살로 뿌리지 말고 **decision 체인**(마름모를 col로 나란히, 각 오류는 자기 마름모 바로 아래 row 1)으로 편다 — 코드의 순차 가드와도 일치 ③ 긴 루프백(에러→입력, 취소→목록) 엣지는 금지하고 해당 노드 details에 `수정 시 즉시 재검증`, `[취소] → 모달 닫고 목록 유지`처럼 결과를 명시하거나, [아니요]류 복귀는 인접한 `end`(exception) 노드로 종결한다 ④ 취소·닫기로 흐름이 끝나면 그 노드를 `end` 타입으로 — 뒤로 이어지는 선이 생기면 안 된다.

**진입·버튼은 `[ ]`로 정확히 표기.** 시작 노드 라벨은 `GNB - [QR 발주서]`처럼 실제 페이지명/버튼명을 대괄호로 감싸고, details에 정확한 경로(`경로: GNB > QR 발주 내역`)를 쓴다. 본문 노드에서도 실제 버튼은 `[발주]`, `칩 [x]`처럼 대괄호 표기.

**Happy path reads left to right on one line.** Put the success path on `row: 0`, ordered by time (`col` 0, 1, 2, …). Branches (error/exception) drop to `row: 1+` below the decision that spawns them. A developer should trace the main scenario without ever scanning vertically.

**Every branch is an explicit decision.** Anywhere the implementation needs an `if` — validation, API response, permission, empty data — add a `decision` node (a short question, e.g. `재고 있음?`) with **all outgoing edges labeled** (`YES`/`NO` or the concrete condition like `401`, `중복`). YES/성공 continues right on the happy row; NO/실패 goes down. Unlabeled decision edges are the #1 thing that makes developers guess — the validator rejects them. Rule of thumb: condition checks the code evaluates (유효성, 응답 코드, 권한, 데이터 유무) get a `decision` node; a user's own choice (취소/닫기 buttons) may branch straight off a `screen`/`action` node with a labeled edge.

**Failure paths loop back to where the user fixes them.** An error/exception node that lets the user retry should connect back to the input step it corrects (`인라인 오류 → 주문 폼`). That loop edge is exactly the retry logic the developer must implement — don't omit it, and don't route it anywhere the user can't act.

**Separate what FE and BE each implement.**
- `api` nodes are BE touchpoints: details start with `METHOD /path` (e.g. `POST /orders`), then key request fields and response codes the flow branches on.
- `owner: "FE" | "BE" | "FE·BE"` on nodes where ownership isn't obvious from the type.
- FE-side handling (토스트, 리다이렉트, 버튼 비활성) are `action`/`screen` nodes — every error/exception path must end at a node stating what the user actually sees. Never leave a failure edge dangling into nothing.

**Mark 권한 and 상태 where they gate behavior.** `role` answers "누가 접근 가능한가" (게스트/유저/관리자 …) — put it on the entry node of a permission-gated flow, or on a node that behaves differently per permission tier. `state` answers "어떤 조건일 때인가" (로그인됨, 데이터 없음, 로딩 …) — put it on nodes that only apply under that condition. Don't repeat the same role on every node — set it where it changes or gates.

**Classify every path node with `case`.** `happy` (default, gray), `error` (red — 실패 응답 처리: API 실패, 유효성 오류), `exception` (orange — 비정상이지만 예상되는 상황: 빈 데이터, 권한 없음, 중복, 네트워크 끊김). Classify by what the path handles, not by where it sits — the colors are how a developer finds "여기서 터지면?" answers. An optional step or a disabled-button state on the normal journey is still `happy`; reserve orange for paths that only run when something is off.

**Short text only.** Node `label` ≤ 16 chars, noun-style Korean (`주문 폼 진입`, not `사용자가 주문 폼에 진입한다`). `details` = 3~6 bullets, each ≤ 22 chars — field names, API paths, error codes, 정책 numbers. Long policy notes go into a `note` node (yellow sticky) at the **same `col` as its related node, first free `row` below it** — not into details.

**Keep the grid clean.** No two nodes share the same `(col, row)`. Merge-back edges (a branch returning to the happy path) are fine — connectors route themselves.

## Delivery notes

- The server saves the flow as `ux-flows/<페이지>-<기능>.json`; re-sending the same page/feature overwrites it, which is the intended way to revise a flow.
- Multiple features → multiple JSON files, one send each. The plugin lists them all.
- Drawing only works in FigJam (connectors are FigJam-only). In a Figma design file the plugin will refuse with a notice.
