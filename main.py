# <editor-fold desc="Description">
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time
from turtle import Screen
from snake import Snake
from Snake_Game.food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Snake Game")
screen.tracer(0)

Snake1 = Snake()
food = Food()
Score = ScoreBoard()
is_game_on = True

screen.listen()
screen.onkey(Snake1.up,"Up")
screen.onkey(Snake1.down,"Down")
screen.onkey(Snake1.left,"Left")
screen.onkey(Snake1.right,"Right")

while is_game_on:
    screen.update()
    time.sleep(0.3)
    Snake1.move()


    if Snake1.head.distance(food) < 20:
        print("Food eaten")
        Score.increase_score()
        food.refresh()
        Snake1.extend()

    if Snake1.head.xcor() > 280 or Snake1.head.xcor() < -280 or Snake1.head.ycor() > 280 or Snake1.head.ycor() < -280:
        # Score.game_over()
        # is_game_on = False
        Score.game_over()
        Snake1.reset()
        food.refresh()

    for segments in Snake1.snake[1:]:
        if segments.distance(Snake1.head) < 10:
            # is_game_on = False
            # Score.game_over()
            Score.game_over()
            Snake1.reset()
            food.refresh()

screen.exitonclick()
# </editor-fold>






