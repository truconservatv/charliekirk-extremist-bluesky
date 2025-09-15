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

This dataset contains **public posts** collected from the social media platform Bluesky using the **official public API**.  

⚠️ **Important Notes**:
- Posts were made publicly and voluntarily by their authors.  
- This dataset is provided **solely for research, academic, and journalistic purposes**.  
- It contains **harmful, offensive, extremist, and violent language**. The presence of this content does not imply endorsement.  
- No private messages, emails, phone numbers, or non-public data are included.  

---

## Purpose

The dataset was created to **document extremist rhetoric** and **celebratory reactions to political violence** so that journalists and researchers can study them responsibly.  

This work aligns with Hugging Face’s Content Policy, which explicitly states that *“context matters—discussing extremist content academically or neutrally is allowed.”*

---

## Methodology

- Data collected using the **atproto/Bluesky API** via Python.  
- Queries targeted terms such as:  
  - `"deserved it"`, `"far-right"`, `"far-right extremist"`, `"celebrate"`  
  - Expanded to `"Nazi"`, `"Hitler"`, `"white supremacist"`, `"trans"`  
- Posts were saved as `.csv` tables and later filtered/flagged for severity (celebration, threat, ideological reference).  
- Handles are preserved only to document public posting; they should not be used for harassment.  

---

## License

Licensed under **CC BY-NC-SA 4.0**.  
- **Non-commercial use only.**  
- **Attribution required.**  
- **Share alike.**  

---

## Citation

If you use this dataset, please cite:  

> Campbell, S. (2025). Charlie Kirk Extremist Bluesky Dataset. Hugging Face. https://huggingface.co/datasets/campbellmsean/charliekirk-extremist-bluesky
