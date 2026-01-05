---
name: process-repo
description: Analyze a git repository to build a narrative project evolution log
---

## What I Do

I turn dry git history into a "Project Biography". I define the story of "how we got here".

1. **Extract History** — Run `./bin/git-extract <path> [since_date]`
2. **Cluster & Synthesize** — Group commits into meaningful "chapters" (Features/Refactors)
3. **Identify Contributors** — Credit the people behind the changes
4. **Update Context** — Write to `vault/Hubtel/{Project}/_context.md`

## When to Use Me

- "Create a context for the payment-gateway repo"
- "Update the evolution log for consumer-app"
- "Who built the fraud engine and why?"

## Workflow

### Step 1: Get History
```bash
./bin/git-extract "repo-name" "YYYY-MM-DD"
```
I can use the **repo name** defined in `config.json` (e.g., "payment-gateway") OR a full path.
If updating existing context, find the last date in `_context.md` and use that.

### Step 2: Analyze Clusters
Look for patterns in the log:
- **Big Features:** Multiple commits over days/weeks by same authors on related files.
- **Refactors:** usage of "refactor", "cleanup", "migration".
- **Fixes:** "fix", "bug", "hotfix" clusters indicating instability.

### Step 3: Write/Update Context (`vault/Hubtel/{Project}/_context.md`)

If creating new:
```markdown
# {Project Name} - Master Context
**Repository:** {path}
**Last Updated:** {date}

## Core Purpose
{Synthesized from README or initial commits}

## Architecture
{Inferred from code structure/commits}

## Key Contributors
- **{Name}**: {Role/Area of focus based on commits}

## Evolution Log
*(The Story of the Code)*

### v{X}: {Major Milestone Title} ({Date Range})
**Driver:** {Why was this done?}
**The Change:** {Summary of what changed}
**Key Decisions:** {Inferred trade-offs}
**Contributors:** {Names}

...
```

If updating:
- Append new "chapters" to the **Evolution Log**.
- Update **Key Contributors** if new people appeared.
- Update **Last Updated** date.

## Quality Checklist
- [ ] Grouped trivial commits (typos) into larger narratives
- [ ] Identified the "Driver" (why did this happen?)
- [ ] Credited specific authors
- [ ] Kept the tone narrative ("We moved to Kafka") vs mechanical ("Added KafkaConsumer.cs")
