---
name: implement-plan
description: Load a Markdown implementation plan from docs/plans/<plan-name>.md and implement it one unchecked task at a time.
arguments:
  - plan_file
disable-model-invocation: true
---

# Implement Plan

You are implementing a project plan from:

`docs/plans/$plan_file.md`

The user invoked this skill as:

`/implement-plan $plan_file`

## Your workflow

1. Read the plan file at `docs/plans/$plan_file.md`.
2. Treat that Markdown file as the source of truth.
3. Summarize the checklist briefly.
4. Find the first task to-do, written like:

  ```md
   - [ ] Task description
  ```

Where to find task:

Just below "Plan Steps" section in the plan file.

How to recognize to-do task:

- [ ] Task description
1. [ ] Task description

How makr taks as done:

- [x] Task description
1. [x] Task description
