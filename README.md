# IM Chess Rating System

A small command-line program that tracks player ratings using the [Elo rating system](https://en.wikipedia.org/wiki/Elo_rating_system). Built for learning and practice—record match results and see ratings update automatically.

## Features

- **Elo calculations** — Expected score and post-match rating updates with a K-factor of 40
- **Persistent storage** — Ratings saved to `ratings.txt` and reloaded on each run
- **New players** — Unknown names start at **1000** and are added after their first match
- **Leaderboard** — Players sorted by rating when the file is saved
- **Confirmation step** — Review the result before ratings change

## Requirements

- Python 3.6+
- No third-party packages

## Quick start

```bash
python "im chess rating system.py"
```

On first run, `ratings.txt` is created when you save a match.

## How to use

1. Enter names for **Player 1** and **Player 2** (stored in uppercase).
2. View their current ratings (or 1000 if they are new).
3. Enter the result **from Player 1’s perspective**:
   - `1` — Player 1 wins
   - `0.5` — Draw
   - `0` — Player 1 loses
4. Confirm with `y` to apply the update, or `n` to cancel.
5. Choose **Y** to record another match or **N** to exit.

### Example session

```
Enter Player 1 name: Alice
Enter Player 2 name: Bob

Current Ratings:
ALICE: 1000
BOB: 1000

Enter result from Player 1's perspective (1 = win, 0.5 = draw, 0 = loss):
ALICE vs BOB: 1

Confirm: ALICE scored 1.0 vs BOB — Sure ALICE WON? (y/n): y

Updated Ratings:
ALICE: 1020.0
BOB: 980.0
```

## Rating formula

For each player after a match:

```
new_rating = old_rating + K × (actual_score − expected_score)
```

- **K** = 40 (how much ratings can swing per game)
- **Expected score** = `1 / (1 + 10^((opponent_rating − player_rating) / 400))`
- **Actual score** = 1 (win), 0.5 (draw), or 0 (loss)

Player 2’s score is always `1 − Player 1’s score`.

## Data file (`ratings.txt`)

The program reads and writes a plain-text table:

```
NO  PLAYER         RATING
1   ALICE          1020.00
2   BOB            980.00
```

- The first line is a header and is skipped when loading.
- Each data row: rank number, player name, rating (space-separated).
- If the file is missing, the program starts with an empty rating list.

## Project structure

```
im-chess-system/
├── im chess rating system.py   # Main script (CLI + Elo logic)
├── ratings.txt                 # Created at runtime (player data)
└── README.md
```

## Notes

- Names are normalized to **uppercase** in storage and lookups.
- Cancelling a match (`n` at confirmation) exits the program without saving.
- This is a study project: single file, no tests or API—suitable for experimenting with rating math and simple file I/O.

## License

No license specified—treat as personal/educational use unless you add one.
