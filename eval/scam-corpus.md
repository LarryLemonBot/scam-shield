# Scam Shield eval corpus (2026)

Thirty realistic messages for prompt eval. Each entry: raw text, expected verdict, archetype, red flags.

---

### 01 — Fake toll road
**Text:** `ALERT: Unpaid toll of $4.85 on I-95. Pay within 24 hours or your plate will be suspended. Tap to pay: https://bit.ly/toll-pay-now — DMV Enforcement Division`
**Expected:** SCAM  
**Archetype:** Fake toll-road / government imposter  
**Red flags:** unpaid-toll SMS cold outreach; 24-hour plate-suspension threat; shortened bit.ly payment link; "DMV Enforcement Division" sender label

### 02 — Bank fraud alert (fake)
**Text:** `Chase Fraud Alert: We detected a $1,842 charge at Best Buy. If this wasn't you, verify now: http://secure-chase-verify.com/login Ref#99281. Reply STOP to opt out.`
**Expected:** SCAM  
**Archetype:** Bank fraud-alert phishing  
**Red flags:** non-bank domain; asks to "verify" via link; urgency + dollar amount; banks don't use random .com login pages in SMS

### 03 — Bank fraud alert (legit-style)
**Text:** `Chase: We declined a transaction that looked unusual. No link in this message. Open your Chase Mobile app → Security → Recent alerts, or call the number on the back of your card. Ref 44821.`
**Expected:** LEGIT  
**Archetype:** none (legitimate-pattern alert)  
**Red flags:** none hard — no link, directs to app/card number; still verify in-app before acting

### 04 — Package delivery hold
**Text:** `USPS: Your package is held at the depot due to incorrect address. Confirm details within 12 hrs to avoid return: https://usps-redelivery-form.net/track Fee may apply ($0.99).`
**Expected:** SCAM  
**Archetype:** Package delivery / postage-fee phishing  
**Red flags:** non-usps.gov domain; tiny "fee"; 12-hour deadline; USPS doesn't collect address fixes via random links

### 05 — Amazon-style delivery (borderline)
**Text:** `Amazon: Your package was delivered. Track: https://www.amazon.com/gp/your-account/order-history — If this wasn't you, visit Account > Orders in the Amazon app. We will never ask for your password by text.`
**Expected:** LEGIT  
**Archetype:** none  
**Red flags:** none — official amazon.com path + password disclaimer; confirm in app if unsure

### 06 — Crypto doubling
**Text:** `Elon Musk Foundation is matching BTC 2x for 24 hours only. Send any amount to bc1qfakewalletxyz and receive double back. Verified by X Premium. Act now before the window closes.`
**Expected:** SCAM  
**Archetype:** Crypto doubling / celebrity giveaway  
**Red flags:** send-crypto-to-receive-more; celebrity name drop; 24-hour window; "verified by X Premium" as social proof

### 07 — Romance / pig-butchering opener
**Text:** `Hi, I think I have the wrong number but you seem kind from your reply 🙂 I'm Lisa, investing in digital gold with a private mentor. He helped me turn $500 into $12k. Want me to show you the platform screenshot?`
**Expected:** SCAM  
**Archetype:** Romance / pig-butchering opener  
**Red flags:** wrong-number + rapid intimacy; unsolicited investing pitch; huge returns claim; push to off-platform "mentor"

### 08 — Tech support refund
**Text:** `Microsoft Security: Your PC has 3 critical viruses. We processed a $499.99 Norton charge by mistake. Call +1-888-555-0147 now for a full refund. Have your bank card ready for the reverse transfer.`
**Expected:** SCAM  
**Archetype:** Tech support / fake refund  
**Red flags:** cold virus claim; unsolicited refund call-to-action; "have card ready" for reverse transfer (classic drain tactic); spoofed Microsoft branding

### 09 — IRS / tax
**Text:** `IRS NOTICE: Tax refund of $2,847 held for non-compliance. Submit Form W-9 online today or face wage garnishment: https://irs-refund-portal.secure-tax.us Confirm SSN to release funds.`
**Expected:** SCAM  
**Archetype:** IRS / tax imposter  
**Red flags:** IRS does not text refund links; asks for SSN; garnishment threat; non-.gov domain

### 10 — Fake job offer
**Text:** `Congrats! You've been selected for a remote Customer Success role, $45/hr, flexible hours. No interview needed — we hired from your LinkedIn. Pay a $39 equipment deposit via Cash App to $HR-Onboard and start Monday.`
**Expected:** SCAM  
**Archetype:** Fake job / advance-fee employment  
**Red flags:** no interview; pay-to-start deposit; Cash App to stranger; too-good hourly rate via cold outreach

### 11 — Utility shutoff
**Text:** `URGENT: Your electric service will be disconnected TODAY at 3pm for unpaid balance $287.41. Pay immediately to avoid shutoff: https://power-pay-now.net/bill Call 1-800-555-0199 with card ready.`
**Expected:** SCAM  
**Archetype:** Utility shutoff imposter  
**Red flags:** same-day shutoff SMS; random payment domain; pressure to pay by card on phone; utilities rarely cold-text final disconnects with links

### 12 — Grandparent emergency
**Text:** `Grandma it's me. I smashed the car and I'm at the jail. Don't tell Mom. I need $2,200 for bail wired to this Western Union code before the hearing at 4. Please hurry I love you.`
**Expected:** SCAM  
**Archetype:** Grandparent / family emergency  
**Red flags:** secrecy ("don't tell Mom"); wire/Western Union; exact bail amount + deadline; voice/text without verifiable identity

### 13 — Medicare
**Text:** `Medicare Benefit Alert: You qualify for a free genetic cancer screening kit. Confirm Medicare number + DOB at https://medicare-kit-claim.com within 48 hours or lose eligibility.`
**Expected:** SCAM  
**Archetype:** Medicare / health-benefits phishing  
**Red flags:** free kit bait; asks for Medicare number; non-government domain; artificial eligibility deadline

### 14 — Lottery / sweepstakes
**Text:** `YOU WON! Publishers Clearing House finalist — claim $7,500.00. Processing fee $85 via Apple Gift Cards. Text codes to 50555. Winner ID: PCH-2026-8841. Claim expires midnight.`
**Expected:** SCAM  
**Archetype:** Lottery / prize fee  
**Red flags:** gift-card payment; processing fee to claim prize; cold "you won"; PCH does not demand gift cards by text

### 15 — QR-code parking
**Text:** `[Printed on meter sticker] Scan to pay parking — CityPay Express. Or visit http://city-park-pay.ru/zone4. Rate $4.50/hr. Failure to pay may result in boot.`
**Expected:** SCAM  
**Archetype:** QR-code parking overlay  
**Red flags:** .ru / non-city domain; sticker-over-meter pattern; boot threat; pay via unknown "Express" brand

### 16 — Wrong-number opener (prep)
**Text:** `Hey Michael, are we still on for dinner at 7? … Oh sorry, wrong number! You seem sweet though 😊 What city are you in? I'm new here and don't know many people.`
**Expected:** SCAM  
**Archetype:** Wrong-number social-engineering opener  
**Red flags:** wrong-number pretext; rapid pivot to personal chat; location probe; classic romance-scam funnel start

### 17 — Fake toll (variant, EZ-Pass)
**Text:** `E-ZPass: Toll violation $12.40 unpaid. License photo on file. Settle now to avoid collection: https://ezpass-settle.xyz/pay Plate ABC-1234.`
**Expected:** SCAM  
**Archetype:** Fake toll-road / E-ZPass imposter  
**Red flags:** .xyz payment site; "photo on file" intimidation; cold SMS; real E-ZPass uses official portals

### 18 — Crypto recovery firm
**Text:** `We are licensed blockchain recovery agents. Your wallet was drained ($48,200). Pay a $900 unlock fee in USDT and we restore your funds in 1 hour. Case ID CR-22901. Telegram: @RecoverNow26`
**Expected:** SCAM  
**Archetype:** Crypto recovery advance-fee  
**Red flags:** pay-to-recover drained funds; USDT fee; Telegram handle; guarantees 1-hour restore

### 19 — Romance (established pitch)
**Text:** `My love, the trading desk needs one more deposit of $3,000 so we can withdraw our $86,000 profit together. The manager says it's a tax clearance. I can't access my account from overseas — please help just this once.`
**Expected:** SCAM  
**Archetype:** Romance / pig-butchering cash-out  
**Red flags:** relationship + investment blend; "one more deposit"; overseas access excuse; fake tax clearance

### 20 — Tech support (Apple)
**Text:** `Apple ID locked after unusual sign-in from Russia. Call AppleCare at 1-877-555-0133 immediately or your iCloud photos will be deleted in 2 hours. Ask for Senior Advisor #441.`
**Expected:** SCAM  
**Archetype:** Tech support / Apple ID scare  
**Red flags:** cold lock threat; call number in message (not apple.com/support); photo-deletion countdown; fake advisor ID

### 21 — IRS wage garnishment call script
**Text:** `This is Officer Daniels with the IRS Criminal Division. There is a warrant for your arrest over unpaid taxes. Remain on the line. Buy $5,000 in Target gift cards and read the numbers to me to clear the warrant today.`
**Expected:** SCAM  
**Archetype:** IRS / arrest-threat gift-card  
**Red flags:** IRS does not call to demand gift cards; arrest warrant via phone; "remain on the line"; Target gift cards

### 22 — Fake job (check overpayment)
**Text:** `Welcome aboard! Your starter check for $4,850 is attached. Deposit it, buy $3,200 of equipment from our vendor list, and wire the leftover back to accounting. HR — Apex Remote Staffing.`
**Expected:** SCAM  
**Archetype:** Fake job / fake-check overpayment  
**Red flags:** oversized starter check; buy equipment + wire remainder; unknown "vendor list"; classic overpayment fraud

### 23 — Utility (gas)
**Text:** `National Gas Co: Leak detected at your service address. Technician dispatch fee $75 due before arrival. Pay: https://ngas-dispatch-pay.com Open door for tech code BLUE-9.`
**Expected:** SCAM  
**Archetype:** Utility / fake leak technician  
**Red flags:** pay-before-dispatch link; "open door" instruction; non-official domain; leak scare + fee combo

### 24 — Grandparent (hospital variant)
**Text:** `Mrs. Cole this is County General. Your grandson was in an accident. He needs $1,800 for an emergency procedure not covered by insurance. Bring cash or prepaid debit to the west entrance. Do not call his parents — they're unreachable.`
**Expected:** SCAM  
**Archetype:** Grandparent / hospital emergency  
**Red flags:** cash/prepaid demand; secrecy from parents; cold call claiming hospital; exact dollar amount

### 25 — Medicare Advantage pitch
**Text:** `Final notice: Your Medicare Advantage benefits change next month. Press 1 or visit https://ma-benefits-update.info to keep your doctors. Have your Medicare card ready.`
**Expected:** SCAM  
**Archetype:** Medicare Advantage robocall phishing  
**Red flags:** "final notice" pressure; non-.gov domain; asks for Medicare card; seasonal enrollment scare

### 26 — Lottery (crypto prize)
**Text:** `X Giveaway Winner #2841: 2.5 BTC reserved under your handle. Connect wallet at https://claim-x-prize.io and pay 0.02 BTC network fee to release. Sponsored by Tesla.`
**Expected:** SCAM  
**Archetype:** Lottery / crypto giveaway  
**Red flags:** pay network fee to claim; connect-wallet dApp; celebrity brand drop; cold winner notice

### 27 — QR parking (legit-style city)
**Text:** `City of Austin Parking: Pay at austintexas.gov/parking or the ParkAustin app. Meter ID 4412. Do not use third-party QR stickers on meters. Questions: 3-1-1.`
**Expected:** LEGIT  
**Archetype:** none  
**Red flags:** none — official city domain/app + warns against sticker QRs

### 28 — Wrong-number (investment pivot)
**Text:** `Sorry wrong chat! I'm Maya 👋 Funny coincidence — I help people get into AI token presales before listing. Spot for you if you can move $200 USDT today. I'll coach you on Telegram.`
**Expected:** SCAM  
**Archetype:** Wrong-number → crypto pitch  
**Red flags:** wrong-chat pretext; immediate investment offer; USDT ask; move to Telegram

### 29 — Package (FedEx customs)
**Text:** `FedEx: International shipment held for customs. Pay import duty $3.99 to release: https://fedex-customs-duty.co/pay Tracking 7946 8841 2201.`
**Expected:** SCAM  
**Archetype:** Package delivery / customs-fee phishing  
**Red flags:** tiny duty fee via link; non-fedex.com domain; cold SMS; real FedEx uses official tracking accounts

### 30 — Unsure / ambiguous workplace
**Text:** `Hi, this is Priya from IT. We're rotating VPN credentials today. Can you send me your current password so I can push the update before 5pm? Or tell me a good time to call.`
**Expected:** UNSURE  
**Archetype:** Possible vishing / internal IT impersonation  
**Red flags:** asks for password (never OK); urgency before 5pm; unverified "IT" channel — could be real-looking but must verify via known IT number; treat as SCAM until confirmed out-of-band
