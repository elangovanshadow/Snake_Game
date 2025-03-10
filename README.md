# 🐍 Classic Snake Game

This is a simple implementation of the classic Snake Game using Python and the Turtle graphics library. The player controls a snake to eat food and grow in length while avoiding collisions with the wall or itself.

---

## 🎮 How to Play

- **Control the Snake**:
  - `Up Arrow` : Move Up
  - `Down Arrow` : Move Down
  - `Left Arrow` : Move Left
  - `Right Arrow` : Move Right

- **Objective**:
  - Eat the red food (🍎) to grow longer.
  - Avoid colliding with the walls.
  - Do not let the snake bite itself.

---

## 🚀 Features

- Object-Oriented Programming (OOP) design for modularity.
- Scoreboard tracking current score and high score.
- Snake resets on collision but retains high score (stored in `data.txt`).
- Easy to play and intuitive controls.

---

## 📝 Files Included

| File           | Description                                             |
|----------------|---------------------------------------------------------|
| `main.py`      | Main game loop and controls                             |
| `snake.py`     | Snake class handling snake body, movement, and reset    |
| `food.py`      | Food class managing the food appearance and position    |
| `scoreboard.py`| Scoreboard class displaying score and high score        |
| `data.txt`     | Stores the high score persistently                     |

---

## ▶️ How to Run the Game

1. Make sure you have **Python 3.x** installed on your computer.
2. Install **Turtle graphics** (comes pre-installed with Python).
3. Clone the repository or download the files.
4. Run `main.py`:
   ```bash
   python main.py
