---
name: spec-sync
description: Sync feature spec Markdown files from Figma (Figma = single source of truth). Use when the user says 스펙 싱크, 피그마 동기화, sync specs, 피그마 바뀐거 md 반영, or after they finish editing the Figma file. Detects changed frames via content fingerprints in .sync-state.json, re-reads only changed screens through the Figma Dev Mode MCP, updates the matching spec md files, and commits/pushes.
---

# Spec Sync (Figma → md, one-way)

Figma is the SSOT for 화면·문구·컴포넌트 상태. The spec mds additionally hold 정책·보안·데이터 requirements that are NOT visible in the design — never delete those during sync.

## Defaults (this project)

- Figma file: 스크럽대디 `SBGmrsYE4ooIBMwXvdtJ7S`, section `1851:88883` (v4.0 수정사항)
- Spec mds: clone of `safeai-kr/safe-qr-docs` (`main`, or the open docs branch), folder `general/feature/admin/` (관리 웹 문서; 소비자 문서는 `general/feature/consumer/`)
- Local mirror: `/Users/khy/Downloads/figmaplugin_260531/specs/`
- State file: `general/feature/admin/.sync-state.json` (committed with the specs)
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
5. **Update mds**: edit only the affected rows/cells of the mapped md(s), following the feature-generator skill rules (columns, short noun style). Keep 정책·보안·데이터 content that the design cannot show. Add one 변경 이력 row per updated file: version bump + "피그마 동기화 — <요약>" + `Claude, hy0909`.
6. **Write state**: regenerate `.sync-state.json` with new hashes, the Figma file key, section id, and `syncedAt` (ISO date).
7. **Ship**: copy updated files to the local mirror, `git add`, commit in Korean ("피그마 동기화 — <바뀐 화면 요약>"), push the branch. On non-fast-forward, rebase and preserve both histories.
8. **Report**: list per-file what changed, linking frame names to md files.

## 문체 규칙 (공통)

이 스킬이 만드는 모든 한국어 산문은 `human-writing` 스킬을 따른다 (같은 저장소의 `human-writing/SKILL.md`. Claude Code는 `~/.claude/skills/human-writing`, Codex는 `~/.codex/skills/human-writing`). 핵심만 요약:

- 한 문장에 생각 하나, 60자 안팎. 대조·원인은 `~지만`, `~기 때문에`로 한 문장에 잇고, 짧은 문장을 문두 `하지만/그래서`로 툭툭 끊지 않는다. 핵심 먼저.
- 개발·디자인을 모르는 사람이 읽는다고 가정한다. 전문용어는 첫 등장에 한 줄로 풀어 쓴다.
- 번역투 금지: `~를 통해`, `~에 있어서`, `~에 의해`, `~되어지다`, `위치해 있다`, `~함에도 불구하고`, `~를 가지고 있다`.
- 상투·기계적 표현 금지: `결론적으로`, `시사하는 바가 크다`, `~하는 것이 중요합니다`, `~할 필요가 있다`, `단순한 ~가 아니라`, `~뿐만 아니라 ~도`, `첫째·둘째·셋째` 나열, 형용사·명사 3개 나열, 문두 `또한/따라서/아울러` 연속, 대시(—), `혁신적인·원활한·강력한·다양한·효과적으로`, `파고들어 봅시다`, `잠재력을 발휘하다`.
- `~습니다`가 세 문장 연속이면 하나는 바꾼다. `-적/-성/-화`는 절반으로.
- `많은·다양한·최근·크게 개선`은 숫자·사례로 바꾼다. 정보가 없으면 지어내지 말고 `TBD` 또는 `[확인 필요]`.
- 비교·대조 가능한 항목은 표로 쓴다. 표로 할지 줄글로 할지 판단이 서지 않으면 사용자에게 묻는다(Claude Code에서는 AskUserQuestion 도구).
- 다 쓴 뒤 한 번 더 읽고 "여전히 AI 같아 보이는 곳"을 한 군데 찾아 고친다.
- 이 스킬의 예외: 표 셀·`목적`·`범위`·요구사항 행은 feature-generator의 명사형 종결 규칙(`데이터 출처 정의`)을 그대로 유지한다. 어미 변주·도치·문장 길이 변주는 설명 문단에만 적용. 반론·`[내 경험]` 같은 관점 규칙은 명세 문서에 넣지 않는다. 미정 표기는 기존 `TBD` / `원문 기준 추가 정의 필요`를 쓰고, 기존 TBD 행은 지우지 않는다.

## Guardrails

- One-way only (Figma → md). Never claim md → Figma is possible.
- Never delete TBD rows or 보안/데이터 requirements just because the design lacks them.
- If the Figma Dev Mode MCP is unreachable, tell the user to open the Figma desktop app (Preferences → Enable Dev Mode MCP Server) and stop — do not guess changes from memory.
- Mock-data-only differences (sample values like dates/IDs repeated across cards) are not spec changes — ignore unless labels/structure changed.
