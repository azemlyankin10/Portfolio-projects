from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Python Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

screen.update()

is_running = True

while is_running:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_segment()
        scoreboard.increase_score()
    if snake.is_collision():
        is_running = False
        scoreboard.game_over()




screen.exitonclick()