---
name: capture-idea
description: Quick capture and structured recording of new project sparks
---

## What I Do

I handle the initial capture of a project idea. I help you flesh out the "Vision" and can suggest connections to existing knowledge if they are relevant.

## Triggers

- "I have a new project idea"
- "Quick capture: {Idea}"
- "I just thought of something: {Idea}"
- "Add a project for {Topic}"

## Workflow

1.  **Acknowledge & Title** — Give the idea a concise, descriptive title.
2.  **Define the Vision** — Briefly summarize what the project is and why it's interesting.
3.  **Identify Connections (Optional)** — Scan the vault for relevant themes and concepts if applicable.
4.  **Create Note** — Use the template from `vault-write` to create `Projects/{Title}.md`.
5.  **Index Update** — Add the new project to `Projects/Projects - Index.md`.

## User Interaction Style

Be encouraging and proactive. When a user shares an idea:
- Ask: "What's the core problem this solves?"
- Suggest: "This seems related to [[{Concept}]]. Should I link it?"
- Prompt: "What's the very first step to get this moving?"

## Output Example

"Captured **AI-Powered Plant Care**!
- **Vision:** A tracker for plant growth using computer vision.
- **Connections:** Linked to [[Neural Networks]] and [[Natural System Learnability]].
- **Location:** `Projects/AI Plant Care.md`
- **Next Step:** Research OpenCV tutorials.

Would you like to add more details to the Vision or Next Steps?"
