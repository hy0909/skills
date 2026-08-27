---
name: spec-sync
description: Sync feature spec Markdown files from Figma (Figma = single source of truth). Use when the user says 스펙 싱크, 피그마 동기화, sync specs, 피그마 바뀐거 md 반영, or after they finish editing the Figma file. Detects changed frames via content fingerprints in .sync-state.json, re-reads only changed screens through the Figma Dev Mode MCP, updates the matching spec md files, and commits/pushes.
---

# Spec Sync (Figma → md, one-way)

Figma is the SSOT for 화면·문구·컴포넌트 상태. The spec mds additionally hold 정책·보안·데이터 requirements that are NOT visible in the design — never delete those during sync.

## Defaults (this project)

- Figma file: 스크럽대디 `SBGmrsYE4ooIBMwXvdtJ7S`, section `1851:88883` (v4.0 수정사항)
- Spec mds: clone of `safeai-kr/safe-qr-docs`, branch `docs/qr-order-group-spec`, folder `general/feature/`
- Local mirror: `/Users/khy/Downloads/figmaplugin_260531/specs/`
- State file: `general/feature/.sync-state.json` (committed with the specs)
- Frame → md mapping:
  - QR 그룹 관리 목록 frames → `qr-group-list.md`
  - QR 그룹 상세 frames → `qr-group-detail.md`
  - QR 발주하기/발주서 모달 frames → `qr-order-form.md`
  - QR 발주 내역(사용자) frames → `qr-order-list.md` / 상세 → `qr-order-detail.md`
  - QR 발주 내역(관리자) frames → `admin-qr-order-list.md` / 상세 → `admin-qr-order-detail.md`
  - 인증 내역 frames → `qr-auth-history.md`
  - GNB·용어·상태 정책 changes → `common.md`

## Workflow

1. **Fingerprint**: call Figma MCP `get_metadata` on the section. If the result is saved to a file, parse it. For each top-level child frame, compute an md5 over its XML subtree with `x=`/`y=` attributes stripped (moves must not count as changes). Build `{frameId: {name, hash}}`.
2. **Diff vs state**: compare with `.sync-state.json`. Classify: added / removed / changed frames. If none → report "피그마와 md가 이미 동기화 상태" and stop.
3. **Ask (check mode)**: if invoked with `check`, only report the drift ("피그마가 바뀌었어요: N개 화면. 최신 버전으로 md를 수정할까요?") and stop — do not edit.
4. **Re-read changed frames only**: `get_screenshot` per changed frame (and `get_metadata` when text extraction helps). Identify what actually changed on screen (문구, 컬럼, 버튼, 상태, 플로우).
5. **Update mds**: edit only the affected rows/cells of the mapped md(s), following the feature-generator skill rules (columns, short noun style). Keep 정책·보안·데이터 content that the design cannot show. Add one 변경 이력 row per updated file: version bump + "피그마 동기화 — <요약>" + `Claude, 김혜연`.
6. **Write state**: regenerate `.sync-state.json` with new hashes, the Figma file key, section id, and `syncedAt` (ISO date).
7. **Ship**: copy updated files to the local mirror, `git add`, commit in Korean ("피그마 동기화 — <바뀐 화면 요약>"), push the branch. On non-fast-forward, rebase and preserve both histories.
8. **Report**: list per-file what changed, linking frame names to md files.

## Guardrails

- One-way only (Figma → md). Never claim md → Figma is possible.
- Never delete TBD rows or 보안/데이터 requirements just because the design lacks them.
- If the Figma Dev Mode MCP is unreachable, tell the user to open the Figma desktop app (Preferences → Enable Dev Mode MCP Server) and stop — do not guess changes from memory.
- Mock-data-only differences (sample values like dates/IDs repeated across cards) are not spec changes — ignore unless labels/structure changed.
