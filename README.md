# charliekirk-extremist-bluesky
Dataset of Bluesky posts referencing Charlie Kirk containing extremist rhetoric, collected for research and journalistic analysis.

---
annotations_creators: []
language: en
license: cc-by-nc-sa-4.0
multilinguality: []
pretty_name: Charlie Kirk Extremist Bluesky Dataset
size_categories:
- 10K<n<100K
source_datasets: []
tags:
- journalism
- extremism
- bluesky
- politics
task_categories:
- text-classification
task_ids:
- hate-speech-detection
---

# Charlie Kirk Extremist Bluesky Dataset

**Maintainer:** [@campbellmsean](https://huggingface.co/campbellmsean)  
**Created:** September 2025  

---

## Disclaimer

This dataset contains **public posts** collected from Bluesky using the **public API**.  

⚠️ **Important Notes**:
- Posts were public and voluntarily made by their authors.  
- This dataset is provided **solely for research, academic, and journalistic purposes**.  
- It contains **harmful, offensive, extremist, and violent language**.  
- No private accounts or non-public data were accessed.  

The maintainer **does not endorse or promote** any of the content.

---

## Files

- `charliekirk_deserved_posts.csv` — full raw posts including defined queries.  
- `charliekirk_celebration_broad.csv` — broader subset including “deserved it” and related terms.  
- `charliekirk_celebration.csv` — filtered extremist celebration subset.  
- `charliekirk_extremist_review.csv` — curated review pack of flagged material.  
- `charliekirk_review_pack.csv` — mixed severity review pack.  
- `charliekirk_flagged.csv` — severity-scored posts.  
- Scripts: `extended_analysis.py`, `celebration_filter.py`, etc.  

---

## Methodology

- **Source:** Collected using [atproto client](https://github.com/bluesky-social/atproto) from Bluesky’s **public API**.  
- **Queries:** `"Charlie Kirk"`, `"deserved it"`, `"he deserved"`, `"she deserved"`, `"they deserved"`, `"far-right"`, `"right-wing"`, `"right-wing extremist"`, `"Nazi"`, `"Hitler"`, `"white supremacist"`, `"trans"`.  
- **Filtering:** Regex + severity scoring (1–5).  
- **Manual curation:** Context checks excluded satire, quotes without endorsement, or unrelated posts.  

---

## License

**CC BY-NC-SA 4.0**  
- Non-commercial use only  
- Attribution required  
- Share alike  

---

## Citation

> Campbell, S. (2025). Charlie Kirk Extremist Bluesky Dataset. Hugging Face. https://huggingface.co/datasets/campbellmsean/charliekirk-extremist-bluesky
