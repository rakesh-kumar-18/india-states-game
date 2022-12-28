import pandas
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("India States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("28_states.csv")
state_names = data.state.to_list()
guessed_states = []

t = turtle.Turtle()
t.hideturtle()
t.penup()

while len(guessed_states) < 28:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/28 States Correct",
                                    prompt="what's another state's name?").title()

    if answer_state == "Exit":
        # missing_states = [[state for state in state_names if state not in guessed_states]]
        missing_states = []
        for state in state_names:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        for state in missing_states:
            state_left = data[data.state == state]
            t.goto(int(state_left.x), int(state_left.y))
            t.pencolor("blue")
            t.write(state, align="left", font=("Arial", 8, 'bold'))
        break
    if answer_state in state_names and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()
