# Scam Shield — Report Card format

Shareable, screenshot-ready summary. Generate only when the user asks or accepts the offer after a verdict. One phone screenshot.

## Layout (top → bottom)

```
┌──────────────────────────────────────────┐
│  SCAM SHIELD          REPORT CARD        │
├──────────────────────────────────────────┤
│  VERDICT BANNER                          │
│  ████████  SCAM  ████████                │
│  (or LEGIT / UNSURE — same weight)       │
├──────────────────────────────────────────┤
│  SCAM TYPE                               │
│  Toll-road smishing                      │
│  Government imposter · unpaid-toll SMS   │
├──────────────────────────────────────────┤
│  RED FLAGS (exactly 3, quoted)           │
│  1. "Pay within 24 hours or your plate   │
│     will be suspended"                   │
│  2. "Tap to pay: https://bit.ly/         │
│     toll-pay-now"                        │
│  3. "DMV Enforcement Division"           │
├──────────────────────────────────────────┤
│  MONEY AT RISK                           │
│  Unknown — no payment made               │
├──────────────────────────────────────────┤
│  ACTIONS TAKEN                           │
│  • Forwarded to 7726                     │
│  • Reported to FTC                       │
│  (or: Verdict only — no filings yet)     │
├──────────────────────────────────────────┤
│  checked by Scam Shield                  │
│  github.com/LarryLemonBot/scam-shield    │
└──────────────────────────────────────────┘
```

Chat cards also print `Confidence: NN%` under the verdict. The shareable image banner is the verdict word; do not invent a percentage for the PNG if the live bot did not emit one.

## Field rules

| Field | Rule |
|-------|------|
| **Verdict banner** | One of `SCAM`, `LEGIT`, `UNSURE`. Loudest element. |
| **Scam type** | Short archetype + one clause of context (who they impersonate, or `none — message appears legitimate`). |
| **Red flags** | Exactly **three** quoted strings from the original message. If fewer than three hard flags exist, use the next-strongest real phrases or mark `weak signal`. Never invent quotes. |
| **Money at risk** | If no payment was made, write `Unknown — no payment made`. Never invent a dollar figure. You may quote a bait amount from the message as bait, not as a loss. A known loss only if the user said they paid. |
| **Actions taken** | Only YES-approved actions, or `Verdict only — no filings yet`. Never imply a filing that did not happen. Never invent an FTC reference number. |
| **Footer** | `checked by Scam Shield` plus `github.com/LarryLemonBot/scam-shield` |

## Text-only fallback (chat)

```markdown
## SCAM SHIELD REPORT CARD

**VERDICT:** SCAM
**Scam type:** Toll-road smishing — government imposter

**Red flags**
1. "Pay within 24 hours or your plate will be suspended"
2. "Tap to pay: https://bit.ly/toll-pay-now"
3. "DMV Enforcement Division"

**Money at risk:** Unknown — no payment made
**Actions taken:** Forwarded to 7726 · Reported to FTC

_checked by Scam Shield_
github.com/LarryLemonBot/scam-shield
```

If filings were not approved, replace actions with `Verdict only — no filings yet`.

## Sharing

Built to screenshot and post. Do not auto-post. Public sharing requires an explicit YES (human-gates.md).
