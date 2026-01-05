# Knowledge Vault

AI-powered personal knowledge management using OpenCode skills.

## Vault Location
`~/Documents/knowledge-vault/`  
(configured in `config.json`)

## Usage

Just ask Claude:
- "Process this YouTube video: https://..."
- "Process my highlights from [Book Title]"
- "What connects X and Y in my vault?"

## Utilities

```bash
source venv/bin/activate

# Fetch YouTube transcript
python utils/fetch.py "https://youtube.com/..."

# Get book highlights
python utils/highlights.py "Book Title"

# Rebuild concept index
python utils/index.py
```

## Skills

Located in `.opencode/skill/`:
- `vault-context` — Load existing knowledge
- `process-youtube` — Video → note workflow
- `process-book` — Book → note workflow
- `synthesize-knowledge` — Cross-domain connections
- `vault-write` — Note formatting
