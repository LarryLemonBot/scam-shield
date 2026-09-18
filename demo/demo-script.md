# Scam Shield — 60-second live demo

**What this is:** a shot list for a real screen recording of the real Scam Shield Grok Bot. No mock UI. No typed-in “bot” replies. No invented verdict, confidence, or dollar loss.

**The scam (eval #01, most universal):**

```
ALERT: Unpaid toll of $4.85 on I-95. Pay within 24 hours or your plate will be suspended. Tap to pay: https://bit.ly/toll-pay-now — DMV Enforcement Division
```

**Splices:** wherever this script says `[LIVE SPLICE]`, leave the take running and keep whatever the bot actually prints. If a take is long, crop silence — do not rewrite the text.

**Setup (off-camera):** Scam Shield bot open, composer empty, font large enough to read on a phone. Have `assets/report-card-example.png` ready for the card beat.

---

### 0:00–0:03 — Hook

**On screen:** the live bot window, composer focused.

**VO (over, first frame):** “This text is hitting phones everywhere.”

Hold. No logo sting. No captions yet.

---

### 0:03–0:12 — Paste the text

**Action:** paste the eval #01 string above into the composer. Do not paraphrase. Send.

**Camera:** stay on the chat. Show the outgoing bubble so the audience can read “DMV Enforcement Division” and the bit.ly link.

**VO (optional, under the paste):** “Fake toll. Fake DMV. One tap.”

---

### 0:12–0:28 — Verdict

**`[LIVE SPLICE]`** Wait for the real reply. Do not overlay a fake `VERDICT:` card.

**Hold on** the verdict block as soon as it appears (`SCAM` / `LEGIT` / `UNSURE` + confidence). If the bot streams, freeze the first complete verdict — not a mid-sentence frame.

**VO (only after the word is on screen):** “Scam Shield’s call.”

If this take is not `SCAM`, **do not ship it.** Re-run. Do not subtitle a different verdict over the footage.

---

### 0:28–0:42 — Three red flags

**`[LIVE SPLICE — same reply, no cut to a mock]`** Scroll inside the real message to the quoted flags.

**VO:** “Three traps. The deadline. The short link. The fake DMV.”

Point (cursor or finger) at whatever quotes the bot actually used. If it quoted fewer than three, hold what it gave — do not paste extra quotes on screen.

---

### 0:42–0:52 — Report Card reveal

**Action:** in the same chat, accept the Report Card offer (or type a short ask: `Report Card`). **`[LIVE SPLICE]`** the in-chat card if the bot emits one.

**Then cut to** `assets/report-card-example.png` (full frame, ~1.5s). That PNG is the shareable example for this same toll-road text: verdict **SCAM**, type **Toll-road smishing**, three quotes from eval #01, money **Unknown — no payment made**, actions **Forwarded to 7726** / **Reported to FTC**.

Do not swap in a different card. Do not add a dollar loss. If the live chat card disagrees with the PNG, ship the live card and drop the PNG from that take.

---

### 0:52–1:00 — Close + contest hook

**On screen:** hold the Report Card. Last frames can super the bot handle once it exists.

**VO:** “I made a Grok Bot that catches scams before they catch you. Forward the text. Get the verdict. Get the evidence pack to report it — 7726, FTC — only if you type YES.”

**End card (one line, ~1s):** `Clone Scam Shield → github.com/LarryLemonBot/scam-shield`

Cut to black at 1:00. No extra claims, no FTC reference numbers, no “we saved $X.”
