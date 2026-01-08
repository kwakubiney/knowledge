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

## Usage

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
- `vault-context` — Load existing knowledge and connections.
- `update-context` — Capture breakthroughs and evolutions in a domain.
- `synthesize-knowledge` — Identify patterns and create bridge notes across domains.
- `process-youtube` — Transform video transcripts into vault notes.
- `process-book` — Transform highlights into structured chapter notes.
- `vault-write` — Ensures consistency in note formatting and tagging.
