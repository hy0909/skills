---
name: pr-generator
description: Create GitHub pull requests for SafeAI work. Use when the user asks to create, open, draft, publish, or prepare a PR; before creating any PR, always mention the Assignees plan and ask for Assignees if the user did not specify them.
---

# PR Generator

## Overview

Use this skill for GitHub PR creation. It adds the user's required planning guardrail: PR creation must not proceed without an explicit Assignees decision.

## Core Rules

- Always use the authenticated GitHub account `hy0909` when running GitHub commands.
- Before creating any PR, explicitly mention the Assignees plan.
- If the user did not explicitly specify Assignees, stop and ask the user to provide Assignees. Do not create the PR until the user answers.
- If Assignees were already specified in the same request, state them back before creating the PR.
- If the user says FE/BE assignees, use FE `easyDong19` and BE `gurdl0525`.
- Default PRs to draft unless the user explicitly asks for ready-for-review.
- Never stage unrelated user changes silently.
- After creating or editing a PR, verify the PR URL, title, assignees, base branch, head branch, and draft state.
- Whenever this skill itself is modified, keep the installed local skill and GitHub source repository in sync, then commit and push the change.

## PR Creation Workflow

1. Confirm the repository and branch context.
2. Inspect `git status -sb` and relevant diffs before staging.
3. Confirm the intended PR scope if unrelated changes exist.
4. Handle Assignees before PR creation:
   - Always mention Assignees before creating.
   - If Assignees were not specified, ask the user to provide Assignees and do not create the PR yet.
   - If Assignees were specified, state the proposed Assignees back and proceed only when unambiguous.
5. Stage only intended files.
6. Commit with a concise message when changes are not already committed.
7. Push the branch.
8. Create a draft PR with the confirmed title, body, base branch, and Assignees.
9. Verify the PR metadata after creation.

## Metadata Defaults

- Assignees: must be user-confirmed or user-specified before PR creation.
- Reviewers: ask separately if the user requested reviewers but did not specify names.
- Labels: use user-requested labels; otherwise choose an appropriate existing label only when clearly applicable.
- Project fields: set only when repository/project context is available.

## Skill Maintenance

When updating this skill:

- Edit the working skill source first.
- Sync the same content into the installed local skill at `~/.codex/skills/pr-generator`.
- Sync the same content into the GitHub source repository, expected to be `hy0909/skills`.
- Commit and push the skill update whenever possible.
- If validation cannot run because a local dependency is missing, say so and still verify file contents directly.
