# from turtle import Turtle, Screen, colormode
# import random
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.pensize(15)
# colormode(255)
# for _ in range(4): # square
#     timmy.forward(100)
#     timmy.right(90)

# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
# for shape_side_n in range(3, 11):
#     timmy.color("red")
#     draw_shape(shape_side_n)
#     timmy.color("blue")

# directions = ['left', 'right', 'up', 'down']
# # colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
#
# def move(direction):
#     if direction == 'left':
#         timmy.left(90)
#         timmy.forward(100)
#     elif direction == 'right':
#         timmy.right(90)
#         timmy.forward(100)
#     elif direction == 'up':
#         timmy.setheading(90)
#         timmy.forward(100)
#     elif direction == 'down':
#         timmy.setheading(270)
#         timmy.forward(100)
#
#
# is_on = True
#
# while is_on:
#     timmy.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
#     move(random.choice(directions))


# timmy.speed(10)
# for angle in range(0, 360, 5):
#     timmy.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
#     timmy.setheading(angle)
#     timmy.circle(50)

# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))



#
# screen = Screen()
# screen.exitonclick()



from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_left():
    tim.left(10)
    tim.heading()

def move_right():
    tim.right(10)
    tim.heading()

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, 'c')
screen.exitonclick()









