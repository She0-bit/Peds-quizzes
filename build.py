"""Parse data/c*.txt question files into questions.json."""
import glob, json, re, sys, difflib

LECTURES = {
 "L3":"Growth and Growth Disorders","L4":"Immunization","L5":"Common GI Problems 1",
 "L6":"Common GI Problems 2","L7":"Common Pediatric Infection 1","L8":"Common Pediatric Infection 2",
 "L9":"Acid-Base Balance","L10":"Behavioral Disorders","L11":"Common Pediatric Emergency",
 "L12":"Normal Development","L13":"Acquired Heart Disease","L14":"Congenital Heart Disease",
 "L15":"Basic Nutritional Concepts","L16":"Nutritional Disorders","L17":"Common Neonatal Conditions",
 "L18":"Serious Pediatric Infection","L19":"Pediatric Rheumatology","L20":"Common Renal Disorders",
 "L21":"Renal Failure","L22":"Immunodeficiency","L23":"Neonatal Jaundice","L24":"Anemia in Pediatrics",
 "L25":"Seizures in Pediatrics","L26":"Common Respiratory Infection","L27":"Common Respiratory Disorders",
 "L28":"Fluid & Electrolyte Disturbance","Other":"Other / Genetics & Endocrine"}

qs, errs = [], []
for f in sorted(glob.glob("data/c*.txt")):
    for block in re.split(r"\n(?=@)", open(f).read().strip()):
        lines = [l for l in block.strip().split("\n") if l.strip()]
        head = lines[0].split()
        lec, year, dr = head[0][1:], head[1], "dr" in head[2:]
        imm = lec == "L4" or "imm" in head[2:]
        stem = " ".join(l for l in lines[1:] if l[:2] not in ("- ", "* ", "> "))
        opts = [l[2:].strip() for l in lines if l[:2] in ("- ", "* ")]
        ans = [i for i, l in enumerate(l for l in lines if l[:2] in ("- ", "* ")) if l.startswith("* ")]
        expl = " ".join(l[2:] for l in lines if l.startswith("> "))
        where = f"{f}: {stem[:50]}"
        if lec not in LECTURES: errs.append(f"bad lecture {lec} in {where}")
        if len(ans) != 1: errs.append(f"answer count {len(ans)} in {where}")
        if len(opts) < 3: errs.append(f"<3 options in {where}")
        if not expl: errs.append(f"no explanation in {where}")
        qs.append(dict(id=len(qs), lec=lec, year=year, dr=dr, imm=imm, q=stem, o=opts, a=ans[0] if ans else -1, e=expl))

# near-duplicate report
for i in range(len(qs)):
    for j in range(i + 1, len(qs)):
        r = difflib.SequenceMatcher(None, qs[i]["q"], qs[j]["q"]).quick_ratio()
        if r > 0.85 and difflib.SequenceMatcher(None, qs[i]["q"], qs[j]["q"]).ratio() > 0.8:
            errs.append(f"possible dup {i}/{j}: {qs[i]['q'][:60]} || {qs[j]['q'][:60]}")

print("\n".join(errs) or "no errors")
from collections import Counter
print(len(qs), "questions"); print(sorted(Counter(q["lec"] for q in qs).items(), key=lambda x: -x[1]))
json.dump({"lectures": LECTURES, "questions": qs}, open("data/questions.json", "w"), indent=0)

html = open("template.html").read().replace("__DATA__", json.dumps({"lectures": LECTURES, "questions": qs}, ensure_ascii=False))
open("index.html", "w").write(html)
print("wrote index.html", len(html), "bytes")
