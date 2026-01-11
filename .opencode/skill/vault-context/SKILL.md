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
4. **Semantic Discovery** — Use `qmd` to find semantically related notes
5. **Cross-Domain Connections** — Check other themes' contexts for potential bridges

## Semantic Search with qmd Tools

The vault is indexed by `qmd`, a local semantic search engine. Use the following MCP tools for direct, efficient access to the vault:

- **qmd_search** — Fast BM25 keyword search.
- **qmd_vsearch** — Semantic vector search (conceptual similarity).
- **qmd_query** — Hybrid search with re-ranking (highest quality, recommended).
- **qmd_get** — Retrieve full content of a specific note/document.
- **qmd_multi_get** — Retrieve multiple documents matching a glob pattern.

### Automatic Tool Selection

You should use these tools automatically whenever:
1. The user asks about their personal notes, highlights, or previous research.
2. You need to verify if a concept already exists before creating a new note.
3. You are looking for semantic bridges between themes.

### Example Tool Use

```typescript
// For most general queries, use hybrid search:
qmd_query({ query: "neural plasticity mechanisms" })

// To get the full content of a specific note found in search:
qmd_get({ file: "Neuroscience/plasticity-basics.md" })
```

### Using qmd Tools Before Processing Content

**Before processing ANY new content** (YouTube videos, books, etc.), always extract 2-3 key concepts and search the vault using `qmd_query`:

```typescript
// Example: Before processing a video about "AI safety and alignment"
qmd_query({ query: "AI safety alignment", limit: 10 })
```

This ensures you have the full context of what already exists in the vault.

### Workflow Enhancement

1. **Extract concepts** from the new content (title, key terms)
2. **Run semantic search** to find existing related notes
3. **Read the top 3-5 results** to understand existing context
4. **Process the content** with awareness of what already exists
5. **Create explicit links** to the discovered related notes

## When to Use Me

**ALWAYS** use this skill before:
- Processing a YouTube video
- Processing book highlights/chapters
- Creating synthesis notes
- Answering questions about the vault

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
- Me (the AI) - when processing content, I must either link to an existing concept OR create a stub

**Shared responsibility:** I create stubs, you fill them in during review.
