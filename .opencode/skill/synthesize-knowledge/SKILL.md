---
name: synthesize-knowledge
description: Find and create connections between existing vault notes across domains
---

## What I Do

Analyze the vault to find cross-domain patterns and create synthesis:

1. **Scan themes** — Read multiple `_context.md` files
2. **Find patterns** — Identify concepts that span domains
3. **Create bridges** — Write notes connecting ideas
4. **Update contexts** — Add cross-references to both domains
5. **Answer questions** — Use the vault to answer user queries

## When to Use Me

When the user asks:
- "What connects {Theme A} and {Theme B}?"
- "Find patterns across my vault"
- "Create a synthesis of {Topic}"
- "What have I learned about {Concept}?"
- "Answer this using my notes: {Question}"

## Workflow

### Pattern Discovery with qmd

Use semantic search to discover connections that keyword matching would miss:

```bash
# Search for conceptually related notes
qmd search "key concept from note" -n 10

# Get results as JSON for systematic processing
qmd search "concept" --json -n 15 --min-score 0.3
```

**Discovery workflow:**

1. **Read all theme contexts** — `vault/*/_context.md`
2. **Extract key concepts** from each theme
3. **Run cross-domain semantic searches**:
   ```bash
   # Find AI concepts that relate to neuroscience
   qmd search "brain learning neural patterns" -n 10
   
   # Find neuroscience concepts that relate to AI
   qmd search "artificial neural network intelligence" -n 10
   ```
4. **Compare foundational concepts** — Look for:
   - Same concept, different names (synonyms)
   - Same person mentioned in multiple domains
   - Complementary ideas (one explains the other)
   - Contradictions (tension worth exploring)
5. **Check concept index** — `concept_index.json` for overlapping terms

### Finding Hidden Connections

qmd excels at finding connections you wouldn't notice manually:

```bash
# Take a key insight from one domain and search across all themes
qmd search "survival of the fittest optimization" -n 10

# The results might surface:
# - AI: "Evolution as optimization" from Hassabis notes
# - Neuroscience: "Brain as evolved optimizer"  
# - Drug Discovery: "Evolutionary algorithms for protein folding"
```

### Types of Connections

| Connection Type | Example | Action |
|-----------------|---------|--------|
| **Same concept, different lens** | "Generative model" in AI vs "Neocortex as simulator" in Neuroscience | Create bridge note |
| **Cause and effect** | Evolution → Intelligence → AI | Create synthesis note |
| **Contradiction** | One book says X, another says not-X | Create debate note |
| **Extends** | Book B builds on Book A's foundation | Add to context |
| **Answers** | New content answers old open question | Update question status |

### Creating Bridge Notes

When I find a significant cross-domain connection:

```markdown
# Bridge: {Concept} Across {Theme A} and {Theme B}

> **Type:** Synthesis
> **Themes:** [[{Theme A} - Index]], [[{Theme B} - Index]]
> **Created:** {date}

---

## The Connection

{Clear statement of how these domains relate}

## In {Theme A}

{How this concept appears in Theme A}
- [[{Note 1}]]: {relevant point}
- [[{Note 2}]]: {relevant point}

## In {Theme B}

{How this concept appears in Theme B}
- [[{Note 3}]]: {relevant point}
- [[{Note 4}]]: {relevant point}

## Synthesis

{What we learn by seeing both perspectives}

## Open Questions

- {Questions raised by this connection}

---

**Backlinks:** [[{Theme A} - Index]] | [[{Theme B} - Index]]
```

### Updating Contexts

After finding connections, update both themes' `_context.md`:
- Add to Cross-References section
- Add bridge note to relevant sections
- Update Evolution Log

## Answering Questions

When asked a question about the vault:

1. **Identify relevant themes** from the question
2. **Load those contexts**
3. **Find relevant notes** using concept index
4. **Read the notes** for specific information
5. **Synthesize answer** citing sources with `[[wiki-links]]`

Example response format:
```markdown
Based on your vault:

{Answer synthesized from multiple notes}

**Sources:**
- [[{Note 1}]]: {relevant point}
- [[{Note 2}]]: {relevant point}

**Open questions this raises:**
- {follow-up worth exploring}
```

## Quality Checklist

- [ ] Multiple themes consulted
- [ ] Connections are substantive (not superficial keyword matches)
- [ ] Bridge notes link back to source notes
- [ ] Context files updated with new cross-references
- [ ] User can trace the reasoning through wiki-links
