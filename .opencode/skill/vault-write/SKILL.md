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

### 4. Index Files (`{Theme} - Index.md`)

```markdown
# {Theme}

This is a collection of resources about **{Theme}**.

## Books
- [[{Book} - Master|{Book Title}]]

## Videos
- [[{Video Note}|{Video Title}]]

## Key Concepts
- [[{Concept}]]

## Cross-References
- [[{Other Theme} - Index|{Other Theme}]]: {connection}
```

## Wiki-Link Conventions

| Type | Format | Example |
|------|--------|---------|
| Simple link | `[[Note Name]]` | `[[AlphaFold]]` |
| Aliased link | `[[Note Name\|Display Text]]` | `[[Neuroscience - Index\|Neuroscience]]` |
| Concept link | `[[Concepts/{Name}]]` or just `[[{Name}]]` | `[[Evolutionary Intelligence]]` |
| Theme index | `[[{Theme} - Index]]` | `[[AI - Index]]` |
| Book master | `[[{Book} - Master]]` | `[[Being Mortal - Master]]` |

## Tag Taxonomy

```
#domain/{theme}           - Primary domain (neuroscience, ai, medicine)
#subdomain/{subtopic}     - Specific area within domain
#concept/{concept}        - Key concept
#person/{name}            - Notable person
#type/{content-type}      - video, book, article, synthesis
#status/{status}          - foundational, developing, speculative
#connection/{domains}     - Cross-domain bridge (ai-neuroscience)
```

## File Naming

| Type | Pattern | Example |
|------|---------|---------|
| Content note | `{Title}.md` | `Demis Hassabis - Natures Patterns.md` |
| Chapter | `{Book} - Chapter {N}.md` | `Being Mortal - Chapter 3.md` |
| Highlights | `{Book} - Highlights.md` | `Being Mortal - Highlights.md` |
| Concept | `{Concept Name}.md` | `Evolutionary Intelligence.md` |
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

**Shared responsibility:**
- I (AI) create stubs when processing content
- You (user) fill them in during review
