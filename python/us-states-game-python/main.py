import turtle
import pandas
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {key: (value * 9/2) + 32 for (key, value) in weather_c.items()}

print(weather_f)
screen = turtle.Screen()
screen.title('US-States-Game')
IMAGE = 'blank_states_img.gif'
screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pandas.read_csv('50_states.csv')
states = data['state'].to_list()

is_game_on = True
guessed = 0

while is_game_on:
    text = screen.textinput(f'{guessed}/{len(states) + guessed} Guess the state', 'What\'s another state\'s name?').capitalize()
    if text in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data['state'] == text]
        t.goto(int(state_data['x']), int(state_data['y']))
        t.write(text)
        states.remove(text)
        guessed += 1
    else:
        is_game_on = False
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(0, 0)
        t.write('Game Over', align='center', font=('Arial', 24, 'normal'))



screen.exitonclick()