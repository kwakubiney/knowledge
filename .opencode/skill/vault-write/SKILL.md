---
name: vault-write
description: Standard format and conventions for writing vault notes
---

## What I Do

Define the standard format for all vault notes to ensure consistency:

1. **Frontmatter structure**
2. **Section ordering**
3. **Wiki-link conventions**
4. **Tag taxonomy**
5. **Backlink format**

## When to Use Me

Reference this when:
- Creating any new note
- Unsure about formatting conventions
- Need to standardize an existing note

## Note Types

### 1. Content Notes (Videos, Chapters, Highlights)

```markdown
# {Title}

> **Source:** {Source details with link if applicable}
> **Theme:** [[{Theme} - Index|{Theme}]]
> **Processed:** {YYYY-MM-DD}
> **Cross-Reference:** [[{Related Notes}]] (optional)

---

## Summary

{Content with [[wiki-links]] to concepts}

---

## Connections to Existing Knowledge

{Optional table or narrative connecting to other notes}

---

## Key Concepts

### {Concept Name}
{Definition}
**Connects to:** [[{related}]] (optional)

---

## Questions Raised

1. {Question}

---

## References

**Explicit:** {named references}
**Implicit:** {assumed knowledge}

---

## Tags

{tags}

---

**Backlinks:** [[{Theme} - Index]] | [[{Other Related}]] (optional)
```

### 2. Concept Notes

```markdown
---
aliases: [{alternate names}]
tags:
  - concept
  - {theme}
created: {YYYY-MM-DD}
---

# {Concept Name}

## Definition
{Clear definition}

## Why It Matters
{Significance}

## First Mentioned
[[{source note}]]

## Related Concepts
[[{concept 1}]] | [[{concept 2}]]

## Appearances
- [[{note where it appears}]]

## Notes
{Personal thoughts}
```

### 3. Context Files (`_context.md`)

```markdown
# {Theme/Book} - Context
**Created:** {date}
**Last Updated:** {date}

## About This Theme / Core Thesis
{Description}

## Foundational Concepts / Key Concepts
- **{Concept}**: {definition}

## Key Figures
- {Person} — [[{related note}]]

## Major Debates / Open Questions
- [ ] {question}

## Cross-References
[[{Other Theme}]]: {how they connect}

## Personal Notes
{Own synthesis}

## Evolution Log
- {date}: {what changed}
```

### 5. Project Ideas

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
- {Only if explicitly requested / XCD}

---
#type/project-idea #status/incubation
```

## Wiki-Link Conventions

| Type | Format | Example |
|------|--------|---------|
| Simple link | `[[Note Name]]` | `[[AlphaFold]]` |
| Aliased link | `[[Note Name\|Display Text]]` | `[[Neuroscience - Index\|Neuroscience]]` |
| Concept link | `[[Concepts/{Name}]]` or just `[[{Name}]]` | `[[Evolutionary Intelligence]]` |
| Theme index | `[[{Theme} - Index]]` | `[[AI - Index]]` |
| Project idea | `[[ideas/{slug}]]` | `[[ideas/ai-plant-tracker]]` |
| Book master | `[[{Book} - Master]]` | `[[Being Mortal - Master]]` |

## Tag Taxonomy

```
#domain/{theme}           - Primary domain (neuroscience, ai, medicine)
#subdomain/{subtopic}     - Specific area within domain
#concept/{concept}        - Key concept
#person/{name}            - Notable person
#type/{content-type}      - video, book, article, synthesis, project-idea
#status/{status}          - foundational, developing, speculative, incubation, active
#connection/{domains}     - Cross-domain bridge (ai-neuroscience)
```

## File Naming

| Type | Pattern | Example |
|------|---------|---------|
| Content note | `{Title}.md` | `Demis Hassabis - Natures Patterns.md` |
| Chapter | `books/{book-slug}/chapters/ch-{NN}.md` | `books/breakneck/chapters/ch-03.md` |
| Highlights | `books/{book-slug}/highlights/highlights.md` | `books/breakneck/highlights/highlights.md` |
| Concept | `{Concept Name}.md` | `Evolutionary Intelligence.md` |
| Project Idea | `ideas/{slug}.md` | `ideas/ai-plant-tracker.md` |
| Context | `_context.md` | `_context.md` |
| Questions | `_questions.md` | `_questions.md` |
| Index | `{Theme} - Index.md` | `Neuroscience - Index.md` |
| Master | `{Book} - Master.md` | `Being Mortal - Master.md` |

## Quality Standards

Every note should have:
- [ ] Clear structure for the note type
- [ ] Wiki-links/backlinks only when useful or explicitly requested
- [ ] Relevant tags
- [ ] Clear source attribution
- [ ] Date processed
- [ ] Optional semantic links only when requested or high-value

## Semantic Link Discovery

Use QMD for semantic link discovery only when explicitly requested (or when it clearly improves the note):

```bash
# Search using the note's key concepts
qmd search "key concept 1 concept 2" -n 10

# Or use the note title/summary
qmd search "title or summary text" -n 10
```

**Integration workflow (optional):**

1. **After drafting the note**, extract 3-5 key concepts
2. **Run semantic search** on selected concepts
3. **Review results** for links that materially improve understanding
4. **Add only high-signal wiki-links**
5. **Skip connection sections** when they add little value

**Example:**

When writing a note about "AI interpretability," run:
```bash
qmd search "AI interpretability understanding neural networks" -n 10
```

This might surface:
- `[[Anthropic - Mapping the Inner Workings of Claude]]`
- `[[Neuroscience/Concepts/Neural Decoding]]`
- `[[Demis Hassabis - Scaling and Innovation]]`

Add only the links that meaningfully improve the note.

## Concept Note Guidelines

**When to create a concept note:**
- A synthesis or deeper understanding emerges during discussion
- The idea cuts across multiple themes
- It's a reusable framework or mental model

**Structure:**
```markdown
---
aliases: []
tags:
  - concept
  - {theme}
created: {YYYY-MM-DD}
---

# {Concept Name}

## Definition
{Clear one-line definition}

## Why It Matters
{Why this concept is useful or important}

## Connects To
- [[{Existing Note 1}]]
- [[{Existing Note 2}]]
- [[{Existing Note 3}]]

## First Mentioned
[[{Source Note}]]

## Notes
{Your personal thoughts on this concept}

---
#concept/{slug} #domain/{theme}
```

## Project Idea Guidelines

**When to create a project idea:**
- A creative spark emerges (from research or just a random thought)
- You identify a "gap" that could be filled by a project
- You want to apply a concept to a real-world problem

**Shared responsibility:**
- I (AI) create the initial draft when you say "I have an idea"
- You (user) refine the vision and next steps during review
