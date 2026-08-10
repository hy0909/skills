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
4. Draft the issue in Korean, matching the user's concise planning style.
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

## Skill Maintenance

When updating this skill:

- Edit the working skill source first.
- Sync the same content into the installed local skill at `~/.codex/skills/issue-generator`.
- Sync the same content into the GitHub source repository, expected to be `hy0909/skills`.
- Commit and push the skill update whenever possible.
- If validation cannot run because a local dependency is missing, say so and still verify file contents directly.
