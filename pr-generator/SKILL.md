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

## Skill Maintenance

When updating this skill:

- Edit the working skill source first.
- Sync the same content into the installed local skill at `~/.codex/skills/pr-generator`.
- Sync the same content into the GitHub source repository, expected to be `hy0909/skills`.
- Commit and push the skill update whenever possible.
- If validation cannot run because a local dependency is missing, say so and still verify file contents directly.
