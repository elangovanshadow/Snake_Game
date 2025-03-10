from turtle import Turtle
FONT = ('Arial',20,'normal')
ALGNIMENT = 'center'
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.sety(260)
        self.color('yellow')
        with open('data.txt', mode='r') as file:
            self.highscore = int(file.read())
        self.show_score()


    def show_score(self):
        self.clear()
        self.write(f"Score : {self.score}, High Score : {self.highscore}", move=False, align= ALGNIMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        self.show_score()
    def game_over(self):
        # self.goto(0,0)
        self.highscore = max(self.highscore,self.score)
        with open('data.txt', mode='w') as file:
            file.write(str(self.highscore))
        self.score = 0
        self.show_score()
        # self.write("Game Over", move=False, align=ALGNIMENT, font=FONT)