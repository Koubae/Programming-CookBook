AI & Machine Learning | Development Environment
===============================================

* Commands: [ai_dev_commands.bash](./ai_dev_commands.bash)


* [forrestchang's Karpathy-Inspired Claude Code Guidelines](https://github.com/forrestchang/andrej-karpathy-skills/tree/main)
* [forrestchang/andrej-karpathy-skills -- CLAUDE.md](https://github.com/forrestchang/andrej-karpathy-skills/blob/main/CLAUDE.md)


Claude
------

#### Features

- `CLAUDE.md`
- Skills | https://code.claude.com/docs/en/skills
- MCP Serviers
- Subagents | https://code.claude.com/docs/en/sub-agents
- Hooks | https://code.claude.com/docs/en/hooks

you might use :

> - CLAUDE.md for project conventions
> - Skill for your deployment workflow
> - MCP to connect to your database
> - Hook to run linting after every edit. 

Each feature handles what it’s best at

### Claude Code

* [Quickstart](https://code.claude.com/docs/en/quickstart)
* [Advanced setup](https://code.claude.com/docs/en/setup)
* [Authentication](https://code.claude.com/docs/en/authentication)
* [common workflows](https://code.claude.com/docs/en/common-workflows)
* [Extend Claude Code](https://code.claude.com/docs/en/features-overview)

* [auto memory](https://code.claude.com/docs/en/memory#auto-memory)
* [Work effectively with Claude Code](https://code.claude.com/docs/en/how-claude-code-works#work-effectively-with-claude-code)

* [Model configuration](https://code.claude.com/docs/en/model-config)
* [Resume Previous conversations](https://code.claude.com/docs/en/common-workflows#resume-previous-conversations)
* [Run parallel Claude Code sessions with Git worktrees](https://code.claude.com/docs/en/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees)

* [Build your setup over time](https://code.claude.com/docs/en/features-overview#build-your-setup-over-time)

* [Hook Events](https://code.claude.com/docs/en/hooks#hook-events)
* [How CLAUDE.md files load](https://code.claude.com/docs/en/memory#how-claude-md-files-load)
* [Understand context costs](https://code.claude.com/docs/en/features-overview#understand-context-costs)
* [Configure thinking mode](https://code.claude.com/docs/en/common-workflows#configure-thinking-mode)
* [Find bugs with ultrareview](https://code.claude.com/docs/en/ultrareview#find-bugs-with-ultrareview)

Add `ultrathink` anywhere in your prompt,  
Adds an in-context instruction telling the model to reason more on that turn.

### API Console -- Claude Platform 

* [Claude Platform Docs](https://platform.claude.com/docs/en/home)
* [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
* [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)


* [Difference between claud.ai vs platform.claude.com](https://stackoverflow.com/questions/79898270/difference-between-claud-ai-vs-platform-claude-com)
* [What’s the difference between Claude and Claude Code](https://www.reddit.com/r/ClaudeAI/comments/1s28mnc/whats_the_difference_between_claude_and_claude/)


#### Claude's file index

see [Explore the .claude directory](https://code.claude.com/docs/en/claude-directory)

- `CLAUDE.md`: ...
- `CLAUDE.local.md`: ...
- `MEMORY..md`: ...
- `.claude/rules/`: https://code.claude.com/docs/en/memory#organize-rules-with-claude/rules/

* [Combine features](https://code.claude.com/docs/en/features-overview#combine-features)

`_claudeMdExcludes_`
- https://code.claude.com/docs/en/memory#exclude-specific-claude-md-files

```json
{
  "claudeMdExcludes": [
    "**/monorepo/CLAUDE.md",
    "/home/user/monorepo/other-team/.claude/rules/**"
  ]
}
```

Comments on `md` files, Block-level HTML comments won't load into context:

```markdown
- rule 1
<!-- maintainer notes -->
- rule 2
```

- `--add-dir`: this flag gives Claude access to additional directories outside your main working directory. 
  By default, CLAUDE.md files from these directories are not loaded.

or To also load memory files from additional directories use this env var:

```bash
CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1 claude --add-dir ../shared-config
``` 

> This loads `CLAUDE.md`, `.claude/CLAUDE.md`, `.claude/rules/*.md`, and `CLAUDE.local.md` from the additional directory. 
> `CLAUDE.local.md` is skipped if you exclude local from `--setting-sources`.


#### Claude Context & Token Management


* [Understand context costs](https://code.claude.com/docs/en/features-overview#understand-context-costs)
* [Reduce token usage](https://code.claude.com/docs/en/costs#reduce-token-usage)


### Shortcuts

- Esc twice to rewind to a previous state of a file change
- Press Shift+Tab to cycle through permission modes:
- CTRL+G: Open & Edit plan

### Claude's Skills

- Manual Skills: `Set disable-model-invocation: true` in a skill’s frontmatter 
  this hides it from Claude entirely until you invoke it manually. 
  This reduces context cost to zero for skills you only trigger yourself.
- **bundled skills:** [commands](https://code.claude.com/docs/en/commands)

Misc
----

* [No way this actually works](https://www.youtube.com/watch?v=L29q2LRiMRc)
* [juliusbrussee/caveman](https://github.com/juliusbrussee/caveman)


Videos
------


* [Why You Need Plan Mode in Claude Code (Pro Tips)](https://www.youtube.com/watch?v=FoRIj5qcslg)
* [How I Use Claude Code Plan Mode: 3 Examples](https://www.youtube.com/watch?v=altX5elI-1k)


For this I want you to ultrathink

- Main feature: Basic chat terminal application with username and a unique "channel", message broadcast 

1. client should have a unique "name" we can start with user-uuid string (trimmed to 10 chars) 
2. client must listen to messages and write to stdout where are from and msg content 
3. cliet but accept input from stdin and write message once press Enter, a client is a chat terminal for now. 
4. The server must wait for the client "hello" to load its username. the From is the username, UserConnection also has now a "remote" field which is  conn.RemoteAddr().String()

