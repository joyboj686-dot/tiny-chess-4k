# tiny-chess-4k

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/joyboj686-dot/tiny-chess-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/joyboj686-dot/tiny-chess-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

Tiny chess engine in 4 KB of Python: 0x88 movegen, alpha-beta with iterative deepening, tapered eval, persistent transposition table, MVV-LVA ordering, quiescence, check extensions, castling and en passant. Practice trials: v4 mean Elo ~1,247.

## Run it

```sh
python3 main.py
```

`main.py` is the whole engine: at most 4,096 bytes as committed, Python 3.13, standard library only. It plays through the env server and searches to a fixed node count, never a clock, so trials replay exactly.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
