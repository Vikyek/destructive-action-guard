---
name: destructive-action-guard
description: >-
  STOP AND VERIFY before any irreversible or high-blast-radius action. Halts
  execution, summarizes exact blast radius, and requires explicit typed target
  confirmation (exact repo, branch, path, or package name) before running
  `gh repo delete`, `git push --force`, `git filter-repo`, `git reset --hard`,
  `rm -rf`, `paru -Rns` on system/core packages, or dropping databases/buckets.
  Do NOT use for routine non-destructive reads, tests, or normal commits.
version: 1.0.0
summary: >-
  Pre-execution safety gate requiring impact summary and typed target
  confirmation before irreversible Git, GitHub, filesystem, or system commands.
tags:
  - security
  - agents-orchestration
  - devops-cloud
keywords:
  - guardrail
  - confirmation
  - destructive
  - git-safety
  - repo-delete
  - force-push
  - data-loss
use_cases:
  - Preventing accidental GitHub repository deletions (`gh repo delete`)
  - Guarding force pushes (`git push --force`) and history rewrites (`git filter-repo`)
  - Requiring typed path confirmation before recursive deletes (`rm -rf`)
---

# Destructive Action Guard (`destructive-action-guard`)

Never execute irreversible or high-blast-radius commands on a vague "yes" or implicit assumption.

## Trigger Actions (Always Halt First)

Halt and require explicit typed target confirmation before running:
1. **GitHub / Remote Admin**: `gh repo delete`, `gh repo archive`, `gh api -X DELETE` on repos/environments/secrets, deleting release tags or protected branches.
2. **Git History / Destructive Reset**: `git push --force` (or `--force-with-lease` on shared/default branches), `git filter-repo`, `git reset --hard` with uncommitted changes, `git clean -fdx`, `git branch -D` on unmerged work.
3. **Filesystem**: `rm -rf` on project roots, `~/.gemini`, `~/.config`, `/etc`, `/boot`, or wildcard globs.
4. **System / Packages / Data**: `paru -Rns` / `pacman -Rdd` on core/desktop packages, `mkfs`, `dd`, `DROP TABLE/DATABASE`, `TRUNCATE`, cloud bucket/project deletion.

## Mandatory 3-Step Gate

1. **Halt Execution**: Do **not** run the destructive command yet. Inspect read-only state first (e.g., `git status`, `git log --oneline -5`, target size/count) so the impact summary is exact.
2. **Present Impact Summary**:
   - **Exact command** that will run
   - **Target** (exact repo slug, branch name, or absolute path)
   - **What is permanently lost or overwritten** (unmerged commits, remote history, files, stars/issues)
   - **Backup / rollback option** (e.g., archive branch, `.bak`, `snapper` snapshot) if one exists
3. **Require Typed Confirmation**:
   Ask the user to reply with the **exact target identifier** (e.g. `CONFIRM DELETE Vikyek/repo-name` or the exact branch/path name) before executing. A generic "ok" or "go ahead" from an earlier turn does **not** authorize a newly discovered destructive target.

## Exceptions

- Temporary build caches or scratch artifacts created inside the current session (e.g., `/tmp/*`, `__pycache__`, `.pytest_cache`).
- Routine `git push` (fast-forward) or deleting an already-merged feature branch when no commits are lost.
