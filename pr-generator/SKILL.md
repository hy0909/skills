---
name: pr-generator
description: Create GitHub pull requests for SafeAI work. Use when the user asks to create, open, draft, publish, edit, comment on, or prepare a PR; assign PRs to `hy0909` by default and ask who should be requested as reviewer when reviewers were not specified. Before creating a PR, editing its body, or posting a PR comment, always ask 「추가 검토할까요?」 (1 consistency/conflict/dev impact, 2 exception/error cases, 3 none), then show the full body in chat and get explicit approval; write the body with the human-writing skill.
---

# PR Generator

## Overview

Use this skill for GitHub PR creation. It adds the user's required planning guardrails: PR Assignees default to `hy0909`, and Reviewer selection must be explicit.

## Core Rules

- Always use the authenticated GitHub account `hy0909` when running GitHub commands.
- Always set PR Assignees to `hy0909`.
- Before creating any PR, explicitly mention `Assignees: hy0909`.
- Do not stop to ask for Assignees when the user did not specify them; `hy0909` is the default and required assignee.
- Before creating any PR, explicitly mention the Reviewer plan.
- If the user did not specify Reviewers, stop and ask who should be requested as reviewer. Do not create the PR until the user answers.
- If Reviewers were already specified in the same request, state them back before creating the PR.
- Default PRs to draft unless the user explicitly asks for ready-for-review.
- Never stage unrelated user changes silently.
- Document links in the PR body: write the `main` path first (permanent — the head branch is deleted after merge), then the head-branch link, each labeled so the reader can tell which is which: `[file.md (main 기준)](main-url) · [같은 파일 (브랜치 <head-branch-name>, 병합 후 삭제 예정)](head-branch-url)`. Always write the real branch name; a bare `브랜치에서 보기` is not enough. Add one line at the bottom: `※ 문서 링크는 main 기준이라 병합 후 열립니다. 병합 전에는 옆의 브랜치 링크로 확인해 주세요. 브랜치는 병합 후 삭제됩니다.`
- After creating or editing a PR, verify the PR URL, title, assignees, reviewers, base branch, head branch, and draft state.
- Whenever this skill itself is modified, keep the installed local skill and GitHub source repository in sync, then commit and push the change.

## PR Creation Workflow

1. Confirm the repository and branch context.
2. Inspect `git status -sb` and relevant diffs before staging.
3. Confirm the intended PR scope if unrelated changes exist.
4. Handle Assignees and Reviewers before PR creation:
   - Always mention `Assignees: hy0909` before creating.
   - Always ask who should be requested as Reviewer if the user did not specify reviewers.
   - If Reviewers were specified, state the proposed Reviewers back and proceed only when unambiguous.
5. Stage only intended files.
6. Commit with a concise message when changes are not already committed.
7. Push the branch.
8. Ask 「추가 검토할까요?」 and run the chosen reviews (see 「올리기 전 추가 검토」). Then show the full PR title and body in chat and wait for explicit approval (see 「올리기 전 승인」). Then create a draft PR with the approved title, body, base branch, `hy0909` assignee, and confirmed reviewers. PR comments and body edits follow the same rule.
9. Verify the PR metadata after creation.

## Metadata Defaults

- Assignees: always `hy0909`.
- Reviewers: always ask before PR creation if not specified.
- Labels: use user-requested labels; otherwise choose an appropriate existing label only when clearly applicable.
- Project fields: set only when repository/project context is available.

## 올리기 전 추가 검토 (2026-10-29 사용자 규칙)

본문 초안을 쓴 뒤, 올리기 전 승인을 받기 전에 추가 검토를 할지 **반드시** 묻는다. 「검토 없이 올려」라고 미리 말했더라도 묻는다. 게시물마다 새로 묻고, 앞에서 받은 답을 다음 게시물에 쓰지 않는다.

- 대상: PR 생성, PR 제목·본문 수정, PR 댓글·리뷰
- 질문: `추가 검토할까요?`
- Claude Code에서는 AskUserQuestion 도구로 묻는다. 여러 개를 고를 수 있게(multiSelect) 하고 선택지는 아래 세 개다.

| 선택지 | 검토 내용 |
| --- | --- |
| 1. 일관성·충돌·개발 영향 | 문서 간 일관성, 충돌 여부, 이대로 개발했을 때 이상하게 될 점 |
| 2. 예외·에러 케이스 | 예외 상황과 에러 케이스가 빠짐없이 나왔는지 |
| 3. 선택 안 함 | 추가 검토 없이 본문 승인 단계로 감 |

- 1과 2는 함께 고를 수 있다. 3을 1·2와 함께 고르면 다시 묻는다.
- 답을 받기 전에는 올리는 명령(`gh issue create`, `gh issue edit`, `gh issue comment`, `gh pr create`, `gh pr edit`, `gh pr comment`, `gh pr review`)을 실행하지 않는다.

**1을 고르면**
`../feature-generator/references/pre_publish_review.md` 2~4절대로 서브에이전트 세 개(기획 일관성, 개발 영향, 충돌)를 동시에 띄운다. 서브에이전트를 쓸 수 없는 환경에서는 같은 검토를 차례로 직접 한다.

**2를 고르면**
서브에이전트 하나를 띄워 올릴 글과 글이 다루는 문서(바뀐 MD, 언급한 요구사항)를 읽고 아래가 정해져 있는지 본다. 기준은 `../feature-generator/references/coverage_exception_review.md`다.

- 화면 상태: 처음 진입, 불러오는 중, 빈 화면, 오류, 권한 없음, 일부만 성공
- 입력: 필수값 누락, 형식 오류, 글자 수·개수 한도, 중복 입력
- 처리: 서버 오류, 네트워크 끊김, 시간 초과, 같은 요청 두 번, 다른 사람이 동시에 수정
- 데이터: 대상이 지워졌거나 권한이 바뀐 경우, 보관 기간이 지난 경우
- 흐름: 각 분기의 끝(성공·실패 뒤 어디로 가는지), 되돌리기·취소

정해지지 않은 것은 정책을 지어내지 말고 `정의 필요`로 적는다. 작업과 관계없는 항목은 빼고 보고한다.

**결과 보고**
서브에이전트 결과는 근거 위치를 직접 열어 맞는지 확인한 뒤 아래 표로 보고한다. 확인하지 못한 것은 `확인 필요`로 적는다.

| 심각도 | 검토 | 위치 | 문제 | 근거 | 권장 조치 |
| --- | --- | --- | --- | --- | --- |

- 심각도는 `병합 막음`, `병합 전 권장`, `참고` 세 가지만 쓴다.
- 지적이 없으면 `중요 문제 없음`과 무엇을 어디까지 봤는지 한 줄로 적는다.
- 어떤 지적을 반영할지 사용자에게 묻고, 반영한 뒤 고친 본문 전체를 다시 보여 주고 「올리기 전 승인」을 받는다.

## 올리기 전 승인 (2026-10-29 사용자 규칙)

GitHub에 글을 남기는 모든 동작은 사용자가 본문을 보고 승인한 뒤에만 실행한다. 사용자가 승인하지 않은 글을 올리지 않는다.

- 대상: PR 생성, PR 제목·본문 수정, PR 댓글·리뷰 작성
- 순서: 본문 작성 → 「추가 검토할까요?」 질문과 검토 → 채팅에 제목과 본문 전체를 그대로 보여 줌 → 사용자 승인 → 실행
- 승인은 「올려」, 「이대로 올려」처럼 이 본문을 올리라고 분명히 말한 경우만 인정한다. 「남겨」, 「정리해」, 「반영해」, 「처리해」는 올리라는 승인이 아니다. 이때도 초안을 먼저 보여 주고 올릴지 묻는다.
- 본문을 한 글자라도 고치면 고친 본문을 다시 보여 주고 다시 승인받는다.
- 사용자가 본문이나 댓글의 일부를 고쳐 달라고 하면, 바뀐 부분만 따로 보여 주지 않는다. 고친 내용을 반영한 제목과 본문 전체를 처음부터 끝까지 다시 보여 준다(2026-10-29 사용자 규칙).
- 본문은 채팅에서 표가 제대로 보이게 코드 블록 없이 보여 준다. GitHub에 올라갈 모습 그대로다.
- 승인 없이 올린 것을 알게 되면 바로 사용자에게 알리고, 사용자가 원하면 지운다.
- 본문을 쓰기 전에 `human-writing` 스킬을 먼저 불러와 그 규칙대로 쓴다(Claude Code는 Skill 도구로 `human-writing` 호출, 없으면 `~/.claude/skills/human-writing/SKILL.md`를 읽는다). 아래 「문체 규칙」은 요약일 뿐이다.

## 마크다운 표기 주의: 물결표 (2026-10-30 사용자 규칙)

GitHub는 물결표(`~`) 두 개 사이의 글자에 취소선을 긋는다. #130 댓글에서 `1~7번 가운데 … 3~7번은`이 `7번 가운데 … 3`에 줄이 그어진 채로 올라갔다. 이 사례 때문에 만든 규칙이다.

- 이슈·PR 제목, 본문, 댓글에서 범위를 `~`로 쓰지 않는다. `1번부터 7번까지`, `1단계부터 3단계까지`, `10-29부터 10-30까지`처럼 글로 쓴다.
- 물결표가 하나뿐이어도 쓰지 않는다. 나중에 다른 문장을 고치다가 물결표가 하나 더 생기면 그 사이에 취소선이 생긴다.
- 올리기 전에 본문 파일에서 `grep -n '~' <본문 파일>`로 물결표가 남았는지 확인한다. 코드 블록이나 백틱 안에 있는 명령어·경로는 예외다.
- 채팅에 초안을 보여 줄 때도 같은 표기로 쓴다. 채팅 화면과 GitHub 화면이 다르게 보이면 사용자가 검토할 수 없다.

## 문체 규칙 (공통)

이 스킬이 만드는 모든 한국어 산문은 `human-writing` 스킬을 따른다 (같은 저장소의 `human-writing/SKILL.md`. Claude Code는 `~/.claude/skills/human-writing`, Codex는 `~/.codex/skills/human-writing`). 핵심만 요약:

- 한 문장에 생각 하나, 60자 안팎. 대조·원인은 `~지만`, `~기 때문에`로 한 문장에 잇고, 짧은 문장을 문두 `하지만/그래서`로 툭툭 끊지 않는다. 핵심 먼저.
- 개발·디자인을 모르는 사람도 읽게 일상 동사(쓰다·적어 두다·손보다·나누다)로 쓴다. 한자어 명사구는 `언제 쓰는지, 어디까지 바꿀 수 있는지`처럼 푼다. 용어는 우리말이 있으면 바꾸고(베리언트→형태별 구분), 팀이 매일 쓰는 말은 그대로 둔다. 서술 문장 한가운데 괄호 설명을 끼우지 않는다. 억지 동의어·도치·조각 문장 금지. 문단 첫 문장은 결론.
- 번역투 금지: `~를 통해`, `~에 있어서`, `~에 의해`, `~되어지다`, `위치해 있다`, `~함에도 불구하고`, `~를 가지고 있다`.
- 상투·기계적 표현 금지: `결론적으로`, `시사하는 바가 크다`, `~하는 것이 중요합니다`, `~할 필요가 있다`, `단순한 ~가 아니라`, `~뿐만 아니라 ~도`, `첫째·둘째·셋째` 나열, 형용사·명사 3개 나열, 문두 `또한/따라서/아울러` 연속, 대시(—), `혁신적인·원활한·강력한·다양한·효과적으로`, `파고들어 봅시다`, `잠재력을 발휘하다`.
- `~습니다`가 세 문장 연속이면 하나는 바꾼다. `-적/-성/-화`는 절반으로.
- `많은·다양한·최근·크게 개선`은 숫자·사례로 바꾼다. 정보가 없으면 지어내지 말고 `TBD` 또는 `[확인 필요]`.
- 비교·대조 가능한 항목은 표로 쓴다. 표로 할지 줄글로 할지 판단이 서지 않으면 사용자에게 묻는다(Claude Code에서는 AskUserQuestion 도구).
- 다 쓴 뒤 한 번 더 읽고 "여전히 AI 같아 보이는 곳"을 한 군데 찾아 고친다.
- 범위는 물결표(`~`) 대신 `부터 … 까지`로 쓴다. GitHub에서 취소선이 된다(「마크다운 표기 주의: 물결표」).
- 이 스킬의 예외: 이슈·PR 본문 산문에 적용한다. 제목은 명사형. 링크 형식, `main 병합 후 열립니다` 안내, 명령어·메타데이터 표기는 기존 규칙 그대로 둔다. 관점 규칙은 넣지 않는다.

## Skill Maintenance

When updating this skill:

- Edit the working skill source first.
- Sync the same content into the installed local skill at `~/.codex/skills/pr-generator`.
- Sync the same content into the GitHub source repository, expected to be `hy0909/skills`.
- Commit and push the skill update whenever possible.
- If validation cannot run because a local dependency is missing, say so and still verify file contents directly.
