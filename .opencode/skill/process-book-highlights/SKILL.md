---
name: process-book-highlights
description: Process Apple Books highlights into a single per-book highlights note
---

## What I Do

I process Apple Books highlights into one canonical file per book:

- `vault/books/{book-slug}/highlights/highlights.md`

Default behavior is local synthesis only. I do not look up prior vault notes unless explicitly requested (or `XCD`).

## When to Use Me

Use when the user says:
- "Process highlights from {Book Title}"
- "Track my highlights for {Book Title}"
- "Update the highlights file for {Book Title}"

## Workflow

### Step 1: Extract Highlights

Run:

```bash
./bin/highlights "{Book Title}"
```

### Step 2: Build Book Path

Create/use:

- `vault/books/{book-slug}/highlights/highlights.md`

`{book-slug}` should be lowercase kebab-case from the book title.

### Step 3: Write or Update Highlights Note

Use this template:

```markdown
# {Book Title} - Highlights

> **Source:** {Book Title} by {Author}
> **Updated:** {YYYY-MM-DD}

---

## Highlight Log

### Highlight {N}
> "{Highlight text}"
> — {Chapter or location if available}

{Optional short synthesis for this highlight}

---

## Patterns So Far

- {Repeated idea 1}
- {Repeated idea 2}

## Open Questions

- {Question 1}
- {Question 2}

## Tags

#type/book-highlights #book/{book-slug}
```

### Step 4: Optional Connections and Backlinks

Only if explicitly requested (or `XCD`):

- Search vault/QMD for related notes
- Add a short `## Related Vault Notes` section
- Add backlinks

### Step 5: Optional Index Rebuild

Run `./bin/index` only if explicitly requested.

## Quality Checklist

- [ ] Highlights file is under `vault/books/{book-slug}/highlights/highlights.md`
- [ ] Extracted highlights are preserved accurately
- [ ] Synthesis stays grounded in highlights
- [ ] No vault lookups unless explicitly requested
- [ ] Backlinks/connections added only when explicitly requested
