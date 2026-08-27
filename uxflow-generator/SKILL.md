---
name: uxflow-generator
description: Create developer-friendly UX flow diagrams on FigJam so FE/BE developers can check business logic and branch handling at a glance. Use whenever the user asks for a UX flow, 유저 플로우, 화면 흐름도, 플로우차트, FigJam/피그잼 flow, 분기 정리, or wants to hand developers a page/feature-level flow with happy/error/exception paths, 권한(role), 상태(state), and yes/no branch arrows. Takes 기획 내용 (text or spec md) plus Figma design links, produces flow JSON, and sends it to the local plugin server (localhost:3765) so the UX 플로우 생성기 FigJam plugin draws it.
---

# UX Flow Generator

Turn planning text and Figma designs into a FigJam flow diagram that FE/BE developers use to implement business logic and branch handling. The reader is a developer asking "이 화면에서 무슨 일이 일어나고, 어떤 조건에서 어디로 가는가?" — every rule below exists to answer that question at a glance.

## Pipeline

1. **Collect input.** Planning text, spec markdown, or a conversation description — plus Figma design links when available. **Spec md가 있으면 md가 최우선 기준이다**: 요구사항 ID(REQ-*)·필수/선택·에러 케이스를 md에서 그대로 가져오고, md의 GitHub URL을 `docLinks`에 넣는다(플러그인이 우측 상단에 📄 링크로 그린다).
2. **Read the design.** For each Figma link, use the Figma MCP (`get_metadata` first, then `get_screenshot` / `get_design_context` for the needed nodes) to identify screens, buttons, empty/error states, and permission-gated UI. Every link you consulted goes into `figmaLinks` — developers jump from the flow to the design through these.
3. **Split by page/feature — page names come from the IA.** One flow = one 페이지 + one 기능 (e.g. `QR 발주 내역 > 발주 승인`). `page` must match the product IA so developers can map flows to routes/menus — check `references/ia.md` (canonical IA Figma link + cached snapshot) before naming, and include the IA link in `figmaLinks` when you consulted it. If a flow needs more than ~9 columns or ~18 nodes, split it into two features rather than shrinking text.
4. **Author the flow JSON.** Schema and a complete example: `references/flow-schema.md`. Writing rules below.
5. **Validate.** `python3 scripts/validate_flow.py <flow.json>` — fix every ERROR, review every WARN.
6. **Send.** `python3 scripts/validate_flow.py <flow.json> --send` (POSTs to `http://localhost:3765/ux-flow`). If the server is down, tell the user to run `./start-server.sh` in the plugin folder (`~/Downloads/figjam_260827`), then retry.
7. **Tell the user how to draw it:** open a **FigJam** file → run the `UX 플로우 생성기` plugin → `UX Flow` tab → click the flow. Mention the flow name you saved.

## Writing rules — developer's point of view

**Form fields are parallel, not a chain.** 한 화면(폼/모달)에서 입력하는 필드들은 시간 순서가 없다 — 수량 → 수출국 → 제품처럼 순차 체인으로 그리지 말 것. 같은 col에 세로로 나란히 배치해 화면 노드에서 병렬로 분기시키고(edge label `병렬`), 모두 "버튼 활성 조건" decision(예: `필수 모두 입력?`)으로 모은다. **필수 입력 노드는 라벨 끝에 `*`, 선택 입력은 라벨에 `(선택)`을 붙인다** — 플러그인이 `*`를 빨간색으로 강조하고 범례에 `* 필수 입력 · (선택) 선택 입력`을 자동 표기하므로, 이 표기만 지키면 비주얼로 필수/선택이 구분된다. 디자인이 실제로 입력 순서를 강제할 때만 체인을 쓴다.

**Spec에 정의된 에러 케이스는 하나도 빠짐없이 red로.** 유효성 에러가 여러 종류면(예: 단위 오류/개수 초과/총량 초과) 각각 별도 `error` 노드로 쪼개고 decision에서 조건별 edge label로 분기시킨다 — 뭉뚱그린 "오류 표시" 하나로 합치면 개발자가 케이스를 놓친다.

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
