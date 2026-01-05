#!/usr/bin/env python3
"""
Git History Extractor
Extracts linear history from a repo for AI analysis
"""
import sys
import subprocess
import json
from pathlib import Path
from datetime import datetime


def run_git(repo_path: Path, args: list) -> str:
    """Run a git command in the repo."""
    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=repo_path,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Git error: {e.stderr}", file=sys.stderr)
        sys.exit(1)


def get_commits(repo_path: Path, since_date: str = None) -> list:
    """Get commits with stats."""
    
    # Format: hash|author|date|subject|body
    fmt = "%h|%an|%ad|%s|%b"
    args = ["log", f"--pretty=format:{fmt}__END_COMMIT__", "--date=short", "--reverse"]
    
    if since_date:
        args.append(f"--since={since_date}")
        
    raw = run_git(repo_path, args)
    
    commits = []
    for chunk in raw.split("__END_COMMIT__"):
        if not chunk.strip():
            continue
            
        parts = chunk.strip().split("|", 4)
        if len(parts) < 4:
            continue
            
        commit_hash = parts[0]
        author = parts[1]
        date = parts[2]
        subject = parts[3]
        body = parts[4].strip() if len(parts) > 4 else ""
        
        # Get stats (files changed)
        # Format: numstat gives inserted/deleted/filename
        try:
            stat_raw = run_git(repo_path, ["show", "--numstat", "--format=", commit_hash])
            stats = []
            for line in stat_raw.splitlines():
                if not line.strip(): continue
                parts = line.split("\t")
                if len(parts) >= 3:
                    stats.append(f"{parts[2]} (+{parts[0]}/-{parts[1]})")
            
            # Get diff (capped at 5000 chars to avoid exploding context)
            diff_raw = run_git(repo_path, ["show", "--format=", "--unified=0", commit_hash])
            if len(diff_raw) > 5000:
                diff_summary = diff_raw[:5000] + "\n...[diff truncated]..."
            else:
                diff_summary = diff_raw
                
        except Exception:
            stats = []
            diff_summary = "[Diff extraction failed]"
        
        commits.append({
            "hash": commit_hash,
            "author": author,
            "date": date,
            "message": f"{subject}\n{body}".strip(),
            "stats": stats,
            "diff": diff_summary
        })
        
    return commits


def resolve_repo_path(path_or_name: str) -> Path:
    """Resolve a repo path from a name (via config) or raw path."""
    # Try as raw path first
    path = Path(path_or_name).expanduser()
    if (path / ".git").exists():
        return path
        
    # Try looking up in config
    config_path = Path(__file__).parent.parent / "config.json"
    if config_path.exists():
        try:
            config = json.loads(config_path.read_text())
            repos = config.get("repos", {})
            if path_or_name in repos:
                return Path(repos[path_or_name]).expanduser()
        except Exception as e:
            print(f"Config error: {e}", file=sys.stderr)
            
    return path  # Return original to let validation fail


def main():
    if len(sys.argv) < 2:
        print("Usage: python git_extract.py <repo_name_or_path> [since_date]", file=sys.stderr)
        sys.exit(1)
        
    input_path = sys.argv[1]
    repo_path = resolve_repo_path(input_path)
    
    if not (repo_path / ".git").exists():
        print(f"Repo not found: {input_path}", file=sys.stderr)
        print(f"Resolved to: {repo_path}", file=sys.stderr)
        print("Check config.json 'repos' or provide absolute path.", file=sys.stderr)
        sys.exit(1)
        
    since_date = sys.argv[2] if len(sys.argv) > 2 else None
    
    commits = get_commits(repo_path, since_date)
    
    print(f"# Git History for {repo_path.name}")
    if since_date:
        print(f"Since: {since_date}")
    print(f"Total Commits: {len(commits)}\n")
    print("---")
    
    for c in commits:
        print(f"## {c['date']} | {c['author']} ({c['hash']})")
        print(f"**Message:** {c['message']}")
        
        if c['stats']:
            print("\n**Files Changed:**")
            for s in c['stats'][:10]:  # Limit to 10 files
                print(f"- {s}")
            if len(c['stats']) > 10:
                print(f"- ...and {len(c['stats'])-10} more")
                
        print("\n**Diff Summary:**")
        print("```diff")
        print(c['diff'])
        print("```")
        print("\n---\n")
