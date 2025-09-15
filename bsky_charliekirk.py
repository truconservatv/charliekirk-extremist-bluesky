import csv
import time
from atproto import Client

# === CREDENTIALS ===
USERNAME = "seancreports.bsky.social"
PASSWORD = "ftrg-agbi-jtbl-jtoi"   # app password

# === SEARCH QUERIES ===
QUERIES = [
    "Charlie Kirk",
    "he deserved",
    "deserved it",
    "far-right",
]

# === OUTPUT FILE ===
OUTPUT_FILE = "charliekirk_deserved_posts.csv"


def save_to_csv(posts, filename):
    """Save list of post dicts to CSV"""
    keys = posts[0].keys() if posts else []
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(posts)


def main():
    client = Client()
    client.login(USERNAME, PASSWORD)

    all_posts = []
    seen_uris = set()  # avoid duplicates

    for query in QUERIES:
        cursor = None
        batch_size = 100

        print(f"Searching for: {query}")
        while True:
            results = client.app.bsky.feed.search_posts(
                {"q": query, "limit": batch_size, "cursor": cursor}
            )
            if not results.posts:
                break

            for post in results.posts:
                if post.uri not in seen_uris:
                    seen_uris.add(post.uri)
                    all_posts.append(
                        {
                            "createdAt": getattr(post.record, "createdAt", ""),
                            "author": post.author.handle,
                            "uri": post.uri,
                            "text": getattr(post.record, "text", ""),
                            "query": query,
                        }
                    )

            cursor = results.cursor
            print(f"  Collected {len(all_posts)} total so far...")

            if not cursor:
                break

            time.sleep(1)  # polite pause

    save_to_csv(all_posts, OUTPUT_FILE)
    print(f"Saved {len(all_posts)} posts to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
