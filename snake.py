from turtle import Turtle,Screen

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0),(-60,0),(-80,0),(-100,0),(-120,0),(-140,0),(-160,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.snake = []
        self.createSnake()
        self.head = self.snake[0]
        self.head.shape('triangle')
    def createSnake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)


    def add_segment(self,pos):
        tim = Turtle()
        tim.penup()
        tim.shape("square")
        tim.color("white")
        tim.goto(pos)
        self.snake.append(tim)

    def extend(self):
        self.add_segment(self.snake[-1].position())


    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            x_val = self.snake[i - 1].xcor()
            y_val = self.snake[i - 1].ycor()
            self.snake[i].goto(x_val, y_val)
        self.head.forward(MOVE_DISTANCE)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset(self):
        for segments in self.snake:
            segments.goto(1000,1000)
        self.snake.clear()
        self.__init__()



