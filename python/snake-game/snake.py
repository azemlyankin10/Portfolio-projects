from turtle import Turtle

class Snake:

    def __init__(self):
        self.direction = 'right'
        self.segments = []
        self.initiate_snake()
        self.head = self.segments[0]

    def initiate_snake(self):
        for i in range(3):
            turtle = Turtle('square')
            turtle.color('white')
            turtle.penup()
            turtle.goto(i * 20, 0)
            self.segments.append(turtle)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

        self.head.forward(20)


    def up(self):
        if self.direction != 'down':
            self.direction = 'up'
            self.head.setheading(90)
    def down(self):
        if self.direction != 'up':
            self.direction = 'down'
            self.head.setheading(270)
    def left(self):
        if self.direction != 'right':
            self.direction = 'left'
            self.head.setheading(180)
    def right(self):
        if self.direction != 'left':
            self.direction = 'right'
            self.head.setheading(0)

    def add_segment(self):
        turtle = Turtle('square')
        turtle.color('white')
        turtle.penup()
        turtle.goto(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(turtle)

    def is_collision(self):
        # if not self.started:
        #     return False
        if self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() < -290:
            return True
        for segment in self.segments:
            if segment == self.head:
                return False
            if self.head.distance(segment) < 10:
                return True
        return False