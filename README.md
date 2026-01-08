# Knowledge Vault

AI-powered personal knowledge management using OpenCode skills.

## Vault Location
`~/Documents/knowledge-vault/`  
(configured in `config.json`)

## Usage

Just ask Claude:
- "Process this YouTube video: https://..."
- "Process my highlights from [Book Title]"
- "Create a context for the [Repo Name] repository"
- "What connects X and Y in my vault?"

## Utilities

```bash
# Fetch YouTube transcript
./bin/fetch "https://youtube.com/..."

# Get book highlights
./bin/highlights "Book Title"

# Rebuild concept index
./bin/index
```

## Live Context (Git Hooks)

Keep your project context up-to-date automatically as you work.

### 1. Install the hook
```bash
./bin/install-hook /path/to/your/project
```

### 2. Work normally
When you `git commit`, a context update is queued in `inbox/`.

### 3. Process updates
Ask Claude:
> "Check my inbox for updates"

Claude will read the pending commits and update the relevant `_context.md` files (Evolution Log, Architecture) if the changes are significant.

---

## Skills

Located in `.opencode/skill/`:
- `vault-context` — Load existing knowledge
- `process-youtube` — Video → note workflow
- `process-book` — Book → note workflow
- `synthesize-knowledge` — Cross-domain connections
- `vault-write` — Note formatting
