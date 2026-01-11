# Knowledge Vault

AI-powered personal knowledge management using OpenCode skills.

## Core Philosophy
The Knowledge Vault is designed to capture the **intellectual evolution** of various domains. Unlike traditional note-taking, it focuses on identifying **concepts** and their connections across different themes (Neuroscience, AI, Medicine, etc.).

## Setup

### 1. Requirements
- macOS (required for Apple Books integration)
- Python 3.10+
- Anthropic Claude (via OpenCode)

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/kwakubiney/knowledge.git
cd knowledge

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration
Copy `config.example.json` to `config.json` and set your vault path:
```json
{
    "vault_path": "~/Documents/knowledge-vault"
}
```

### 4. Semantic Search (qmd)
For AI-powered semantic search across your vault:
```bash
# Install bun (if not installed)
brew install oven-sh/bun/bun

# Install qmd globally
bun install -g https://github.com/tobi/qmd

# Create collection for your vault
qmd collection add ~/Documents/knowledge-vault --name vault --mask "**/*.md"

# Add context description
qmd context add qmd://vault "Personal knowledge vault"

# Generate vector embeddings (downloads ~1.6GB of local models on first run)
qmd embed
```

## Usage

### Semantic Search
```bash
# Keyword search (fast, BM25)
qmd search "neural plasticity" -n 10

# Or use the helper script
./bin/qmd-search "neural plasticity"

# Find connections you wouldn't notice manually
./bin/qmd-search "brain learning patterns" -n 10
```

### Concept-Driven Workflow
Just ask Claude:
- "What connects Neuroscience and AI in my vault?"
- "I just had a breakthrough about [Topic], update my context."
- "Process this YouTube video: [URL]"
- "Extract my highlights from [Book Title]"

### Command Line Tools
```bash
# Fetch YouTube transcript
./bin/fetch "[URL]"

# List books with highlights (macOS Apple Books)
./bin/highlights list

# Get highlights for a specific book
./bin/highlights "[Book Title]"

# Rebuild concept index for fast lookup
./bin/index
```

## Skills
Located in `.opencode/skill/`:
- `vault-context` — Load existing knowledge and connections (enhanced with qmd search).
- `update-context` — Capture breakthroughs and evolutions in a domain.
- `synthesize-knowledge` — Identify patterns and create bridge notes across domains (uses qmd for discovery).
- `process-youtube` — Transform video transcripts into vault notes.
- `process-book` — Transform highlights into structured chapter notes.
- `vault-write` — Ensures consistency in note formatting and tagging (includes semantic link suggestions).

## qmd Integration

[qmd](https://github.com/tobi/qmd) provides local semantic search using:
- **BM25** full-text search
- **Vector embeddings** for conceptual similarity
- **LLM re-ranking** for best results

### How Skills Use qmd

**Before processing new content:**
```bash
# Find related notes to provide context
qmd search "key concepts from new content" -n 10
```

**When writing notes:**
```bash
# Discover non-obvious connections to add as wiki-links
qmd search "note concepts" -n 10
```

**For cross-domain synthesis:**
```bash
# Find hidden connections across themes
qmd search "AI neural network learning" -n 15 --json
```

### Keeping the Index Fresh
```bash
# Re-index after adding new notes
qmd update && qmd embed

# Or use the helper
./bin/qmd-search --update
```
