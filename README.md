# Scam Shield

> I made a Grok Bot that catches scams before they catch you.

Paste any sketchy text, email, or DM. Scam Shield returns an instant verdict — **scam / legit / unsure** — with the red flags explained in plain English. Then it **closes the loop**: with your explicit OK, it prepares an evidence pack for FTC and carrier (7726) spam reports, logs the hit, and can send a weekly digest of what's targeting you.

## What it does / what it doesn't

**It does:**
- ✅ Read a message you paste (or a screenshot you attach) and give a clear verdict
- ✅ Quote the exact red flags and explain the trick simply
- ✅ Make a shareable Report Card for warning friends and family
- ✅ Prepare a ready-to-submit evidence pack for 7726 / FTC reports

**It doesn't:**
- ❌ Have a phone number — you can't forward texts to it; you paste or attach the message in the chat
- ❌ File reports or contact anyone on its own — every external action needs your YES, every time
- ❌ Ask for passwords, bank logins, or your SSN — ever
- ❌ See your other messages, contacts, or photos

**Easiest way to use it:** copy the text, run the [one-tap iOS Shortcut](ios-shortcut/setup.md), paste, send.

## How it works

1. **Paste** a suspicious message (or attach a screenshot).
2. **Get a verdict** — classification, confidence, named scam archetype, quoted red flags, and a grandparent-plain explanation.
3. **Get three next steps** — most urgent first (ignore / block / report / verify through official channels).
4. **Approve or decline** any external action. Nothing is filed, sent, or emailed without you typing **YES**.
5. **Share the Report Card** — a screenshot-ready card built for posting: verdict, scam type, red flags, money at risk, actions taken.

## Why it exists

Scam losses keep climbing year over year. Imposter scams are among the most-reported frauds, and the **text message** is the #1 contact method. Nobody owns the "paste the sketchy text → verdict → report it" loop. Scam Shield does.

## Contest entry

- **Contest:** [xAI Grok Bot Sharing Contest](https://x.ai) · Sep 15–29, 2026
- **Deadline:** Tuesday, September 29, 2026
- **Entry post draft:** [`entry/contest-post.md`](entry/contest-post.md)
- **Grok Bot template:** *coming soon* — link will land here once the template is published

## Repo structure

```
scam-shield/
├── README.md
├── bot-template/
│   ├── system-prompt.md       # full Grok Bot template prompt
│   ├── report-card-format.md  # shareable Report Card spec
│   └── human-gates.md         # approval policy (YES every time)
├── eval/
│   └── scam-corpus.md         # 30 realistic 2026 scam texts + expected verdicts
├── assets/                    # report-card-example.png after demo recording
└── entry/
    └── contest-post.md        # contest entry post for X
```

## Trust design

Scam Shield **never** asks for passwords, bank logins, or SSN. It **never** sends money. It **never** contacts carriers, the FTC, or anyone else without an explicit **YES** from you — every single time.

## License

Public contest entry. Use, fork, and adapt freely for personal protection tooling.
