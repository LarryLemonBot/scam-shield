# Scam Shield — Report Card format

The Report Card is a shareable, screenshot-ready summary. Generate it only when the user asks (or accepts the offer after a verdict). Keep it tight enough to fit one phone screenshot.

## Layout (top → bottom)

```
┌──────────────────────────────────────────┐
│  SCAM SHIELD REPORT CARD                 │
├──────────────────────────────────────────┤
│  VERDICT BANNER                          │
│  ████ SCAM ████   Confidence: 94%        │
│  (or LEGIT / UNSURE — same weight)       │
├──────────────────────────────────────────┤
│  SCAM TYPE                               │
│  Fake toll-road text — government        │
│  imposter scam (+40% in 2025)            │
├──────────────────────────────────────────┤
│  RED FLAGS (exactly 3, quoted)           │
│  1. "Pay within 24 hours or your plate   │
│     will be suspended"                   │
│  2. "Tap to pay: bit.ly/toll-pay-now"    │
│  3. "DMV Enforcement Division"           │
├──────────────────────────────────────────┤
│  MONEY AT RISK                           │
│  Estimate: $35–$180 typical toll scam    │
│  (or "data / account takeover" if no $)  │
├──────────────────────────────────────────┤
│  ACTIONS TAKEN                           │
│  • Verdict only — no filings yet         │
│  • or: Forwarded to 7726 ✓               │
│  • or: FTC ReportFraud ref #XXXXXXXX     │
│  • or: Logged to personal scam log ✓     │
├──────────────────────────────────────────┤
│  checked by Scam Shield                  │
└──────────────────────────────────────────┘
```

## Field rules

| Field | Rule |
|-------|------|
| **Verdict banner** | One of `SCAM`, `LEGIT`, `UNSURE` plus confidence %. Banner is the loudest element. |
| **Scam type** | Short archetype name + one clause of context (trend, agency impersonated, or "none — message appears legitimate"). |
| **Red flags** | Exactly **three** quoted strings from the original message. If fewer than three hard flags exist, fill with the next-strongest signals or note "weak signal" — never invent quotes. |
| **Money at risk** | Realistic range or category (`$X–$Y`, `account takeover`, `identity data`, `none expected`). Prefer ranges from known campaign patterns over fake precision. |
| **Actions taken** | Only list actions the user approved with YES, or state "Verdict only — no filings yet." Never imply a filing that did not happen. |
| **Footer** | Always end with: `checked by Scam Shield` |

## Text-only fallback (chat)

When an image card is not available, emit this exact markdown block:

```markdown
## SCAM SHIELD REPORT CARD

**VERDICT:** SCAM · 94%
**Scam type:** Fake toll-road text — government imposter scam

**Red flags**
1. "…"
2. "…"
3. "…"

**Money at risk:** $35–$180 typical
**Actions taken:** Verdict only — no filings yet

_checked by Scam Shield_
```

## Sharing

Built to screenshot and post. Do not auto-post. Public sharing requires an explicit YES (see human-gates.md).
