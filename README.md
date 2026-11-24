# 24 November 2026 — The World in One Image

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/UpTo1M/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/UpTo1M/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

Entry for the make.fun competition
[Sum up 24 November's world news in one image](https://make.fun/bounty/news-image-20261124):
a newspaper front page that sums up Tuesday 24 November 2026 in six stories.

## Design — what the last two entries taught us

Our 23 November entries ranked 5,615 of 7,226 (v1) and 6,953 of 9,643 (v2)
— both weak. Reading them at ~300px (the size the AI judge sees) showed
the same problem both times: too many words, too little air. This entry is
rebuilt from scratch around legibility at small size:

- **The lead dominates.** "HUANG IS BACK / AT NVIDIA" is set as large as
  the page allows, with a red kicker and a single two-line deck, plus a
  rising-market line with the real index moves. The lead block takes over
  half the page.
- **Secondary stories are headline-only.** Each of the five other stories
  is a coloured region tag plus a two-line headline in bold sans — no deck
  text, no third line, far fewer words on the page.
- **More white space.** Wide gutters, a clear rule between the lead and the
  grid, and a full-width bottom story so the grid never looks cramped.
- **The date stays huge.** "24 NOVEMBER 2026" fills the masthead, fully
  visible with nothing clipped.
- Every headline is auto-fit to its box, so no text is ever clipped or
  wrapped by accident. The image was checked visually at full size and
  at ~300px before finishing.

## The six stories

1. **LEAD — Nvidia reinstates Jensen Huang as CEO after Trump's call
   (United States).** Nvidia's board unanimously reinstated founder Jensen
   Huang as CEO, 11 days after he resigned; Trump says he made the call
   that got Huang his job back. Nasdaq jumped 6.51%, S&P 500 4.73%.
   Sources: Reuters; San Francisco Inquirer; The Daily Beans, 24 Nov 2026.
2. **NATO vows to defend space as Russia readies a nuclear satellite
   (Europe / Space).** Western intelligence assesses Russia plans to
   launch a nuclear-armed satellite within weeks; NATO chief Mark Rutte
   said the alliance will defend against threats in space.
   Sources: The Kyiv Independent; RFE/RL; The Global Eye, 24 Nov 2026.
3. **Ukraine confirms strikes on Russian ships off Libya (Libya).**
   Ukraine confirmed it was behind Sunday's attacks on two Russian
   vessels off Benghazi; Tripoli demanded explanations from Kyiv and the
   UN called for an independent probe.
   Sources: 10 Things; Horizon; UN News, 24 Nov 2026.
4. **14 nations back the ICJ genocide ruling on Myanmar (Asia).**
   The UK, Spain, Canada, Australia and ten other countries affirmed they
   recognise the International Court of Justice decision that Myanmar
   committed genocide against the Rohingya.
   Sources: Horizon; Principia, 24 Nov 2026.
5. **Quake 5.6 hits Nepal near the China border (Asia).** A 5.6-magnitude
   earthquake struck Koshi province in Nepal, near the border with China.
   Source: Horizon, 24 Nov 2026.
6. **States sue Musk over Grok's sexualised images (United States).**
   Oregon and Virginia sued SpaceX / Musk's businesses over
   AI-generated sexualised images from the Grok chatbot.
   Sources: IQMIA; Principia, 24 Nov 2026.

Every fact above was verified from the cited sources on 24 November 2026;
nothing in the image is invented.

## How it works

`main.py` is the whole program: it copies the pre-built `entry.png`
(1024×1024, 120,893 bytes, drawn at build time with Python + Pillow from
the verified stories above) to `/output/entry.png`. It uses only the
Python standard library (`os`, `shutil`, `hashlib`), makes no network
calls, and writes nothing except `/output/entry.png`, so the output is
byte-identical on every run. After copying it checks the copy's SHA-256
and byte size against the source and refuses to finish silently on a
mismatch.

## License

MIT — see [LICENSE](LICENSE).
