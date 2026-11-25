# Candidates — One Line, No Deadline Met

Judge criteria (most important first): (1) really an excuse for a missed
deadline; (2) a real joke with a turn/surprise, not a plain apology;
(3) single sentence, punch lands at the end; (4) sounds like a real person
cornered, exaggerated just enough; (5) fresh angle, no stock retreads.

## DeepSeek candidates (brutal mode, 3 generation calls)

### Batch 1 (gen1)
1. "I had it done Thursday, but I opened it to attach it and accidentally saved a grocery list over it, and honestly the grocery list was better organized." (160 chars) — Good surprise turn and a real excuse (file destroyed), but the joke lands on the grocery list, not on the deadline; the excuse feels secondary.

### Batch 2 (gen2)
2. "I did finish it, then reread it and had to go lie down in my car, so the work exists, it's just emotionally unavailable right now." (130 chars) — **PICKED.** See rationale below.
3. "I was ready to send it Thursday but I got into an argument with my own outline and I'm not proud of how that ended." (118 chars) — Fresh, human, funny; but the "argument" is abstract and the excuse (why that delayed sending) is thin.
4. "My neighbor's parrot learned my login and I refuse to type my password in front of him, so I've been waiting him out." (118 chars) — Absurd and funny, but fails criterion 4: nobody would actually say this when cornered; the excuse is not believable even as exaggeration.
5. "I spent the entire weekend mentally drafting an apology for sending this late, and that honestly took longer than the actual work." (133 chars) — Meta, clever, very human, punch at the end. Strong runner-up; slightly weaker than the pick because the turn ("apology took longer than the work") is a known self-referential joke shape.
6. "I finished it early and then made the mistake of improving the font, and I have now been choosing fonts for four days." (121 chars) — Extremely relatable, punch at the end, real excuse (procrastination by polish). Strong runner-up; loses on freshness — font-picking is a well-worn procrastination trope.

### Batch 3 (gen3)
7. "I finished it early, but then I opened the file to admire it and the cursor blinked at me judgmentally, so we're not on speaking terms." (137 chars) — Cute, but the cursor is not a reason for missing a deadline; excuse fails criterion 1.
8. "My laptop died, and I tried to grieve properly, but the five stages took longer than expected because I got stuck bargaining with Geek Squad." (151 chars) — Funny five-stages turn, but long, two clauses, punch diluted; "laptop died" is a stock opener.
9. "I would've sent it, but my neighbor's wind chimes achieved sentience and demanded I finish their memoir first, and I'm contractually obligated now." (146 chars) — Absurd; fails criterion 4 like the parrot.
10. "The deadline was in my other pants, along with my confidence, my keys, and the version of me who doesn't procrastinate." (123 chars) — Punchy list, great last item, but it is a joke *about* the deadline, not an excuse for missing it; criterion 1 is weak.
11. "I had it done, but then I proofread it and found I'd accidentally written a love letter to the printer, so I'm starting over out of respect." (143 chars) — Fresh and funny, but the excuse is thin: proofreading found a love letter? The premise strains belief.

## My own candidates (builder-authored)
12. "I finished it on time, then spent three days deciding whether 'on time' needed a hyphen, and the hyphen won." — Too meta/cute; the punch is a grammar joke, not an excuse.
13. "The deadline and I had a long talk and agreed to see other people, but I forgot to tell the deadline." — Clever, but again a joke about the deadline, not an excuse.
14. "I submitted it to the wrong deadline — there's a very confused poetry contest out there wondering why it got a spreadsheet." — Decent real excuse (wrong submission), but two-part structure and the punch is split.
15. "I kept it in drafts so long it legally qualifies as a vintage." — One-liner, but no real excuse and no turn; a quip, not a joke.
16. "My calendar marked the deadline as optional, and honestly I just believed it." — Close to the "time flew" stock family; weak.

## Pick rationale

**Picked #2:** "I did finish it, then reread it and had to go lie down in my car, so the work exists, it's just emotionally unavailable right now."

- (1) It *is* an excuse: the work is done but cannot be sent — the delay is explained, not just joked about.
- (2) Two turns: rereading your own work so hard you must lie down in your car, then the kicker that the work is "emotionally unavailable" — a phrase borrowed from relationships, applied to a document.
- (3) One sentence, reads cleanly aloud, punch ("emotionally unavailable right now") is the last clause.
- (4) Sounds like a real person cornered: "had to go lie down in my car" is exactly the kind of specific, slightly shameful detail a person volunteers when caught.
- (5) Fresh: no dog, no alarm, no traffic, no wifi, no "time flew"; the therapy-speak applied to a file is an angle not heard before.
- 130 characters, comfortably inside the 200-char gate.

Beats runner-up #6 (fonts) on freshness and on punch placement: the font joke's punch is "four days" (a duration), while #2's punch reframes the whole excuse. Beats runner-up #5 (apology-drafting) because #5's turn is self-referential meta-humor, while #2's turn is a concrete, visual, human scene.

## DeepSeek critic note

Two critique calls were attempted (deadline-critique, deadline-critique2, 1200/800 tokens, 3 retries each). Both failed: the 100milionseek provider answered HTTP 524/503 throughout this run (see ~/workspace/makefun/ds-brutal.log). Generation calls succeeded (11 candidates above); the critique-pick above is the builder's own, against the kit's published judge criteria, as the task allows ("with DeepSeek as critic where it answers").
