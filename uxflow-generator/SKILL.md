---
name: uxflow-generator
description: Create developer-friendly UX flow diagrams on FigJam so FE/BE developers can check business logic and branch handling at a glance. Use whenever the user asks for a UX flow, 유저 플로우, 화면 흐름도, 플로우차트, FigJam/피그잼 flow, 분기 정리, or wants to hand developers a page/feature-level flow with happy/error/exception paths, 권한(role), 상태(state), and yes/no branch arrows. Takes 기획 내용 (text or spec md) plus Figma design links, produces flow JSON, and sends it to the local plugin server (localhost:3765) so the 핸드오프문서 자동생성기 FigJam plugin draws it.
---

# UX Flow Generator

Turn planning text and Figma designs into a FigJam flow diagram that FE/BE developers use to implement business logic and branch handling. The reader is a developer asking "이 화면에서 무슨 일이 일어나고, 어떤 조건에서 어디로 가는가?" — every rule below exists to answer that question at a glance.

## Pipeline

1. **Collect input.** Planning text, spec markdown, or a conversation description — plus Figma design links when available.
2. **Read the design.** For each Figma link, use the Figma MCP (`get_metadata` first, then `get_screenshot` / `get_design_context` for the needed nodes) to identify screens, buttons, empty/error states, and permission-gated UI. Every link you consulted goes into `figmaLinks` — developers jump from the flow to the design through these.
3. **Split by page/feature.** One flow = one 페이지 + one 기능 (e.g. `QR 주문 > 주문 생성`). If a flow needs more than ~9 columns or ~18 nodes, split it into two features rather than shrinking text.
4. **Author the flow JSON.** Schema and a complete example: `references/flow-schema.md`. Writing rules below.
5. **Validate.** `python3 scripts/validate_flow.py <flow.json>` — fix every ERROR, review every WARN.
6. **Send.** `python3 scripts/validate_flow.py <flow.json> --send` (POSTs to `http://localhost:3765/ux-flow`). If the server is down, tell the user to run `./start-server.sh` in the plugin folder (`~/Downloads/figmaplugin_260531`), then retry.
7. **Tell the user how to draw it:** open a **FigJam** file → run the `핸드오프문서 자동생성기` plugin → `UX Flow` tab → click the flow. Mention the flow name you saved.

## Writing rules — developer's point of view

**Happy path reads left to right on one line.** Put the success path on `row: 0`, ordered by time (`col` 0, 1, 2, …). Branches (error/exception) drop to `row: 1+` below the decision that spawns them. A developer should trace the main scenario without ever scanning vertically.

**Every branch is an explicit decision.** Anywhere the implementation needs an `if` — validation, API response, permission, empty data — add a `decision` node (a short question, e.g. `재고 있음?`) with **all outgoing edges labeled** (`YES`/`NO` or the concrete condition like `401`, `중복`). YES/성공 continues right on the happy row; NO/실패 goes down. Unlabeled decision edges are the #1 thing that makes developers guess — the validator rejects them.

**Separate what FE and BE each implement.**
- `api` nodes are BE touchpoints: details start with `METHOD /path` (e.g. `POST /orders`), then key request fields and response codes the flow branches on.
- `owner: "FE" | "BE" | "FE·BE"` on nodes where ownership isn't obvious from the type.
- FE-side handling (토스트, 리다이렉트, 버튼 비활성) are `action`/`screen` nodes — every error/exception path must end at a node stating what the user actually sees. Never leave a failure edge dangling into nothing.

**Mark 권한 and 상태 where they gate behavior.** `role` (게스트/유저/관리자 …) on entry screens or any node that behaves differently by permission; `state` (로그인됨, 데이터 없음, 로딩 …) when a node only applies in that state. Don't repeat the same role on every node — set it where it changes or gates.

**Classify every path node with `case`.** `happy` (default, gray), `error` (red — API 실패, 유효성 오류 등 실패 응답 처리), `exception` (orange — 빈 데이터, 권한 없음, 중복, 네트워크 끊김 같은 edge case). The colors are how a developer finds "여기서 터지면?" answers, so classify by what the path handles, not by where it sits.

**Short text only.** Node `label` ≤ 16 chars, noun-style Korean (`주문 폼 진입`, not `사용자가 주문 폼에 진입한다`). `details` = 3~6 bullets, each ≤ 22 chars — field names, API paths, error codes, 정책 numbers. Long policy notes go into a `note` node (yellow sticky) placed in the cell below its related node, not into details.

**Keep the grid clean.** No two nodes share the same `(col, row)`. Merge-back edges (a branch returning to the happy path) are fine — connectors route themselves.

## Delivery notes

- The server saves the flow as `ux-flows/<페이지>-<기능>.json`; re-sending the same page/feature overwrites it, which is the intended way to revise a flow.
- Multiple features → multiple JSON files, one send each. The plugin lists them all.
- Drawing only works in FigJam (connectors are FigJam-only). In a Figma design file the plugin will refuse with a notice.
