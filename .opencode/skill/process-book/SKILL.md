---
name: process-book
description: Route book processing to highlights or chapters workflows
---

## What I Do

I route book work into the right workflow:

1. **Highlights flow** — Use `process-book-highlights` for Apple Books highlights
2. **Chapters flow** — Use `process-book-chapters` for pasted chapter text
3. **Respect lookup policy** — Do not query prior vault content unless explicitly requested (or `XCD`)

## When to Use Me

When the user says:
- "Process highlights from {Book Title}"
- "Add this chapter to my vault"
- "I just finished reading {Book} — synthesize my highlights"

## Workflow

### Step 1: Detect Input Type

- If input is Apple Books highlights, use `process-book-highlights`.
- If input is chapter text pasted by user, use `process-book-chapters`.

### Step 2: Choose Book Folder

Use a book-first path:

- `vault/books/{book-slug}/highlights/highlights.md`
- `vault/books/{book-slug}/chapters/ch-{NN}.md`
- Optional: `vault/books/{book-slug}/_context.md` (only when explicitly requested)

### Step 3: Respect Lookup and Backlink Rules

- Do not search previous notes by default.
- Only do vault/QMD lookups if explicitly requested (or `XCD`).
- Only add backlinks/connections when explicitly requested.

### Step 4: Optional Shared Context and Index

- If requested, create/update `vault/books/{book-slug}/_context.md`.
- If requested, run `./bin/index`.

## Delegation Notes

- For highlights, follow `.opencode/skill/process-book-highlights/SKILL.md`.
- For chapters, follow `.opencode/skill/process-book-chapters/SKILL.md`.

## Quality Checklist

- [ ] Correct flow chosen (highlights vs chapters)
- [ ] Files created under `vault/books/{book-slug}/...`
- [ ] No vault lookups unless explicitly requested
- [ ] Backlinks/connections added only when explicitly requested
