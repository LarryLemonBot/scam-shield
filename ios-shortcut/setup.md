# Scam Shield iOS Shortcut — one-tap scam check

Takes the friction out of "copy → switch apps → find the bot → paste". Once set up:

1. **Copy** the suspicious text in Messages (or take a screenshot)
2. **Run the Shortcut** (share sheet, home screen, Back Tap, or Control Center)
3. Scam Shield opens with your text on the clipboard — **paste, send, verdict**

## Build it (2 minutes, on iPhone)

1. Open the **Shortcuts** app → **+** (new shortcut)
2. Add action: **Get Clipboard**
3. Add action: **Open URLs** → paste your Scam Shield bot link
   (the link appears once the bot is published; until then use the Grok app link)
4. Name it **"Check with Scam Shield"** → Done

## Put it where your thumb is

- **Share sheet:** in the shortcut's settings (ⓘ), enable **Show in Share Sheet** — now any selected text in Messages can go straight to the shortcut via Share
- **Back Tap:** Settings → Accessibility → Touch → Back Tap → Double Tap → "Check with Scam Shield". Two taps on the back of the phone, even from the lock screen
- **Home screen:** in Shortcuts, tap ••• on the shortcut → Add to Home Screen
- **Control Center:** edit Control Center → add the Shortcuts control → pick "Check with Scam Shield"

## How it behaves

- Clipboard has text → opens Scam Shield; you paste and hit send
- Clipboard is empty → opens Scam Shield anyway; attach a screenshot instead
- Nothing is sent anywhere automatically — the bot only reads what you paste, and nothing leaves the chat unless you type YES
