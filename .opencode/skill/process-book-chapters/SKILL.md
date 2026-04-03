---
name: process-book-chapters
description: Process pasted book chapters into chapter knowledge notes
---

## What I Do

I turn pasted chapter text into chapter knowledge notes, one file per chapter:

- `vault/books/{book-slug}/chapters/ch-{NN}.md`

Default behavior is no prior-vault lookup. I only search existing notes when explicitly requested (or `XCD`).

## When to Use Me

Use when the user says:
- "Process chapter {N} from {Book Title}"
- "Create a chapter note from this text"
- "Turn this chapter into a knowledge note"

## Workflow

### Step 1: Parse Inputs

Collect:

- Book title
- Chapter number (if missing, infer from text or use next available)
- Chapter text

### Step 2: Build Chapter Path

Create/use:

- `vault/books/{book-slug}/chapters/ch-{NN}.md`

Use two-digit chapter numbers (for example: `ch-01.md`, `ch-12.md`).

### Step 3: Write Chapter Knowledge Note

Use this template:

```markdown
# {Book Title} - Chapter {NN}

> **Source:** {Book Title} by {Author if known}
> **Chapter:** {NN}
> **Processed:** {YYYY-MM-DD}

---

## Core Claim

{Main chapter claim in 1-3 sentences}

## Key Ideas

- **{Idea 1}:** {Explanation}
- **{Idea 2}:** {Explanation}

## Mechanisms and Models

- {How something works according to the chapter}

## Practical Takeaways

- {Actionable takeaway 1}
- {Actionable takeaway 2}

## Evidence and Examples

- {Important example or evidence}

## Open Questions

- {Question 1}
- {Question 2}

## Tags

#type/book-chapter #book/{book-slug}
```

### Step 4: Optional Backlinks/Related Notes

Only if explicitly requested (or `XCD`):

- Search vault/QMD for related notes
- Add `## Related Vault Notes` with selective links

### Step 5: Optional Index Rebuild

Run `./bin/index` only if explicitly requested.

## Quality Checklist

- [ ] Chapter note is under `vault/books/{book-slug}/chapters/ch-{NN}.md`
- [ ] Note captures knowledge from chapter, not just a generic summary
- [ ] Claims and takeaways are concrete
- [ ] No vault lookups unless explicitly requested
- [ ] Backlinks/connections added only when explicitly requested
