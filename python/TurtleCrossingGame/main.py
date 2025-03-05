from turtle import Screen
from dashboard import Dashboard
from car import Car
import time
from avatar import Avatar

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

dashboard = Dashboard()
avatar = Avatar()
cars = []
for _ in range(10):
    car = Car()
    cars.append(car)

screen.update()

screen.listen()
screen.onkey(avatar.move_up, "Up")
screen.onkey(avatar.move_down, "Down")
screen.onkey(avatar.move_left, "Left")
screen.onkey(avatar.move_right, "Right")

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    if avatar.ycor() > 280:
        avatar.goto(0, -280)
        dashboard.level_up()
        for car in cars:
            car.move_speed += 5
    for car in cars:
        car.move()
        if car.xcor() < -300:
            car.reset()
        if car.is_collision(avatar):
            is_game_on = False
            dashboard.clear()
            dashboard.goto(0, 0)
            dashboard.write("Game Over", align="center", font=("Courier", 24, "normal"))




screen.exitonclick()