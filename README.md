# Peds-quizzes
## Mini quizzes

Open `index.html` in a browser. It has 29 quizzes of 9-10 questions each, 10 minutes per quiz, and every question in a quiz comes from a different lecture.

- Questions live in `data/c*.txt`, one block per question: `@<lecture> <batch> [dr]`, the stem, options (`*` marks the answer), and `>` for the explanation.
- After editing a question, run `python3 build.py` to rebuild `data/questions.json` and `index.html`.
- The source PDF is unsolved. The answers were written by Claude and should be checked against the lecture slides. Questions tagged `dr` use answers noted in the PDF as doctor-confirmed.
