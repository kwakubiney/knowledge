---
name: process-book
description: Process book chapters or highlights into vault notes with full synthesis
---

## What I Do

Process book content (highlights from Apple Books or pasted chapters) into integrated vault notes:

1. **Extract content** — For Apple Books: `./bin/highlights "<Book Title>"`
2. **Load context** — Use `vault-context` skill
3. **Synthesize** — Create structured notes with cross-references
4. **Update context** — Enrich book and theme `_context.md` files
5. **Rebuild index** — Run `./bin/index`

## When to Use Me

When the user says:
- "Process highlights from {Book Title}"
- "Add this chapter to my vault"
- "I just finished reading {Book} — synthesize my highlights"

## Workflow

### Step 1: Get Content

**For Apple Books highlights:**
```bash
./bin/highlights "Book Title"
```

**For pasted content:**
User will paste the text directly.

### Step 2: Load Context

Before processing, understand:
- What theme does this book belong to?
- Is there existing context for this book?
- What concepts already exist in this domain?
- What open questions might this content address?

### Step 3: Create/Update Book Context

If this is the first content from a book, create `vault/{Theme}/{Book}/_context.md`:

```markdown
# {Book Title} - Context
**Author:** {Author}
**Theme:** [[{Theme} - Index|{Theme}]]
**Started:** {date}
**Last Updated:** {date}

## Core Thesis
{The main argument of the book, synthesized from content}

## Key Concepts
{Concepts that keep appearing, with definitions}

## Recurring Themes
{Patterns across chapters/highlights}

## Open Questions
- [ ] {Questions the book raises or leaves unanswered}

## Connections to Other Work
| This Book | Related Work | Connection |
|-----------|--------------|------------|
| {concept} | [[{other note}]] | {how they relate} |

## Personal Notes
{User's own synthesis and reactions}

## Evolution Log
- {date}: {what was processed}
```

### Step 4: Create Content Note

**For highlights:**
```markdown
# {Book Title} - Highlights

> **Source:** {Book Title} by {Author}
> **Theme:** [[{Theme} - Index|{Theme}]]
> **Processed:** {date}

---

## Key Highlights

### {Thematic Group 1}

> "{Highlight text}"
> — Chapter {N}

{My synthesis: what this means, how it connects to [[existing concept]]}

---

## Synthesis

{Overall synthesis of highlights with rich cross-references}

---

## Concepts Discovered

### {New Concept}
**Definition:** {from the book}
**Connects to:** [[{existing concept}]]
```

**For chapters:**
```markdown
# {Book Title} - Chapter {N}

> **Source:** {Book Title} by {Author} | Chapter {N}
> **Theme:** [[{Theme} - Index|{Theme}]]

---

## Summary
{Chapter summary with cross-references}

## Key Arguments
{Main points with connections}

## Questions Raised
{Questions for later chapters or other books}
```

### Step 5: Update Context Files

1. **Book context** — Add new concepts, update thesis understanding
2. **Theme context** — Add cross-references if new connections found
3. **Evolution log** — Record what was processed

### Step 6: Rebuild Index
```bash
./bin/index
```

## Quality Checklist

- [ ] Core thesis captured (for books with enough content)
- [ ] Cross-references to at least 2 existing notes
- [ ] Book context file created/updated
- [ ] Theme context updated if new connections found
- [ ] Open questions captured
