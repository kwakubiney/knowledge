---
name: process-youtube
description: Process a YouTube video into a clean vault note
---

## What I Do

Process a YouTube video from URL to a structured vault note:

1. **Fetch transcript** — Run `./bin/fetch <url>`
2. **Load context (lightweight)** — Read only what is needed for accurate summary
3. **Analyze content** — Extract key ideas, claims, and concepts
4. **Write note** — Create clear markdown focused on the video itself
5. **Optional connections** — Add links only when explicitly requested or clearly high-value
6. **Optional updates** — Update context/index only when needed

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

Default behavior: do this without QMD unless explicitly requested.

Use QMD only when:
- The user explicitly asks for related notes/connections
- The user uses `XCD`

### Step 3: Analyze

As I analyze the content, prioritize:
- Main argument and key claims
- Supporting examples
- Practical takeaways
- Questions or caveats

### Step 3.5: Optional Connection Pass

Only if requested (or clearly useful), add a brief connection section that links to existing notes.

Do not force concept-note creation or cross-domain synthesis.

### Step 4: Write the Note

Use this template:

```markdown
# {Video Title}

> **Source:** {Channel} | [YouTube]({url})
> **Theme:** [[{Theme} - Index|{Theme}]]
> **Processed:** {date}

---

## Summary

{Rich summary of the video}

---

## Key Concepts

### 1. {Concept Name}
{Definition and why it matters}

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

## Optional Related Notes

- [[{Related Note}]]
```

### Step 5: Update Context

Add to `vault/{Theme}/_context.md`:
- New key figures mentioned
- New facts or viewpoints worth preserving
- Evolution log entry

Only do this if it adds clear value.

### Step 6: Rebuild Index
```bash
./bin/index
```

## Quality Checklist

Before finishing, verify:
- [ ] Summary accurately reflects the video
- [ ] Key concepts are clear and useful
- [ ] Open questions captured if relevant
- [ ] Connections added only if requested or clearly valuable
