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

**Maintainer:** [@truconservatv](https://github.com/truconservatv)  

This repository contains datasets built from **Bluesky’s public API**, focusing on extremist discourse surrounding Charlie Kirk — including posts celebrating his reported death and material tied to far-right and far-left extremist narratives.  

---

## Disclaimer

This dataset is provided **for journalistic and research purposes only**.  
It contains **publicly available information** gathered from a public-facing API.  

- No private information was collected.  
- No accounts were accessed without authorization.  
- The purpose is to allow **researchers, journalists, and watchdogs** to study extremist narratives, disinformation, and online radicalization patterns.  

The maintainer **does not endorse or promote any of the content** contained herein.

---

## Files

- `charliekirk_deserved_posts.csv` — full raw posts including defined queries.  
- `charliekirk_celebration_broad.csv` — broader subset including “deserved it” and related terms.  
- `charliekirk_celebration.csv` — filtered extremist celebration subset.  
- `charliekirk_extremist_review.csv` — curated review pack of flagged material.  
- `charliekirk_review_pack.csv` — mixed low- and high-severity review pack.  
- `charliekirk_flagged.csv` — posts scored by severity filters.  
- Analysis scripts (e.g. `extended_analysis.py`, `celebration_filter.py`) for replication.  

---

## Methodology

### Source
All posts were collected via the official [atproto client](https://github.com/bluesky-social/atproto), accessing Bluesky’s **public API** only.  
No private messages, hidden accounts, or non-public data were accessed.

### Search Terms
The following search queries were used:

- "Charlie Kirk"  
- "deserved it"  
- "he deserved it"  
- "she deserved it"  
- "they deserved it"  
- "far-right"  
- "right-wing"  
- "right-wing extremist"  
- "Nazi"  
- "Hitler"  
- "white supremacist"  
- "trans"

These terms were chosen to surface extremist rhetoric celebrating Charlie Kirk’s death or embedding it in far-right/ideological discourse.

### Filtering & Classification
- **Keyword matches** (exact/regex)  
- **Severity scoring** (1–5) depending on rhetoric intensity  
- **Review subsets** prepared for manual validation  

### Manual Curation
After automated filtering, subsets were manually reviewed to confirm extremist content:  

1. **Context check** – Was the phrase celebratory, or quoting/mockery?  
2. **Tone classification** – Labeled Low/Medium/High severity:  
   - Low: political reference  
   - Medium: ambiguous or indirect endorsement  
   - High: explicit celebration of Kirk’s death or ideological justification  
3. **Exclusions** – Removed posts quoting without endorsement or unrelated to Kirk  

This ensures the dataset reflects extremist rhetoric, not just raw keyword dumps.

### Purpose
This dataset exists for **journalistic and academic research**.  
It is intended to help researchers and journalists study extremist celebration of political violence.  

- Not for harassment or doxxing  
- Posts are verbatim for verification  

### Limitations
- Some false positives (satire, criticism) may remain  
- Handles are shown as in Bluesky’s API  
- Posts are unaltered for transparency  

---

## Usage

Clone this repo:  

```bash
git clone https://github.com/truconservatv/charliekirk-extremist-bluesky.git
cd charliekirk-extremist-bluesky

