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

# Charlie Kirk Extremist Dataset (Bluesky)

**Maintainer:** [@truconservatv](https://github.com/truconservatv)  

This repository contains public posts scraped from Bluesky using its public API, focusing on extremist discourse surrounding Charlie Kirk — including posts celebrating his reported death and material from accounts linked to far-right and far-left extremist narratives.  

---

## Disclaimer

This dataset is provided **for journalistic and research purposes only**.  
It contains **publicly available information** gathered from a public-facing API.  

- No private information was collected.  
- No accounts were accessed without authorization.  
- The purpose of this dataset is to allow **researchers, journalists, and watchdogs** to study extremist narratives, coordinated disinformation, and online radicalization patterns.  

The maintainer **does not endorse or promote any of the content** contained herein.

---

## Files

- `charliekirk_deserved_posts.csv` — raw posts including the search terms.  
- `charliekirk_celebration_broad.csv` — broader subset including “deserved it” and related terms.  
- `charliekirk_celebration.csv` — filtered extremist celebration subset.  

---

## Usage

Clone this repo:

```bash
git clone https://github.com/truconservatv/charliekirk-extremist-bluesky.git
cd charliekirk-extremist-bluesky


