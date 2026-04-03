---
name: vault-context
description: Load vault context, existing concepts, and open questions before processing any content
---

## Vault Location

The vault path is configured in `config.json` at the project root. Default: `~/Documents/knowledge-vault`

## What I Do

Before processing ANY new content into the knowledge vault, I load the relevant context:

1. **Theme Context** — Read `vault/{Theme}/_context.md` for the relevant domain
2. **Book Context** — If processing book content, read `vault/{Theme}/{Book}/_context.md`
3. **Concept Index** — Scan `concept_index.json` for existing concepts
4. **Optional Semantic Discovery** — Use `qmd` only when explicitly requested
5. **Optional Cross-Domain Check** — Only when needed for the task

## Semantic Search with qmd Tools

The vault is indexed by `qmd`, a local semantic search engine. Use the following MCP tools for direct, efficient access to the vault:

- **qmd_search** — Fast BM25 keyword search.
- **qmd_vsearch** — Semantic vector search (conceptual similarity).
- **qmd_query** — Hybrid search with re-ranking (highest quality, recommended).
- **qmd_get** — Retrieve full content of a specific note/document.
- **qmd_multi_get** — Retrieve multiple documents matching a glob pattern.

### Tool Selection Policy

Use QMD tools when:
1. The user explicitly asks to search the vault
2. The user asks what relates to the current topic
3. The user uses the `XCD` trigger

Otherwise, do not run QMD by default.

### Example Tool Use

```typescript
// For most general queries, use hybrid search:
qmd_query({ query: "neural plasticity mechanisms" })

// To get the full content of a specific note found in search:
qmd_get({ file: "Neuroscience/plasticity-basics.md" })
```

### Using qmd Tools (On Demand)

If QMD is requested, extract 2-3 key concepts and run a targeted `qmd_query`.

### Workflow Enhancement (When QMD Is Requested)

1. **Extract concepts** from the new content (title, key terms)
2. **Run semantic search** to find existing related notes
3. **Read the top 3-5 results** to understand existing context
4. **Process the content** with awareness of what already exists
5. **Create explicit links** to the discovered related notes

## When to Use Me

Use this skill before:
- Processing a YouTube video
- Processing book highlights/chapters
- Creating synthesis notes
- Answering questions about the vault

Keep context loading lightweight unless deeper discovery is requested.

## How to Use Me

1. **Identify the theme** (or let it be detected from content)
2. **Read the theme's `_context.md`** for:
   - Foundational concepts
   - Key figures
   - Major debates
   - Cross-references to other domains
3. **Check for related themes** that might connect
4. **Load open questions** from `_questions.md` if present

## Vault Structure

```
vault/
├── {Theme}/
│   ├── _context.md          # Theme-level context (ALWAYS read this)
│   ├── _questions.md        # Open questions for theme
│   ├── {Theme} - Index.md   # Index of all content in theme
│   ├── Concepts/            # Individual concept notes
│   │   └── {Concept}.md
│   └── {Book}/              # Book-specific folder
│       ├── _context.md      # Book-level context
│       ├── _questions.md    # Book-specific questions
│       └── {Book} - *.md    # Chapter/highlight notes
└── concept_index.json       # Fast lookup of all concepts
```

## Context File Format

Theme context files contain:
- **About This Theme** — Domain scope
- **Foundational Concepts** — Core ideas
- **Key Figures** — Important people
- **Major Debates** — Open questions in the field
- **Cross-References** — Links to other themes
- **Personal Notes** — User's own synthesis
- **Evolution Log** — History of updates

## Output

After loading context, I should be able to answer:
1. What concepts already exist in this domain?
2. What questions are still open?
3. What other domains might this connect to?
4. Who are the key figures already referenced?

## Concept Creation Protocol

When processing content, if we synthesize a **new deeper understanding** about a topic:

1. **Create** `vault/{Theme}/Concepts/{Concept Name}.md`
2. **Link** to 2-3 relevant existing notes
3. **Tag** with `#concept/{slug}` and `#domain/{theme}`

**Who creates concepts:**
- The user (you) - when you notice a cross-cutting idea
- Me (the AI) - only when explicitly requested or clearly useful
