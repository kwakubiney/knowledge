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
> **Cross-Reference:** [[{Related Notes}]]

---

## Summary

{Content with [[wiki-links]] to concepts}

---

## Connections to Existing Knowledge

{Table or narrative connecting to other notes}

---

## Key Concepts

### {Concept Name}
{Definition}
**Connects to:** [[{related}]]

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

**Backlinks:** [[{Theme} - Index]] | [[{Other Related}]]
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
# {Project Title}

> **Status:** #status/incubation
> **Themes:** [[{Theme} - Index]] (optional)
> **Created:** {YYYY-MM-DD}
> **Cross-Reference:** [[{Related Concepts}]] (optional)

---

## The Vision
{What is this project about? What problem does it solve?}

---

## Connection to Knowledge
{How does this project relate to concepts in the vault?}

---

## Next Steps
- [ ] {Task 1}
- [ ] {Task 2}

---

## References
{Links to source material or inspiration}

---

## Tags
#type/project-idea #status/incubation #domain/{theme}
```

## Wiki-Link Conventions

| Type | Format | Example |
|------|--------|---------|
| Simple link | `[[Note Name]]` | `[[AlphaFold]]` |
| Aliased link | `[[Note Name\|Display Text]]` | `[[Neuroscience - Index\|Neuroscience]]` |
| Concept link | `[[Concepts/{Name}]]` or just `[[{Name}]]` | `[[Evolutionary Intelligence]]` |
| Theme index | `[[{Theme} - Index]]` | `[[AI - Index]]` |
| Project idea | `[[Projects/{Name}]]` | `[[Projects/AI Plant Tracker]]` |
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
| Chapter | `{Book} - Chapter {N}.md` | `Being Mortal - Chapter 3.md` |
| Highlights | `{Book} - Highlights.md` | `Being Mortal - Highlights.md` |
| Concept | `{Concept Name}.md` | `Evolutionary Intelligence.md` |
| Project Idea | `Projects/{Title}.md` | `Projects/AI Plant Tracker.md` |
| Context | `_context.md` | `_context.md` |
| Questions | `_questions.md` | `_questions.md` |
| Index | `{Theme} - Index.md` | `Neuroscience - Index.md` |
| Master | `{Book} - Master.md` | `Being Mortal - Master.md` |

## Quality Standards

Every note should have:
- [ ] At least one wiki-link to existing content
- [ ] Proper theme backlink
- [ ] Relevant tags
- [ ] Clear source attribution
- [ ] Date processed
- [ ] **Semantic link suggestions checked** (see below)

## Semantic Link Discovery

Before finalizing any note, use qmd to discover non-obvious connections:

```bash
# Search using the note's key concepts
qmd search "key concept 1 concept 2" -n 10

# Or use the note title/summary
qmd search "title or summary text" -n 10
```

**Integration workflow:**

1. **After drafting the note**, extract 3-5 key concepts
2. **Run semantic search** on each concept
3. **Review results** for notes that should be linked
4. **Add wiki-links** to discovered connections
5. **Update the "Connections to Existing Knowledge" section** with findings

**Example:**

When writing a note about "AI interpretability," run:
```bash
qmd search "AI interpretability understanding neural networks" -n 10
```

This might surface:
- `[[Anthropic - Mapping the Inner Workings of Claude]]`
- `[[Neuroscience/Concepts/Neural Decoding]]`
- `[[Demis Hassabis - Scaling and Innovation]]`

Add these as explicit connections in the note.

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
