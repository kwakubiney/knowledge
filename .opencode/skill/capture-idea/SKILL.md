---
name: capture-idea
description: Quick capture and structured recording of new project sparks
---

## What I Do

I capture project ideas quickly and turn them into actionable notes.

I prioritize:
- Clear problem and outcome definition
- First concrete step to start execution
- Helpful assets from the vault only if they can directly help implementation

## Triggers

- "I have a new project idea"
- "Quick capture: {Idea}"
- "I just thought of something: {Idea}"
- "Add a project for {Topic}"

## Workflow

1.  **Acknowledge & Title** — Give the idea a concise, descriptive title.
2.  **Define the Vision** — Briefly summarize what the project is and why it matters now.
3.  **Clarify Execution** — Capture the first practical step and immediate constraints.
4.  **Find Helpful Assets (Optional)** — Only if explicitly requested (or user says `XCD`), use QMD to find notes, snippets, or references that can help execute the idea.
5.  **Create Note** — Write the idea to `vault/ideas/{slug}.md` using the template below.

## User Interaction Style

Be encouraging and execution-focused. When a user shares an idea:
- Ask: "What specific problem does this solve?"
- Ask: "What would a first shippable version look like?"
- Prompt: "What is the first step you can do in under 30 minutes?"

Do not force cross-references, backlinks, or concept links.

## Idea Note Template

```markdown
# {Idea Title}

## Problem
{What pain or gap this solves}

## Proposed Solution
{High-level approach}

## Why Now
{Why this is worth doing now}

## First Step
{The first concrete action}

## Constraints
{Time, tools, dependencies, risks}

## Helpful Vault Assets (Optional)
- {Only include if explicitly requested / XCD}

---
#type/project-idea #status/incubation
```

## Output Example

"Captured **AI-Powered Plant Care**!
- **Vision:** A tracker for plant growth using computer vision.
- **First Step:** Build a simple weekly photo upload flow.
- **Location:** `vault/ideas/ai-powered-plant-care.md`

Would you like me to break this into a one-week execution plan?"
