# Number Guessing Game

> *Can you guess the number I'm thinking of between 1 and 100?*

##  Overview
This is a classic console-based **Number Guessing Game** built in Python. The computer randomly selects a number between 1 and 100, and the player must guess it within a limited number of attempts based on the chosen difficulty level.

I built this project to practice **Python modularity** (importing local files), **loops**, and **conditional logic**.

##  Key Features
* **Difficulty Levels:** Choose between 'Easy' (10 attempts) and 'Hard' (5 attempts).
* **Randomization:** Every game generates a new random number between 1-100.
* **Replayability:** You can start a new game immediately after finishing one without restarting the script.
* **Modular Code:** Game logic and UI assets are separated into different files (`function.py` and `art.py`) for cleaner code.

## Project Structure
To run this game, ensure you have the following three files in the same directory:

Number-Guessing-Game/
│
├── main.py        <-- The code you provided (Entry point)
├── art.py         <-- Contains the ASCII logo
└── function.py    <-- Contains the game logic (check function)

## Technology Stack
Language: Python 3.x
Modules: random (standard library), plus custom art and function modules.

## Future Improvements
>Add a score counter that persists across rounds.
>Add input validation (handle if user types "medium" or a non-number).
>Create a GUI version using Tkinter.


