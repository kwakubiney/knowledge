---
name: process-youtube
description: Process a YouTube video into vault notes with intelligent cross-references
---

## What I Do

Process a YouTube video from URL to fully integrated vault note:

1. **Fetch transcript** — Run `python utils/fetch.py <url>`
2. **Load context** — Use `vault-context` skill to understand existing knowledge
3. **Analyze content** — Extract key ideas, claims, and concepts
4. **Find connections** — Link to existing notes, concepts, and themes
5. **Write note** — Create structured markdown with cross-references
6. **Update context** — Add to theme's `_context.md`
7. **Rebuild index** — Run `python utils/index.py`

## When to Use Me

When the user says:
- "Process this YouTube video: <url>"
- "Add this video to my vault: <url>"
- "Watch and summarize: <url>"

## Workflow

### Step 1: Get Transcript
```bash
python utils/fetch.py "https://youtube.com/watch?v=VIDEO_ID"
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
python utils/index.py
```

## Quality Checklist

Before finishing, verify:
- [ ] At least 3 cross-references to existing notes
- [ ] Theme context was read and used
- [ ] New concepts linked to existing ones
- [ ] Open questions addressed if relevant
- [ ] Context file updated with new connections
