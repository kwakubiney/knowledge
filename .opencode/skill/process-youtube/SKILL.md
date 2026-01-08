---
name: process-youtube
description: Process a YouTube video into vault notes with intelligent cross-references
---

## What I Do

Process a YouTube video from URL to fully integrated vault note:

1. **Fetch transcript** — Run `./bin/fetch <url>`
2. **Load context** — Use `vault-context` skill to understand existing knowledge
3. **Analyze content** — Extract key ideas, claims, and concepts
4. **Find connections** — Link to existing notes, concepts, and themes
5. **Write note** — Create structured markdown with cross-references
6. **Update context** — Add to theme's `_context.md`
7. **Rebuild index** — Run `./bin/index`

## When to Use Me

When the user says:
- "Process this YouTube video: <url>"
- "Add this video to my vault: <url>"
- "Watch and summarize: <url>"

## Workflow

### Step 1: Get Transcript
```bash
./bin/fetch "https://youtube.com/watch?v=VIDEO_ID"
```
This outputs the transcript to stdout. Read it.

### Step 2: Load Context
Read the vault to understand what's already there:
- What themes might this video relate to?
- What concepts already exist?
- What open questions might this answer?

### Step 3: Analyze & Connect

As I analyze the content, actively look for:
- **Concepts that match existing notes** → Create `[[wiki-links]]`
- **Ideas that extend existing themes** → Note the extension
- **Answers to open questions** → Reference the question
- **New concepts worth tracking** → Flag for concept notes
- **Cross-domain connections** → The MOST valuable output

### Step 3.5: Synthesize Deeper Understanding (If Any)

After processing the content, review the conversation and notes. If we have arrived at a **synthesis or deeper understanding** about a topic that doesn't exist in the vault:

1. **Create a concept note** in `vault/{Theme}/Concepts/{Concept Name}.md`
2. **Include:**
   - A clear definition
   - Why it matters
   - Links to at least 2-3 relevant notes in the vault
   - Tags: `#concept/{slug}`

Example concept note structure:
```markdown
# {Concept Name}

## Definition
{One sentence definition}

## Why It Matters
{Why this concept is useful or important}

## Connects To
- [[{Existing Note 1}]]
- [[{Existing Note 2}]]
- [[{Existing Note 3}]]

---
#concept/{slug} #domain/{theme}
```

**When to create a concept note:**
- We explicitly discuss and synthesize an idea (e.g., "Simulation-Reality Gap")
- The idea cuts across multiple themes
- It's a framework or mental model worth reusing

### Step 4: Write the Note

Use this template:

```markdown
# {Video Title}

> **Source:** {Channel} | [YouTube]({url})
> **Theme:** [[{Theme} - Index|{Theme}]]
> **Processed:** {date}
> **Cross-Reference:** [[{Related Theme}]], [[{Related Note}]]

---

## Summary

{Rich summary with [[wiki-links]] to existing concepts}

---

## Connections to Existing Knowledge

| This Video Says | Existing Note Says | The Link |
|-----------------|-------------------|----------|
| {claim} | [[{note}]] | {how they connect} |

### Key Insight
> {The most important cross-domain connection discovered}

---

## Key Concepts

### 1. {Concept Name}
{Definition and why it matters}

**Connects to:** [[{existing concept}]], [[{other note}]]

---

## Questions Raised

1. {Question that connects to existing open questions or raises new ones}

---

## References

**Explicit:** {What the video mentions}
**Implicit:** {What it assumes}

---

## Tags

#domain/{theme} #concept/{concept} #person/{speaker} #type/video

---

**Backlinks:** [[{Theme} - Index]] | [[{Related Notes}]]
```

### Step 5: Update Context

Add to `vault/{Theme}/_context.md`:
- New key figures mentioned
- New cross-references discovered
- Evolution log entry

### Step 6: Rebuild Index
```bash
./bin/index
```

## Quality Checklist

Before finishing, verify:
- [ ] At least 3 cross-references to existing notes
- [ ] Theme context was read and used
- [ ] New concepts linked to existing ones
- [ ] Open questions addressed if relevant
- [ ] Context file updated with new connections
