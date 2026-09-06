#!/usr/bin/env python3
"""
Generate GitHub Contribution Graph Art: LUCY ♥ U
Creates backdated empty commits that form pixel art on the contribution graph.
Target year: 2025
"""

import subprocess
import datetime
import os
import sys

LETTERS = {
    'L': [
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,1,1,1,1],
    ],
    'U': [
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0],
    ],
    'C': [
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,1],
        [0,1,1,1,0],
    ],
    'Y': [
        [1,0,0,0,1],
        [0,1,0,1,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
    ],
    'H': [  # heart ♥
        [0,1,0,1,0],
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1],
        [0,1,1,1,0],
        [0,0,1,0,0],
        [0,0,0,0,0],
    ],
    ' ': [
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
    ],
}

MESSAGE = "LUCY H U"

REPO_DIR = os.path.expanduser("~/Documents/lucy-contribution-art")
TARGET_YEAR = 2025
COMMITS_PER_PIXEL = 5


def build_grid(message):
    grid = [[] for _ in range(7)]
    for i, char in enumerate(message):
        letter = LETTERS.get(char, LETTERS[' '])
        for row in range(7):
            grid[row].extend(letter[row])
        if char != ' ' and i < len(message) - 1:
            for row in range(7):
                grid[row].append(0)
    return grid


def preview_grid(grid):
    total_cols = len(grid[0])
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    print(f"\n  Preview ({total_cols} columns):\n")
    for row in range(7):
        line = f"  {days[row]} "
        for col in range(total_cols):
            line += "██" if grid[row][col] else "  "
        print(line)
    print()


def find_first_sunday(year):
    d = datetime.date(year, 1, 1)
    while d.weekday() != 6:
        d += datetime.timedelta(days=1)
    return d


def run(cmd, env=None):
    result = subprocess.run(cmd, capture_output=True, text=True, env=env)
    if result.returncode != 0:
        print(f"  ERROR: {result.stderr.strip()}")
        sys.exit(1)


def main():
    grid = build_grid(MESSAGE)
    total_cols = len(grid[0])

    print("=" * 60)
    print("  LUCY ♥ U — Contribution Graph Art Generator")
    print("=" * 60)

    preview_grid(grid)

    first_sunday = find_first_sunday(TARGET_YEAR)
    usable_weeks = 52
    start_col = (usable_weeks - total_cols) // 2

    print(f"  Target year  : {TARGET_YEAR}")
    print(f"  Grid size    : {total_cols} cols × 7 rows")
    print(f"  Start week   : {start_col}")
    print(f"  First Sunday : {first_sunday}")
    print(f"  Commits/pixel: {COMMITS_PER_PIXEL}")

    pixel_count = sum(grid[r][c] for r in range(7) for c in range(total_cols))
    total_commits = pixel_count * COMMITS_PER_PIXEL
    print(f"  Active pixels: {pixel_count}")
    print(f"  Total commits: {total_commits}")
    print()

    os.makedirs(REPO_DIR, exist_ok=True)
    os.chdir(REPO_DIR)

    if not os.path.exists(".git"):
        run(["git", "init"])
        run(["git", "config", "user.name", "reandri-1"])
        run(["git", "config", "user.email", "reandri-1@users.noreply.github.com"])
        run(["git", "checkout", "-b", "main"])
        with open("README.md", "w") as f:
            f.write("# 🎨 Contribution Art\n\nThis repo generates pixel art on my GitHub contribution graph.\n")
        run(["git", "add", "."])
        run(["git", "commit", "-m", "init"])
        print("  ✓ Repository initialized\n")

    commit_num = 0
    for col in range(total_cols):
        for row in range(7):
            if grid[row][col] == 1:
                week_offset = start_col + col
                target_date = first_sunday + datetime.timedelta(days=week_offset * 7 + row)

                if target_date.year != TARGET_YEAR:
                    continue

                date_str = f"{target_date.isoformat()}T12:00:00"
                env = os.environ.copy()
                env["GIT_AUTHOR_DATE"] = date_str
                env["GIT_COMMITTER_DATE"] = date_str

                for _ in range(COMMITS_PER_PIXEL):
                    commit_num += 1
                    run(
                        ["git", "commit", "--allow-empty", "-m", f"art #{commit_num}"],
                        env=env
                    )

        progress = int((col + 1) / total_cols * 100)
        print(f"\r  Generating commits... {progress}%", end="", flush=True)

    print(f"\n\n  ✅ Done! {commit_num} commits created in:\n  {REPO_DIR}")
    print(f"\n  Next steps:")
    print(f"  1. Create repo 'lucy-contribution-art' on GitHub")
    print(f"  2. cd {REPO_DIR}")
    print(f"  3. git remote add origin git@github.com:reandri-1/lucy-contribution-art.git")
    print(f"  4. git push -u origin main")
    print()


if __name__ == "__main__":
    main()
