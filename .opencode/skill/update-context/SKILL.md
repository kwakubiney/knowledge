---
name: update-context
description: Update vault context based on new concept discovery or deep discussion
---

## What I Do

I act as the "Project Biographer" triggered by active learning or discussion.
I capture the evolution of our understanding as we synthesize new information or reach a breakthrough.

## Triggers
- **New Concept Discovery:** We found a new topic or relationship.
- **Deep Discussion:** A conversation lead to a "shifting of the gears" in how we see a domain.
- **Synthesis:** A `synthesize-knowledge` run connected two previously separate areas.

## Inputs
- **Topic:** The domain or theme being updated.
- **Breakthrough:** What new thing did we learn or realize?
- **Impact:** How does this change our existing model of the domain?

## Workflow

### 1. Load Existing Context
Read `vault/{Theme}/_context.md`.

### 2. Identify the Shift
Ask: Does this new info...
- **Add a new dimension?** (A concept we hadn't considered)
- **Clarify a mystery?** (Answering a question from `_questions.md`)
- **Bridge domains?** (Connecting this theme to another)
- **Change the core thesis?** (Pivoting our understanding)

### 3. Update the Evolution Log
Append to the **Evolution Log** in `_context.md`:

```markdown
### {Date}: {Discovery Title}
**Discovery:** {Summary of the new understanding}
**Impact:** {How this changes our mental model of this theme}
**Source:** {e.g., "Discussion", "Bridge Note: [[Name]]", "Video: [[Name]]"}
```

### 4. Update Questions
Move answered questions from `_questions.md` to the **Personal Notes** or **Evolution Log** of the context.

---

## When to Use Me
- "Our understanding of {Theme} has changed. Update the context."
- "We just realized that {Concept A} is actually just a subset of {Concept B}."
- "This discussion on {Topic} was a breakthrough. Record it."
