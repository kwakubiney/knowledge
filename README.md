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

## Skills

Located in `.opencode/skill/`:
- `vault-context` — Load existing knowledge
- `process-youtube` — Video → note workflow
- `process-book` — Book → note workflow
- `synthesize-knowledge` — Cross-domain connections
- `vault-write` — Note formatting
