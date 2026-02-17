#  Anime Rating Higher-Lower Game

A Python command-line game where you test your knowledge of anime popularity! Guess which of two anime has a higher rating and build your high score.

##  Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [File Setup (Crucial Step)](#file-setup)
- [How to Run](#how-to-run)
- [How to Play](#how-to-play)

##  Features
- **Endless Gameplay:** The game continues as long as you guess correctly.
- **Score Tracking:** Keeps track of your current winning streak.
- **Dynamic Comparison:** The winner of the previous round stays to face a new challenger.

##  Prerequisites
- **Python 3.x** installed on your system.

##  File Setup
This game relies on two external files to work (`data.py` and `art.py`). Ensure your project folder looks like this:

    /AnimeGame
      ├── main.py    (Paste your game code here)
      ├── data.py    (Contains the list of anime)
      └── art.py     (Contains the ASCII art)


## How to Run
Open your terminal or command prompt.
Navigate to the folder containing your files.

## Run the game:
Bash
```python main.py```

## How to Play
1. The game will present two Anime options (A and B).
2. You will see their Name, Episode Count, and Creator.
3. You must guess which one has the Higher Rating.
4. Type 'A' or 'B' and hit Enter.
5. If you are correct, you get a point and the game continues.
6. If you are wrong, the game ends and shows your final score.