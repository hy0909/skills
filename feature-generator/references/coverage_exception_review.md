# Coverage and Exception Review

Use this reference for every feature-spec draft. Its two purposes are:

1. prevent screens and functions explicitly present in the source from being omitted;
2. offer a separate, context-aware review of exception cases and missing policies after the initial MD is complete.

The checklist is diagnostic. It does not authorize silently inventing product policy or bloating the output with inapplicable rows.

## 1. Build the Coverage Inventory

Create an internal inventory before drafting and verify it again after drafting. Do not add the inventory to the final MD unless the user asks.

For each in-scope item, track its source and intended requirement row:

- screen, page, tab, step, drawer, modal, popup, and overlay;
- visible function, input, button, menu, bulk action, and system-triggered action;
- role or actor;
- initial, loading, empty, success, error, disabled, permission-limited, and other explicitly provided states;
- data created, viewed, changed, deleted, or passed to another system;
- entry condition, main flow, branch, completion result, and follow-up action.

Coverage is complete when every source-confirmed item is mapped to a requirement ID or explicitly excluded from scope with a reason.

### Figma-Based Input

- Inspect every in-scope frame and its meaningful variants, nested screens, overlays, tabs, and prototype-linked destinations available from the source.
- Map visible controls and interactions to the screen that owns them.
- Treat distinct loading, empty, error, success, permission, and partial-result frames as product states, not decorative duplicates.
- Apply the separate scroll-frame rules when a frame name contains `scroll`.
- Ignore clearly out-of-scope scratch frames or deprecated alternatives only when the source or user identifies them as such. Otherwise record the ambiguity for confirmation.

### Text-Based Input

- Extract screen nouns, user/system actions, roles, data objects, states, conditions, results, and follow-up behavior.
- Merge repeated wording without dropping a unique condition or branch.
- When the text describes behavior but not a screen, keep it as a functional or process requirement rather than inventing UI.

## 2. Respect Product Context

Classify the work before judging policy completeness.

### New Service or Blank-Slate Feature

- Use the review checklist to identify decisions that need a baseline policy.
- Recommend a concrete default only when it is a reasonable product decision; label it as a recommendation, not a confirmed rule.
- Present meaningful alternatives when the choice changes user experience, data integrity, security, or operations.

### Existing Product Improvement or New Feature in an Existing Product

- First inspect available context: neighboring files in the repository's `feature`, `features`, or feature-spec area; related PRD/policy documents; linked issues; existing requirement rows; and relevant Figma screens.
- Reuse established roles, permission boundaries, status terms, deletion behavior, notification rules, and audit conventions when the evidence is clear.
- If the relevant repository folder or document is unavailable, request its location or the minimum missing context only when needed to make a sound recommendation.
- Do not say or imply that the user failed to define a policy. Use neutral evidence-based wording such as `현재 제공 자료에서는 권한 범위를 확인할 수 없어 추가 정의를 권장합니다.`

## 3. Initial Draft Boundary

The initial MD must include:

- every in-scope screen and function confirmed by the source;
- every exception, restriction, state, and recovery behavior explicitly defined by the source;
- `TBD` or `원문 기준 추가 정의 필요` only where the missing decision must be visible for implementation.

Do not add guessed permissions, deletion rules, retry behavior, notification delivery, external-system behavior, or audit policy as if they were confirmed.

## 4. Mandatory Review Offer

After the initial MD is complete, ask:

> 작성된 기능명세를 기준으로 예외 케이스 및 누락 정책의 추가 작성을 검토해드릴까요?

If commit/push was requested, ask before committing or pushing.

- If the user declines, keep the initial MD and continue with any already requested finalization.
- If the user agrees, perform the context review and checklist below, then present recommendations before adding unsupported policy.
- After presenting recommendations, ask which recommendations to reflect. Update the MD only with the user's selection or confirmation, then recheck coverage and proceed with any requested commit/push.

## 5. Exception and Policy Checklist

Review every category, but report only relevant gaps, ambiguities, or risks. Internally mark irrelevant items as not applicable with a reason instead of adding noise to the MD.

### 5.1 접근 및 권한

- 기능 진입 조건
- 사용자별 접근 권한
- 조회·생성·수정·삭제 권한
- 본인 데이터와 타인 데이터의 처리 범위
- 권한이 없을 때의 처리 방식

### 5.2 CRUD 및 데이터 관리

- 생성 가능 여부와 필수 입력값
- 조회 가능 여부와 조회 범위
- 수정 가능 여부와 수정 가능 항목
- 삭제 가능 여부
- 소프트 삭제·영구 삭제 기준
- 삭제 후 복구 가능 여부와 복구 기한
- 일괄 등록·수정·삭제 가능 여부
- 중복 데이터 처리 기준
- 연관 데이터가 있을 때의 수정·삭제 제한
- 변경 이력 기록 여부

### 5.3 상태 및 생명주기

- 최초 기본 상태
- 상태 종류
- 상태별 가능 행동
- 상태 변경 조건
- 이전 상태로 되돌릴 수 있는지
- 자동 상태 변경 조건
- 종료·만료·보관 조건

### 5.4 화면 및 시스템 상태

- 기본 상태
- 로딩 상태
- 빈 상태
- 오류 상태
- 성공 상태
- 부분 성공 상태
- 권한 제한 상태
- 네트워크 연결 해제 상태
- 처리 중 중복 실행 방지

### 5.5 작업 제어 및 복구

- 중단·취소 가능 여부
- 취소 가능 시점
- 취소 시 이미 처리된 데이터의 처리 방식
- 재시도 가능 여부
- 자동·수동 재시도 기준
- 실패 후 복구 방법
- 저장되지 않은 변경사항 이탈 경고
- 실행 취소 및 되돌리기 가능 여부

### 5.6 결과 및 후속 처리

- 성공·실패 알림 방식
- 완료 후 이동 화면
- 데이터 즉시 반영 여부
- 알림 발송 여부
- 외부 시스템 연동 결과
- 변경 이력·감사 로그 기록
- 후속 작업 자동 생성 여부

## 6. Recommendation Output

Ground every recommendation in the current draft and available product context. Include only items that need a decision.

Use a compact table:

| 검토 영역 | 적용 화면·기능/요구사항 ID | 확인 근거 | 검토 결과 | 권장 정책 문구 |
| --- | --- | --- | --- | --- |

Use these result labels:

- `추가 정의 권장`: evidence suggests a policy is needed but the policy is absent;
- `맥락 확인 필요`: existing product context may define it elsewhere or sources conflict;
- `보완 권장`: a rule exists but does not cover a relevant branch;
- `해당 없음`: omit from the user-facing table unless its absence would otherwise be confusing.

Write recommendations as actionable suggestions, for example:

- `권한이 없는 사용자는 메뉴를 숨기고 직접 URL 접근 시 접근 제한 안내를 노출하는 정책을 권장합니다.`
- `일괄 처리 중 일부 항목만 실패한 경우 성공 건은 반영하고 실패 건과 사유를 제공하는 부분 성공 정책을 권장합니다.`

Reference the relevant requirement ID, Figma frame, source heading, or repository document when available. Do not present a recommendation as an already approved rule.

When the user approves a recommendation:

- add it to the relevant requirement row;
- use `핵심 기획 규칙` only when it affects multiple rows or prevents cross-cutting misunderstanding;
- do not create a separate exception-case section unless the user asks;
- record the material update in change history.
