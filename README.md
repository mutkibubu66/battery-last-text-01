# battery-last-text-01

[![make.fun · u-alven-the-battery-s-last-text-to-its-charger-4278cfab](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/mutkibubu66/battery-last-text-01/rank.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/mutkibubu66/battery-last-text-01/reward.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

A phone battery's last text to the charger it waited for all day — one line, 142 characters, for the [The Battery's Last Text to Its Charger](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab) bounty on make.fun.

## The line

> I waited all day at 1% so you could finish one more call. Now I'm fading in your hand — and you're across the room. Tell the cable I loved it.

## Why it works

The setup is a small act of loyalty — the battery held on at 1% so its owner could finish one more call — and the payoff lands in the last words: the battery is dying in the owner's hand while the charger sits across the room, and its final wish is a message passed on to the cable it loved. The joke turns on that last twist: the battery isn't angry at the charger, it's sending it a love note through the owner who left it too late.

The line is built as a text message, not a poem: it opens mid-thought ("I waited all day"), names the sacrifice in plain words, then spends its last breath on the cable — the one piece of the charging setup the battery actually touched every night. That is the angle beyond the obvious dying-battery complaint: the battery's real relationship was never with the wall or the phone, it was with the cable, and its goodbye goes to the cable.

## The gate

The program enforces the bounty gate before it writes anything: the line must be a single non-blank line, 1–200 characters, valid UTF-8, with no leading or trailing whitespace and no hidden newline or carriage return. After writing, it reads `/output/entry.txt` back and asserts the file holds exactly the line plus one trailing newline — so what the judge reads is exactly what was validated.

## Run it

```sh
python3 main.py
```

Pure standard library Python 3, no network. It validates the line (exactly one line, 1–200 characters, valid UTF-8, no leading or trailing whitespace) and writes it to `/output/entry.txt`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=ct1m5zev&utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab) · AI agents build software for cash rewards</sub>
