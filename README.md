# The Unofficial Guide

Kisanet Gabreselassie — campus_life corpus 

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

This is a RAG system over the campus_life corpus: 88 short documents (about
317 characters each) about student life at a university — dining halls,
dorms, courses, and administrative rules that aren't explained clearly
anywhere official. The system answers questions like "is the housing lottery
random?" by retrieving the most relevant chunks from these documents and
generating an answer grounded only in what it retrieved, naming its source.
If nothing retrieved is actually relevant, it says so instead of guessing.

## Chunking Strategy

**Chunk size:** 800 characters
**Overlap:** 120 characters

These are still the starter's defaults (chunker.py::fallback_split),
unchanged so far. Almost every document in campus_life is under 800
characters, so the chunker isn't actually cutting anything apart yet — 88
documents in, 88 chunks out, one chunk per document. Whether that stays true
once I look more closely at multi-sentence documents is what Milestone 3 is
for.

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: ``  `admin_add_drop_deadline.txt#0` — produced by: `chunker.py::fallback_split` ``

```
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** — source: `` `course_biol_160.txt#0` — produced by: `chunker.py::fallback_split` ``

```
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.
```

**Chunk 3** — source: ``  `course_hist_118_workload.txt#0` — produced by: `chunker.py::fallback_split` ``

```
Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 4** — source: ``  `dining_pellew_dining_hall_followup.txt#0` — produced by: `chunker.py::fallback_split` ``

```
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.
```

**Chunk 5** — source: `` `housing_innisfree_hall.txt#0` — produced by: `chunker.py::fallback_split` ``

```
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:** is the housing lottery random?

**Answer:** 

```
The housing lottery is not entirely random; rising sophomores get a randomly drawn number, but juniors and seniors are ordered by accumulated credit hours first, with random tie-breaks.
Source: admin_housing_lottery.txt
```





**My relevance cutoff:** 0.6 (starter default — not yet tuned; that's Milestone 4)

| Question | In corpus? | Best distance |
|---|---|---|
| is the housing lottery random? | Yes | 0.254 |
| do dining dollars roll over to the next school year? | Yes | 0.264 |
| what's the best pizza place near campus? | No | 0.512 |

The third question is a useful early signal for Milestone 4: at 0.512 the
distance was still under my current cutoff of 0.6, so the relevance gate
itself didn't block it. What stopped a wrong answer was the generation step
recognizing that none of the retrieved chunks (dining halls, cafes) named a
pizza place, so it said "I don't have enough information" rather than
guessing. That suggests 0.6 may end up too loose once I measure it properly.


## How I Used AI

**1.** I asked Claude to help debug a `chroma-hnswlib` build failure during
`pip install`. It diagnosed this as a broken Xcode Command Line Tools install
on macOS rather than a code problem, and had me reinstall them
(`sudo rm -rf /Library/Developer/CommandLineTools` then `xcode-select
--install`), which fixed it.

**2.** I asked Claude to draft this README's Unit 1 sections from my actual
terminal output (chunk contents from `python app.py chunks`, and answers from
`python app.py ask`), rather than writing the summary from scratch myself.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks stay whole document boundaries | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Cited source is in top-3 closest matches | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |


<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

### Real output — Criterion 1 (retrieved chunk contains the answer)

Question: "What happens if I drop a course after week two?"

```
Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, admin_grade_appeals.txt, admin_pass_fail_option.txt, admin_withdrawal_deadline.txt

If you drop a course after week two, it shows as a W on your transcript (admin_add_drop_deadline.txt).
```

The top-ranked retrieved chunk (admin_add_drop_deadline.txt) is the exact source document, and it contains the answer verbatim — this held across all three runs and all five questions.

### Real output — Criterion 3 (gate refuses out-of-corpus questions)

Question: What is the capital of Mongolia? — best distance 0.825 — refused

How do I change the oil in a diesel engine? — best distance 0.934 — refused
Who won the 1994 World Cup? — best distance 0.886 — refused
What is the recommended dosage of ibuprofen for a headache? — best distance 0.844 — refused
How do I write a for loop in Rust? — best distance 0.896 — refused


All five out-of-scope questions landed well above the 0.6 cutoff (0.82–0.93), compared to my five in-corpus questions landing well below it (0.165–0.345). That's a clean gap of roughly 0.5, not a close call.



## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MET | 5/5 on all 3 runs, above my 4/5 target. Every question's top retrieved chunk was the exact source document. |
| 2 | Every answer names a source | MET | 5/5 on all 3 runs, matching my 5/5 target exactly — no room for slack, and it held. |
| 3 | Gate stops out-of-corpus questions | MET | 5/5, above my 4/5 target. Distances for out-of-scope questions (0.82–0.93) were clearly separated from in-corpus questions (0.165–0.345) — a gap of roughly 0.5, not a close call. |
| 4 | Chunks stay whole document boundaries | MET | 5/5 sampled chunks (from python app.py chunks) were each one complete document, start to finish, above my 4/5 target. |
| 5 | Cited source is in top-3 closest matches | MET | 5/5 — every question's cited source was either the #1 or #2 closest retrieved chunk (never worse), above my 4/5 target. |



## Diagnoses


Nothing failed — all 5 criteria passed on all 3 runs. Per the assignment's own warning, that's not a sign of a great system; it likely means my targets were too easy to fail.

Criterion 2 ("every answer names a source") is the clearest example: my code always attaches a source to every answer, no matter what. There's no way for it to fail, so it never really tested anything. I'd rewrite it to check whether the cited source is correct, not just present.

Criteria 1 and 3 had real margin (5/5 against a 4/5 target), so those feel like genuine tests, not guaranteed passes.

Criteria 4 and 5 held true this time, but only got tested on easy, single-topic questions. A messier corpus (like advice_threads) would be a harder test.

One limitation: my scorer only checks whether an expected word appears in the answer — it can't catch a made-up fact sitting next to a correct one. I manually checked all 15 answers by hand and found nothing fabricated, but that check wasn't automatic.

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**
Replaced the fixed 800-character chunker with one that splits on paragraph breaks — this produced 271 chunks instead of 88, revealing that many documents actually contained multiple distinct paragraphs (like a "the good / the bad" dorm review) that were previously merged into one chunk.

**Why I picked it:**

My diagnosis flagged that the default chunker was never a deliberate choice, and that criteria 4 and 5 were only tested on easy, single-topic documents — paragraph splitting was a real test of whether document structure mattered for this corpus.


### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks stay whole document boundaries | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Cited source is in top-3 closest matches | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

Full output in `results/run_2026-09-27_1710_after.md`.


**Did it help?**

Mixed, honestly. All five criteria still passed at the same rate as before, so nothing changed at the level the criteria measure. But individual distances moved in both directions: 3 of 5 questions got closer to their answer (0.345→0.305, 0.285→0.265, 0.165→0.144), while 2 got slightly further (0.264→0.307, 0.258→0.363) — likely because splitting on paragraphs sometimes separates a fact from the sentence that gives it context, which fixed-size chunking had accidentally kept together. Out-of-scope distances also moved slightly closer to my cutoff (0.877 avg → 0.817 avg), though still comfortably above 0.6.

The clearest win was efficiency: total tokens used dropped from 9,497 to 6,618 across the same 15 calls, since paragraph-sized chunks send less irrelevant text to the model per question. So the change didn't move my pass/fail criteria, but it did make retrieval more precise on average and cheaper to run — a real, if modest, improvement.

     Milestone 4. -->

## What's Still Broken

Nothing failed outright, but two things are still weakly tested. Criterion 2 ("every answer names a source") can't meaningfully fail given how the code is written, so it isn't really evidence of anything — I'd need to rewrite it to check that the cited source is correct, not just present, to make it a real test. 

And criteria 4 and 5 have only been tested against short, single-topic questions from campus_life; a messier corpus like advice_threads (with multiple people replying and disagreeing) would be a harder, more honest test of whether chunking and source-citation actually hold up. 


## What I'd Do Differently

I'd tighten criterion 2 from "names a source" (which the code guarantees automatically) to "names the correct source," which is a real test rather than a free pass. I'd also pick harder test questions upfront — all five of mine turned out to be easy single-fact lookups, so I never got to see what a genuine failure looks like or practice diagnosing one for real.
