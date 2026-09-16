---
name: pr-generator
description: Create GitHub pull requests for SafeAI work. Use when the user asks to create, open, draft, publish, or prepare a PR; assign PRs to `hy0909` by default and ask who should be requested as reviewer when reviewers were not specified.
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
- Document links in the PR body point to the `main` path (`.../blob/main/...`), never to the head branch — the branch is deleted after merge. Add one line at the top or bottom of the body: `※ 문서 링크는 main 브랜치 기준이라 병합 후 열립니다.` (the PR's own `Files changed` tab shows the content before merge).
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
8. Create a draft PR with the confirmed title, body, base branch, `hy0909` assignee, and confirmed reviewers.
9. Verify the PR metadata after creation.

## Metadata Defaults

- Assignees: always `hy0909`.
- Reviewers: always ask before PR creation if not specified.
- Labels: use user-requested labels; otherwise choose an appropriate existing label only when clearly applicable.
- Project fields: set only when repository/project context is available.

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
- Sync the same content into the installed local skill at `~/.codex/skills/pr-generator`.
- Sync the same content into the GitHub source repository, expected to be `hy0909/skills`.
- Commit and push the skill update whenever possible.
- If validation cannot run because a local dependency is missing, say so and still verify file contents directly.
