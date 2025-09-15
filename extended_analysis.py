"""
extended_analysis.py
--------------------
Analyzes Bluesky posts collected via bsky_charliekirk.py.
- Flags extremist rhetoric using keywords
- Applies severity scoring (1-5)
- Summarizes top authors, word frequencies, and language breakdown
- Saves charts for timeline and severity distribution

Usage:
    python extended_analysis.py
"""

import pandas as pd
import matplotlib.pyplot as plt
from langdetect import detect

INPUT_FILE = "charliekirk_deserved_posts.csv"

# Keywords and severity scoring
FLAG_TERMS = {
    "deserved": 2,
    "kill": 4,
    "dead": 3,
    "celebrate": 3,
    "nazi": 4,
    "hitler": 4,
    "white supremacist": 4,
    "far-right": 3,
    "extremist": 3,
    "trans": 2,
}

def score_post(text: str) -> int:
    """Assign a severity score to a post based on keyword matches."""
    score = 0
    if not isinstance(text, str):
        return score
    for term, value in FLAG_TERMS.items():
        if term.lower() in text.lower():
            score = max(score, value)
    return score

def main():
    print(f"Loading {INPUT_FILE}...")
    df = pd.read_csv(INPUT_FILE)

    # Apply scoring
    df["score"] = df["text"].apply(score_post)

    # Flagged subset
    flagged = df[df["score"] > 0]
    high_severity = flagged[flagged["score"] >= 4]

    print(f"Total posts: {len(df)}")
    print(f"Flagged: {len(flagged)}")
    print(f"High severity: {len(high_severity)}\n")

    # Top repeat offenders
    print("Top repeat offenders:")
    print(flagged["author"].value_counts().head(20))

    # Word counts
    words = " ".join(flagged["text"].dropna().astype(str)).lower().split()
    word_freq = pd.Series(words).value_counts().head(20)
    print("\nMost common words in flagged posts:")
    print(word_freq)

    # Language detection (sample)
    sample = flagged.sample(min(500, len(flagged)), random_state=42)
    langs = sample["text"].dropna().apply(
        lambda t: detect(t) if isinstance(t, str) and len(t) > 20 else "unknown"
    )
    print("\nLanguage breakdown (sampled):")
    print(langs.value_counts())

    # Timeline severity
    df["createdAt"] = pd.to_datetime(df["createdAt"], errors="coerce", utc=True)
    timeline = df.groupby(df["createdAt"].dt.date)["score"].agg(["count", "mean"])

    # Charts
    plt.figure(figsize=(10, 5))
    timeline["count"].plot(title="Post Volume Over Time")
    plt.savefig("timeline.png")
    print("Saved chart: timeline.png")

    plt.figure(figsize=(8, 5))
    flagged["score"].plot.hist(bins=5, title="Severity Score Distribution")
    plt.savefig("severity_hist.png")
    print("Saved chart: severity_hist.png")

if __name__ == "__main__":
    main()
