from turtle import Turtle

class Dashboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-270, 270)
        self.level = 1
        self.update()

    def level_up(self):
        self.clear()
        self.level += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Courier", 24, "normal"))