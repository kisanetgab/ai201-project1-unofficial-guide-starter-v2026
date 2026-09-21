# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**

Two of my five questions (housing lottery, dining dollars) come from
documents I've already confirmed retrieve cleanly at distances under 0.27.
The other three are less-tested topics, so I expect at least one might not
retrieve as cleanly — hence 4 of 5, not 5 of 5.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**

Since campus_life documents are short and mostly self-contained (88 documents,
88 chunks — one chunk per document at the current chunk size), there's no
structural reason generation should ever have zero retrieved chunks to cite
from, as long as the question is in-corpus. 5 of 5 is achievable here.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

Not yet measured — I haven't run the actual distance comparison in Milestone
4 yet. Based on one early example (a pizza question scored 0.512, under my
current 0.6 cutoff, but the model still declined to answer at the generation
step), I suspect there may not be a clean gap between in-corpus and
out-of-corpus distances at 0.6. 4 of 5 accounts for that uncertainty rather
than assuming a clean separation.

**Why this target:**
<!-- What did your distances look like when you set the cutoff in Milestone 4?
     Was there a clean gap, or did the two groups overlap? -->

---

## 4. Something about your chunks

<!-- YOU WRITE THIS ONE.

For at least 4 of 5 sampled chunks, the chunk is exactly one full source
document — starting at the beginning of the file and ending at its end —
with no chunk boundary falling in the middle of a sentence.

**Why this target:**

Since campus_life's average document length (317 characters) is well under
the current chunk size (800 characters), 88 documents produced exactly 88
chunks — every chunk I've sampled so far (5 of 5) is a whole document, start
to finish. I set the target at 4 of 5 rather than 5 of 5 because a few
documents in this corpus (like the "followup" posts) run longer, and I
haven't checked all of them yet.


---

## 5. The cited source is actually one of the closest matches, not just present



**Why this target:**

Criterion 2 only checks that *a* source gets named. That's a weaker
guarantee than the named source actually being the most relevant one. In my
one test so far (the housing lottery question), the retrieved sources
included tangentially related documents like admin_parking_permits.txt
alongside the correct one — so I want to verify the model is citing from the
strongest matches, not just whatever happened to be in the pool of 5.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
