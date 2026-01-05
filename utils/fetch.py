#!/usr/bin/env python3
"""
YouTube Transcript Fetcher
Minimal utility - just fetches transcript, Claude does the thinking
"""
import sys
import re
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url_or_id: str) -> str:
    """Extract video ID from URL or return as-is if already an ID."""
    if "youtube.com" in url_or_id or "youtu.be" in url_or_id:
        # Handle various YouTube URL formats
        patterns = [
            r'(?:v=|/v/|youtu\.be/)([a-zA-Z0-9_-]{11})',
            r'(?:embed/)([a-zA-Z0-9_-]{11})',
        ]
        for pattern in patterns:
            match = re.search(pattern, url_or_id)
            if match:
                return match.group(1)
    # Assume it's already a video ID
    return url_or_id.split('&')[0]  # Remove any query params


def fetch_transcript(video_id: str) -> str:
    """Fetch transcript and return as plain text."""
    ytt = YouTubeTranscriptApi()
    transcript_list = ytt.fetch(video_id)
    
    # Combine all text segments
    full_text = " ".join([entry.text for entry in transcript_list])
    
    # Clean up
    full_text = re.sub(r'\s+', ' ', full_text)
    
    return full_text


def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch.py <youtube_url_or_id>", file=sys.stderr)
        print("Output: Transcript text to stdout", file=sys.stderr)
        sys.exit(1)
    
    url_or_id = sys.argv[1]
    video_id = extract_video_id(url_or_id)
    
    try:
        transcript = fetch_transcript(video_id)
        print(transcript)
    except Exception as e:
        print(f"Error fetching transcript: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
