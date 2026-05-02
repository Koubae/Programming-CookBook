
## Plan Mode

- Always write plan mode suitable for markdown
- Store plans in `docs/plans/`
- Update plan as you work
- Request the name of the plan file when creating a new plan

### How to implement plans step by step

I want you to implement it strictly ONE POINT AT A TIME.
You'll see the plan's step in the header `## Plan Steps`, each step is a checklist item bulleted point like `- [ ] Step description` or `1. [ ] Step description`.

Rules:
1. First, read the plan file and summarize the checklist.
2. Find the first unchecked item.
3. Implement ONLY that item.
4. Do not start the next item.
5. After implementing the item:
   - update the plan file by marking that item as done
   - briefly summarize what changed
   - tell me what command I should run to verify it, or run the relevant test/build command if appropriate
6. Then STOP and wait for my confirmation before continuing.

Important:
- Do not batch multiple checklist items together.
- Do not “improve” unrelated architecture.
- Keep the implementation simple.

To move to the next step, you must update the plan file by marking the current step as done and summarize what changed.
To mark the step as done you must use the checkbox syntax like `- [x] Step description` or `1. [x] Step description`.
