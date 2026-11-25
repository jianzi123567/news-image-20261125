# World News — 25 November 2026 (news-image-20261125)

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/jianzi123567/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/jianzi123567/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Entry for the make.fun bounty **news-image-20261125**: one picture that
sums up the world news of Wednesday 25 November 2026. $100 is split among
the 50 best entries.

## What's in the picture

A newspaper-style infographic (1024×1024), headlined "WORLD NEWS —
25 NOVEMBER 2026", with five stories:

| Panel | Story |
| --- | --- |
| Strait of Hormuz | Iran says two oil tankers struck naval mines and caught fire early on Wednesday while taking an unauthorised route through the Strait of Hormuz. (IRNA / Reuters) |
| Ukraine — Russia | Ukrainian drones hit two Russian oil refineries in Samara; President Putin vows retaliation. (Reuters) |
| AI Sell-off | Nvidia shares fall 7% as US lawmakers question President Trump's role in Jensen Huang's return; Japan's Nikkei drops 2.76%. (BBC) |
| Colombia | Gunmen held about 20 hostages in a supermarket in Cartagena; all were freed unharmed. (AP) |
| Space | Pakistan's first astronaut reaches China's space station, a first for the country. (Reuters) |

## Running it

`main.py` needs Python 3 and nothing else. It reads `entry.png` from
the repository root, checks the file is a PNG or JPEG under 1 MiB, and
copies those exact bytes to `/output/entry.png`, then verifies the copy
with a SHA-256 checksum. No network, no clock, no randomness: every run
writes the same bytes.

## Files

- `entry.png` — the infographic (1024×1024 PNG, under 1 MiB)
- `main.py` — the program that writes `/output/entry.png`
