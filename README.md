# Peds-quizzes
## Mini quizzes

Open `index.html` in a browser. It has 29 quizzes of 9-10 questions each, 10 minutes per quiz, and every question in a quiz comes from a different lecture.

- Questions live in `data/c*.txt`, one block per question: `@<lecture> <batch> [dr]`, the stem, options (`*` marks the answer), and `>` for the explanation.
- After editing a question, run `python3 build.py` to rebuild `data/questions.json` and `index.html`.
- Answers follow `Pediatric Midterm Solved .pdf` (answers highlighted in purple). Explanations were written by Claude. Questions tagged `conflict` are ones where the solved PDF highlights different answers in different copies; the explanation says which was kept. `dr` marks answers the PDF notes as doctor-confirmed.
- Mixed quizzes are built from the first 285 questions so existing quizzes stay the same; questions added later are appended to the shortest quizzes.
