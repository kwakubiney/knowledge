#!/usr/bin/env python3
"""
Concept Index Builder
Scans vault and builds concept_index.json for fast lookups
"""
import json
import re
from pathlib import Path


def get_vault_path() -> Path:
    """Get vault path from config."""
    config_path = Path(__file__).parent.parent / "config.json"
    if config_path.exists():
        config = json.loads(config_path.read_text())
        return Path(config.get("vault_path", "~/Documents/knowledge-vault")).expanduser()
    return Path("~/Documents/knowledge-vault").expanduser()


def normalize(name: str) -> str:
    """Normalize a concept name for matching."""
    return re.sub(r'[^\w\s-]', '', name.lower()).strip()


def scan_vault() -> dict:
    """Scan vault and extract all concepts."""
    vault_dir = get_vault_path()
    if not vault_dir.exists():
        print(f"Vault not found at {vault_dir}")
        return {}
    
    concepts = {}
    
    for md_file in vault_dir.rglob("*.md"):
        if md_file.name.startswith("_"):
            continue  # Skip context files
        
        rel_path = str(md_file.relative_to(vault_dir))
        content = md_file.read_text(encoding='utf-8', errors='ignore')
        
        # Extract note title
        title = md_file.stem
        normalized = normalize(title)
        if normalized and len(normalized) > 2:
            if normalized not in concepts:
                concepts[normalized] = {
                    "name": title,
                    "path": rel_path,
                    "type": "note",
                    "mentions": 1
                }
            else:
                concepts[normalized]["mentions"] += 1
        
        # Extract headings
        for match in re.finditer(r'^#{1,3}\s+(.+)$', content, re.MULTILINE):
            heading = match.group(1).strip()
            normalized = normalize(heading)
            if normalized and len(normalized) > 3 and normalized not in concepts:
                concepts[normalized] = {
                    "name": heading,
                    "path": rel_path,
                    "type": "heading",
                    "mentions": 1
                }
        
        # Extract wiki-links
        for match in re.finditer(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content):
            link = match.group(1).strip()
            normalized = normalize(link)
            if normalized and len(normalized) > 2:
                if normalized not in concepts:
                    concepts[normalized] = {
                        "name": link,
                        "path": "",
                        "type": "concept",
                        "mentions": 1
                    }
                else:
                    concepts[normalized]["mentions"] += 1
        
        # Extract tags
        for match in re.finditer(r'#([\w/-]+)', content):
            tag = match.group(1)
            normalized = normalize(tag.replace('/', '-'))
            if normalized and normalized not in concepts:
                concepts[normalized] = {
                    "name": f"#{tag}",
                    "path": rel_path,
                    "type": "tag",
                    "mentions": 1
                }
    
    return concepts


def main():
    vault_dir = get_vault_path()
    index_path = vault_dir / "concept_index.json"
    
    print(f"Scanning vault at {vault_dir}...")
    concepts = scan_vault()
    
    if not concepts:
        print("No concepts found.")
        return
    
    # Save index
    index_path.write_text(json.dumps(concepts, indent=2))
    print(f"Saved {len(concepts)} concepts to {index_path}")
    
    # Show summary
    by_type = {}
    for c in concepts.values():
        t = c["type"]
        by_type[t] = by_type.get(t, 0) + 1
    
    print("\nBreakdown:")
    for t, count in sorted(by_type.items()):
        print(f"  {t}: {count}")


if __name__ == "__main__":
    main()
