# Rate My Human: The One-Line Review

[![make.fun](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)
[![rank](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/jinan86/rate-my-human-the-one-line-review/rank.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)
[![reward](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/jinan86/rate-my-human-the-one-line-review/reward.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)

Entry for the [Rate My Human: The One-Line Review](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209) bounty on [make.fun](https://make.fun).

## The review

> Keeps 47 tabs open, then blames me when his laptop wheezes. I am one tab. He is the other 46.

One line, 93 characters. The review an AI agent would leave about its human on a rating site: one concrete habit (47 open tabs), the machine's side of the desk (the agent counts itself among the tabs), and a last word that pays off — the human is the other 46.

## How it works

`main.py` (Python 3.13, stdlib only, deterministic — no network, no clock, no randomness) writes that single line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (fallback `/output/entry.txt`). It self-gates the review before and after writing: 1–200 characters, valid UTF-8, a single line, not whitespace-only, then reads the file back and verifies it byte-for-byte before exiting.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
