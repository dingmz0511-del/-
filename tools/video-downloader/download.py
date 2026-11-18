#!/usr/bin/env python3
"""Download a single public video with yt-dlp.

Usage:
    python tools/video-downloader/download.py "https://example.com/video"
    python tools/video-downloader/download.py "https://example.com/video" --output downloads
"""
import argparse
import sys
from pathlib import Path
from urllib.parse import urlparse

from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError


def main() -> int:
    parser = argparse.ArgumentParser(description="Download one public video with yt-dlp")
    parser.add_argument("url", help="Public video URL")
    parser.add_argument("--output", default="downloads", help="Output directory (default: downloads)")
    args = parser.parse_args()

    parsed = urlparse(args.url.strip())
    if parsed.scheme not in ("http", "https") or not parsed.hostname:
        parser.error("The URL must be a valid http:// or https:// link")

    target = Path(args.output).expanduser()
    target.mkdir(parents=True, exist_ok=True)

    options = {
        "outtmpl": str(target / "%(title).150s [%(id)s].%(ext)s"),
        "noplaylist": True,
        "restrictfilenames": True,
        "merge_output_format": "mp4",
        "overwrites": False,
    }
    try:
        with YoutubeDL(options) as ydl:
            result = ydl.download([args.url.strip()])
        return int(result or 0)
    except DownloadError as exc:
        print(f"Download failed: {exc}", file=sys.stderr)
        print("Some sites require login or may temporarily block automatic downloads.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
