---
name: issue-generator
description: Create or update GitHub issues and sub-issues for SafeAI planning work. Use when the user asks to create, edit, move, transfer, or verify an issue/sub-issue, especially when repository routing, assignees, labels, issue type, project fields, priority, or start date matters: always prefer the matching `*-docs` repository for planning issues, and assign new issues to `hy0909` by default.
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
- Every document link in an issue body or comment points to the `main` branch (`.../blob/main/...`), never to a feature branch — branches are deleted after merge and the links die. When the linked file or change is not merged yet, add one line at the top or bottom of the body: `※ 문서 링크는 main 브랜치 기준이라 main 병합 후 열립니다.`
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
4. Draft the issue in Korean, matching the user's concise planning style. Use `main` paths for every repo link and add the `main 병합 후 열립니다` line when the target is unmerged.
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
7. Create or edit the issue with `gh issue create` or `gh issue edit`.
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
