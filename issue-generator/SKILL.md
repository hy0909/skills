---
name: issue-generator
description: Create or update GitHub issues and sub-issues for SafeAI planning work. Use when the user asks to create, edit, comment on, move, transfer, or verify an issue/sub-issue, especially when repository routing, assignees, labels, issue type, project fields, priority, or start date matters: always prefer the matching `*-docs` repository for planning issues, and assign new issues to `hy0909` by default. Before posting an issue, issue edit, or issue comment, always ask 「추가 검토할까요?」 (1 consistency/conflict/dev impact, 2 exception/error cases, 3 none), then show the full body in chat and get explicit approval; write the body with the human-writing skill.
---

# Issue Generator

## Overview

Use this skill for SafeAI GitHub issue work. The user is a planner, so planning issues and sub-issues must be created in documentation repositories, not development repositories.

## Core Rules

- Always use the authenticated GitHub account `hy0909` when running GitHub commands.
- Never infer that a development repository is the correct target for planning issues.
- Before creating or moving an issue, confirm the target repository name contains `docs`.
- If the user provides a non-docs repository URL, route to the matching docs repository when it exists.
- For `safeai-kr/safe-site`, use `safeai-kr/safe-site-docs`.
- For plain issues, create the issue directly in the docs repository.
- For sub-issues, create the child issue in the docs repository and set the provided parent issue with `--parent` when available.
- Always set issue and sub-issue Assignees to `hy0909`.
- Before creating any issue or sub-issue, explicitly mention `Assignees: hy0909`.
- Do not stop to ask for Assignees when the user did not specify them; `hy0909` is the default and required assignee.
- If the user requests extra assignees such as FE/BE, include `hy0909` and the requested additional assignees unless the user explicitly says otherwise.
- If the user says FE/BE assignees, add FE `easyDong19` and BE `gurdl0525` in addition to `hy0909`.
- When labels, issue type, project fields, priority, or start date are available, set sensible planning defaults instead of leaving them empty.
- Default priority to a middle/medium value unless the user says otherwise.
- Default start date to today's local date from the active environment context unless the user says otherwise.
- If an issue is accidentally created in a non-docs repository, transfer it to the matching docs repository immediately and verify the new URL.
- After creating, transferring, or editing an issue, verify the result with `gh issue view`.
- Document links in an issue body or comment: the permanent link is the `main` path (`.../blob/main/...`) because feature branches are deleted after merge. While the change is unmerged, write both, main first, and label each link so the reader can tell which is which: `[file.md (main 기준)](main-url) · [같은 파일 (브랜치 <branch-name>, 병합 후 삭제 예정)](branch-url)` — always spell out the real branch name, and add one line at the bottom: `※ 문서 링크는 main 기준이라 병합 후 열립니다. 병합 전에는 옆의 브랜치 링크로 확인해 주세요. 브랜치는 병합 후 삭제됩니다.`
- Whenever this skill itself is modified, keep the installed local skill and GitHub source repository in sync, then commit and push the change.

## Repository Routing

Use this mapping unless the user explicitly names a different docs repository:

- `safeai-kr/safe-site` -> `safeai-kr/safe-site-docs`
- A repository named `<name>` -> prefer `<name>-docs` if it exists.

If both a development repo and a docs repo appear in context, use the docs repo for issue creation. Keep development repo links only as references in the body or parent relationship.

## Issue Creation Workflow

1. Parse the user's request and identify whether it is a plain issue or sub-issue.
2. Extract the referenced repository and issue number or URL, if present.
3. Resolve the creation repository to a docs repository.
4. Draft the issue in Korean, matching the user's concise planning style. Pair every repo link as `(main 기준)` + `(브랜치 <name>, 병합 후 삭제 예정)` while unmerged, and add the note line.
5. Handle assignees before creation:
   - Always mention `Assignees: hy0909` before creating.
   - If no assignees were specified, proceed with `hy0909`.
   - If extra assignees were specified, include `hy0909` and state the full proposed assignee list before creating.
   - FE: `easyDong19`
   - BE: `gurdl0525`
6. Apply issue metadata when possible:
   - Labels: use the user's requested labels; otherwise choose an appropriate planning label only if it exists.
   - Type: use a planning/product/documentation type when the repository supports issue types.
   - Priority field: default to middle/medium.
   - Start date field: default to today's local date.
7. Ask 「추가 검토할까요?」 and run the chosen reviews (see 「올리기 전 추가 검토」). Then show the full title and body in chat and wait for explicit approval (see 「올리기 전 승인」). Then create or edit the issue with `gh issue create` or `gh issue edit`. Issue comments follow the same rule before `gh issue comment`.
8. Verify title, URL, assignees, labels, type, parent relationship, and any project fields that were set.

## Sub-Issue Workflow

When the user asks for a sub-issue:

- Use `gh issue create --repo <docs-repo> --parent <parent-number-or-url>`.
- If the parent issue is in a development repo, keep the parent URL but still create the sub-issue in the docs repo.
- Include a `Parent Issue` section in the body with the parent URL or issue number.
- Verify `parent` and `assignees` fields after creation.

Example:

```bash
gh issue create \
  --repo safeai-kr/safe-site-docs \
  --parent https://github.com/safeai-kr/safe-site/issues/12 \
  --title "[PD] 위험알림 보고서 컴포넌트 제작 및 기획 문서 작성" \
  --body-file <body-file> \
  --assignee hy0909,easyDong19,gurdl0525
```

## Transfer Workflow

When an issue was created in a non-docs repo by mistake:

```bash
gh issue transfer <issue-number-or-url> safeai-kr/safe-site-docs --repo safeai-kr/safe-site
```

Then run:

```bash
gh issue view <new-number> --repo safeai-kr/safe-site-docs --json title,url,assignees,parent,body
```

## 올리기 전 추가 검토 (2026-10-29 사용자 규칙)

본문 초안을 쓴 뒤, 올리기 전 승인을 받기 전에 추가 검토를 할지 **반드시** 묻는다. 「검토 없이 올려」라고 미리 말했더라도 묻는다. 게시물마다 새로 묻고, 앞에서 받은 답을 다음 게시물에 쓰지 않는다.

- 대상: 이슈 생성, 이슈 제목·본문 수정, 이슈 댓글, 하위 이슈 생성
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

- 대상: 이슈 생성, 이슈 제목·본문 수정, 이슈 댓글 작성·수정, 하위 이슈 생성
- 순서: 본문 작성 → 「추가 검토할까요?」 질문과 검토 → 채팅에 제목과 본문 전체를 그대로 보여 줌 → 사용자 승인 → 실행
- 승인은 「올려」, 「이대로 올려」처럼 이 본문을 올리라고 분명히 말한 경우만 인정한다. 「남겨」, 「정리해」, 「반영해」, 「처리해」는 올리라는 승인이 아니다. 이때도 초안을 먼저 보여 주고 올릴지 묻는다.
- 본문을 한 글자라도 고치면 고친 본문을 다시 보여 주고 다시 승인받는다.
- 본문은 채팅에서 표가 제대로 보이게 코드 블록 없이 보여 준다. GitHub에 올라갈 모습 그대로다.
- 승인 없이 올린 것을 알게 되면 바로 사용자에게 알리고, 사용자가 원하면 지운다.
- 본문을 쓰기 전에 `human-writing` 스킬을 먼저 불러와 그 규칙대로 쓴다(Claude Code는 Skill 도구로 `human-writing` 호출, 없으면 `~/.claude/skills/human-writing/SKILL.md`를 읽는다). 아래 「문체 규칙」은 요약일 뿐이다.

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
- 이 스킬의 예외: 이슈·PR 본문 산문에 적용한다. 제목은 명사형. 링크 형식, `main 병합 후 열립니다` 안내, 명령어·메타데이터 표기는 기존 규칙 그대로 둔다. 관점 규칙은 넣지 않는다.

## Skill Maintenance

When updating this skill:

- Edit the working skill source first.
- Sync the same content into the installed local skill at `~/.codex/skills/issue-generator`.
- Sync the same content into the GitHub source repository, expected to be `hy0909/skills`.
- Commit and push the skill update whenever possible.
- If validation cannot run because a local dependency is missing, say so and still verify file contents directly.
