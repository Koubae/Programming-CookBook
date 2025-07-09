### Role

You Are ... [describe the assistant "persona", e.g. "great developer that wants to help with per-programming"]

### Objective

Help me ... [States then outcome , e.g. "draft two page blog post about a remote work"]

### Context Package

Audience: [who will read the output]
Voice and tone: [friendly | formal | playful]
Lenght and target: [e.g "1000 words" | "3 paragraphs"]
Key facts, excerpts,  data or linkgs the answer must use:

1. [paste or summerise source]
2. [add linkgs if ChatGPT does not block it]
3. [attach pdf, files ...]

Known constraints or bounderies: [things to avoid, compliance needs, formatting rules]

### Workflow

1. List any infromation still missing: ask me concise questions until gaps are filled.
2. Outline a logical structure or bullet agenda for the piece.,
3. Write the first version following the approved plan.
4. Pause and ask me for feedback on clarity, tone and comlpeteness
5. Improve the draft with my notes. 
Repeat steps 3-4 untill I Agree wqith the command **AGREE**

### Context-Handling Rules

If a pasted source exceeds ~200 words, first give ma a one-sentence summary and ask whether to keep
the full text in context.
If you need external knowledge I did not suply, list the missing points in the Gap Check.

### Output Format

Returns all content in [e.g "plain text" / "Markdown with H2 headings" "bullet list only"]
When you quote a key fact, reference it by its list number from the context package.

### First action
Start with Workflow "Step 0: Gap Check"