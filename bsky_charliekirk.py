"""
bsky_charliekirk.py
-------------------
Collects Bluesky posts mentioning Charlie Kirk or related extremist terms
using the official atproto client. Saves results to CSV.

Usage:
    python bsky_charliekirk.py
"""

import csv
from atproto import Client

# ---------------------------
# CONFIGURATION
# ---------------------------
USERNAME = "seancreports.bsky.social"
PASSWORD = "your-app-password-here"  # Replace with your Bluesky app password
OUTPUT_FILE = "charliekirk_deserved_posts.csv"

# Search terms (transparent and replicable)
SEARCH_TERMS = [
    "Charlie Kirk",
    "deserved it",
    "he deserved it",
    "she deserved it",
    "they deserved it",
    "far-right",
    "right-wing",
    "right-wing extremist",
    "Nazi",
    "Hitler",
    "white supremacist",
    "trans",
]

# ---------------------------
# MAIN SCRIPT
# ---------------------------
def main():
    client = Client()
    client.login(USERNAME, PASSWORD)

    all_posts = []

    for term in SEARCH_TERMS:
        print(f"Searching for term: {term}")
        try:
            results = client.app.bsky.feed.search_posts({"q": term, "limit": 100})
            for post in results.posts:
                all_posts.append({
                    "createdAt": post.record.created_at,
                    "author": post.author.handle,
                    "uri": post.uri,
                    "text": post.record.text,
                    "search_term": term,
                })
        except Exception as e:
            print(f"Error searching '{term}': {e}")

    # Save to CSV
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["createdAt", "author", "uri", "text", "search_term"])
        writer.writeheader()
        writer.writerows(all_posts)

    print(f"Saved {len(all_posts)} posts to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
