#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from langdetect import detect, DetectorFactory, LangDetectException

DetectorFactory.seed = 0  # stable language detection

INPUT = "charliekirk_posts.csv"
OUTPUT = "charliekirk_flagged.csv"

# Extended keyword & emoji patterns
KEYWORDS = {
    "kill": 3,
    "death": 3,
    "murder": 3,
    "hang": 4,
    "execute": 4,
    "terrorist": 2,
    "traitor": 2,
    "fuck charlie kirk": 3,
    "he deserved": 2,
    "far-right": 1,
    "far-right extremists": 2,
}

EMOJIS = {
    "💀": 2,
    "🔫": 3,
    "🔪": 3,
    "🔥": 2,
    "☠️": 3,
}

def score_text(text: str) -> int:
    score = 0
    lower = str(text).lower()
    for kw, val in KEYWORDS.items():
        if kw in lower:
            score += val
    for emoji, val in EMOJIS.items():
        if emoji in str(text):
            score += val
    return score

def safe_detect(text: str) -> str:
    try:
        if not isinstance(text, str) or len(text.strip()) < 20:
            return "unknown"
        return detect(text)
    except LangDetectException:
        return "unknown"

def main():
    df = pd.read_csv(INPUT)
    df["score"] = df["text"].astype(str).apply(score_text)

    # save updated flagged file
    df.to_csv(OUTPUT, index=False)

    # --- Summary ---
    total = len(df)
    flagged = (df["score"] > 0).sum()
    high = (df["score"] >= 4).sum()
    print(f"Total posts: {total}")
    print(f"Flagged: {flagged}")
    print(f"High severity: {high}\n")

    # --- Top repeat offenders ---
    offenders = df[df["score"] > 0]["author"].value_counts().head(20)
    print("Top repeat offenders:")
    print(offenders)

    # --- Common violent/framing words ---
    words = []
    for t in df[df["score"] > 0]["text"].dropna():
        words.extend(t.lower().split())
    counter = Counter(words)
    print("\nMost common words in flagged posts:")
    for w, c in counter.most_common(20):
        print(f"{w}: {c}")

    # --- Language detection (sample 500) ---
    sample = df.sample(min(500, len(df)), random_state=42)
    langs = sample["text"].dropna().apply(safe_detect)
    print("\nLanguage breakdown (sampled):")
    print(langs.value_counts())

    # --- Timeline ---
    df["createdAt"] = pd.to_datetime(df["createdAt"], errors="coerce", utc=True)
    df = df.dropna(subset=["createdAt"])
    timeline = df.groupby(df["createdAt"].dt.date)["score"].agg(
        total="count",
        flagged=lambda x: (x > 0).sum(),
        high=lambda x: (x >= 4).sum()
    )

    timeline.plot(y=["total", "flagged", "high"], figsize=(10,6))
    plt.title("Posts over time")
    plt.ylabel("Count")
    plt.xlabel("Date")
    plt.legend(["Total", "Flagged", "High severity"])
    plt.tight_layout()
    plt.savefig("timeline.png")
    print("\nSaved chart: timeline.png")

    # --- Severity histogram ---
    df["score"].plot.hist(bins=20, figsize=(8,6))
    plt.title("Distribution of severity scores")
    plt.xlabel("Score")
    plt.ylabel("Post count")
    plt.tight_layout()
    plt.savefig("severity_hist.png")
    print("Saved chart: severity_hist.png")

if __name__ == "__main__":
    main()
