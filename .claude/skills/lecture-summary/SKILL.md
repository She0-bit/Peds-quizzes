---
name: lecture-summary
description: Turn an annotated lecture PDF (slides + handwritten/typed notes) into the standard landscape study summary PDF used in this repo. Use when the user uploads a lecture and asks for "a summary like before" / "same format".
---

# Lecture summary format

`example.html` is the finished L08 summary. Copy its `<style>` block unchanged and reuse its markup patterns. Only write new content.

## Reading the lecture (do not skip anything)
1. Extract text + render every page with PyMuPDF (`pip install pymupdf pillow`); most content is images/handwriting, so view every slide.
2. Zoom (dpi 400-500 clips) into dense handwriting, mind-maps, and pasted screenshots.
3. Note which points the doctor stressed: stars, "imp", underlines, "hallmark", red ink, mind-map highlights, case answers.

## Content rules
- Merge handwritten/typed notes INTO the content (no separate note styling, no ✎).
- No byline, no note-taker credits, no legend other than the highlight key, no conflicts section, no ⚠ markers. If sources disagree, use the slide version.
- No lecturer contact details.
- Short phrases with ➞ ↑ ↓ ±, not sentences. No em dashes.
- Flowcharts ➞ `.flow` box with indented `.i1` / `.i2` lines.
- Add nothing medical that is not in the lecture.

## Highlighting
- `<span class="hy">` yellow = stressed by the doctor (per the marks above).
- `<span class="hb">` blue = other high-yield (percentages, #1 organisms, classic exam numbers).
- `<span class="clue">` red underline = sign/symptom that points straight to the diagnosis.
- Key line under the title: `Yellow = stressed by the doctor · Blue = other high-yield · Red underline = clue`.

## Layout
- A4 landscape, each `.page` is fixed 297x210 mm; content is placed per page by hand (no auto-flow).
- Page = `h2` section title + `.row.grow` with two `.col` (flex ratios adjustable, e.g. 1 : 1.15).
- Each box = `.card` with `h3 > span.no` numbered `<section>.<n>` (1.1, 1.2, ...). Boxes never split across pages.
- Colour per section via class on `.page`: `ph` (pink), `om` (blue), `si` (teal), `sk` (orange), `ut` (gold); `gy` summary/MCQ; `pu` keywords.
- Page 1 starts with `h1` title + one `.scope` line listing topics, then the key line.
- Order: disease sections ➞ Summary table (+ extra comparison table if useful) ➞ Ultra-quick keyword table (2 columns) ➞ MCQs (lecture cases first, then new ones from lecture content only; 2 columns) ➞ Answer key on its own page.
- Images: crop clinical photos from slides with PyMuPDF `clip=`, save to `img/`, show with fixed height (18-34 mm).

## Build & check
```
python3 measure.py summary.html      # every page must have spare >= 0 (px); move/shrink cards if negative
/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless --no-sandbox --no-pdf-header-footer --print-to-pdf=out.pdf file://$PWD/summary.html
```
`measure.py` needs `pip install playwright` and uses the preinstalled Chromium. Render 1-2 pages to PNG and look at them before delivering. Save the PDF in the repo root as `<Lecture code> <Topic> Summary.pdf`.
