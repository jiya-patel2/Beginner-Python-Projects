# 🗿 📄 ✂️ Stone Paper Scissor Game

A simple, interactive command-line implementation of the classic "Rock, Paper, Scissors" game written in Python. Play against the computer, track your score, and race to a set number of points to win!


##  Features
- **User Customization:** Enter your player name.
- **Custom Winning Condition:** You decide how many points are needed to win the match (e.g., First to 3 wins).
- **Score Tracking:** The game tracks both user and computer scores in real-time.
- **Randomized Opponent:** The computer makes random moves using Python's `random` module.

##  Prerequisites
You need to have Python installed on your machine to run this game.
- **Python 3.x** (Recommended)

To check if Python is installed, open your terminal or command prompt and run:
```bash
python --version

## 🚀 How to Run
1. Save the code in a file named game.py (or any name you prefer).

2. Open your terminal or command prompt.

3. Navigate to the folder where you saved the file.

4. Run the following command:

```bash
python game.py
## 🎮 How to Play
1. Start the Game: Run the script.

2. Setup: - Enter your Name.

3. Enter the Points required to win (e.g., 3 for a "Best of 5" style match).

4. Gameplay: - When prompted, type your move.

##Important: Input is case-sensitive. You must type exactly one of these options:
Rock
Paper
Scissor
Winning: The game continues until either you or the computer reaches the target score defined in step 2.


...
##  Game Rules
The winner is decided based on standard rules:
Rock crushes Scissor
Scissor cuts Paper
Paper covers Rock
Same choice results in a Tie

##  ⚠️ Notes
Ensure you capitalize the first letter of your move (e.g., Rock not rock), otherwise the game will return "Invalid choice".