#!/usr/bin/env python3
"""
Apple Books Highlights Extractor
Minimal utility - just extracts highlights, Claude does the thinking
"""
import sys
import sqlite3
from pathlib import Path
from dataclasses import dataclass


# Apple Books database locations (macOS)
BOOKS_DB = Path.home() / "Library/Containers/com.apple.iBooksX/Data/Documents/BKLibrary/BKLibrary-1-091020131601.sqlite"
ANNOTATIONS_DB = Path.home() / "Library/Containers/com.apple.iBooksX/Data/Documents/AEAnnotation/AEAnnotation_v10312011_1727_local.sqlite"


@dataclass
class Highlight:
    text: str
    note: str
    chapter: str
    
    def __str__(self):
        result = f"> {self.text}"
        if self.note:
            result += f"\n\n**Note:** {self.note}"
        if self.chapter:
            result += f"\n\n— {self.chapter}"
        return result


def get_book_asset_id(book_title: str) -> str | None:
    """Find the asset ID for a book by title."""
    if not BOOKS_DB.exists():
        raise FileNotFoundError(f"Books database not found at {BOOKS_DB}")
    
    conn = sqlite3.connect(str(BOOKS_DB))
    cursor = conn.cursor()
    
    # Search for book by title (case-insensitive partial match)
    cursor.execute("""
        SELECT ZASSETID, ZTITLE, ZAUTHOR 
        FROM ZBKLIBRARYASSET 
        WHERE ZTITLE LIKE ?
    """, (f"%{book_title}%",))
    
    results = cursor.fetchall()
    conn.close()
    
    if not results:
        return None
    
    # Return first match
    return results[0][0]


def get_highlights(asset_id: str) -> list[Highlight]:
    """Get all highlights for a book."""
    if not ANNOTATIONS_DB.exists():
        raise FileNotFoundError(f"Annotations database not found at {ANNOTATIONS_DB}")
    
    conn = sqlite3.connect(str(ANNOTATIONS_DB))
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT 
            ZANNOTATIONSELECTEDTEXT,
            ZANNOTATIONNOTE,
            ZFUTUREPROOFING5
        FROM ZAEANNOTATION
        WHERE ZANNOTATIONASSETID = ?
        AND ZANNOTATIONSELECTEDTEXT IS NOT NULL
        AND ZANNOTATIONDELETED = 0
        ORDER BY ZANNOTATIONLOCATION
    """, (asset_id,))
    
    highlights = []
    for row in cursor.fetchall():
        highlights.append(Highlight(
            text=row[0] or "",
            note=row[1] or "",
            chapter=row[2] or "",
        ))
    
    conn.close()
    return highlights


def list_books():
    """List all books with highlights."""
    if not BOOKS_DB.exists():
        raise FileNotFoundError(f"Books database not found at {BOOKS_DB}")
    
    conn = sqlite3.connect(str(BOOKS_DB))
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT ZTITLE, ZAUTHOR
        FROM ZBKLIBRARYASSET
        WHERE ZASSETID IN (
            SELECT DISTINCT ZANNOTATIONASSETID 
            FROM ZAEANNOTATION 
            WHERE ZANNOTATIONSELECTEDTEXT IS NOT NULL
        )
        ORDER BY ZTITLE
    """)
    
    results = cursor.fetchall()
    conn.close()
    
    return results


def main():
    if len(sys.argv) < 2:
        print("Usage:", file=sys.stderr)
        print("  python highlights.py list              - List books with highlights", file=sys.stderr)
        print("  python highlights.py \"Book Title\"      - Get highlights for a book", file=sys.stderr)
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "list":
        try:
            books = list_books()
            print("# Books with Highlights\n")
            for title, author in books:
                print(f"- {title} by {author}")
        except FileNotFoundError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # Treat as book title
        book_title = " ".join(sys.argv[1:])
        
        try:
            asset_id = get_book_asset_id(book_title)
            if not asset_id:
                print(f"Book not found: {book_title}", file=sys.stderr)
                print("\nAvailable books:", file=sys.stderr)
                for title, author in list_books():
                    print(f"  - {title}", file=sys.stderr)
                sys.exit(1)
            
            highlights = get_highlights(asset_id)
            
            print(f"# Highlights from {book_title}\n")
            print(f"**Total highlights:** {len(highlights)}\n")
            print("---\n")
            
            for i, h in enumerate(highlights, 1):
                print(f"## Highlight {i}\n")
                print(str(h))
                print("\n---\n")
                
        except FileNotFoundError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
