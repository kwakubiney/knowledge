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
4. **Cross-Domain Connections** — Check other themes' contexts for potential bridges

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
