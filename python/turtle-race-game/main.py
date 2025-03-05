from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput('Make your bet', 'Which turtle will win the race? Enter a color: ')

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# tim = Turtle(shape='turtle')
# tim.penup()
# tim.goto(-230, -100)

turtles = []
for i in range(len(colors) - 1):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230, -100 + i * 40)
    turtles.append(new_turtle)

is_race = False
winner = ''
if user_bet:
    is_race = True

while is_race:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            is_race = False
        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

print(f"The winner is {winner}")
screen.exitonclick()