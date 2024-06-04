import pandas
import turtle

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
states_guessed = []
while len(states_guessed) < 50:
    answer = screen.textinput(title=f"{len(states_guessed)}/50 States Correct",
                              prompt="What's another state's name?").title()
    if answer == "Exit":
        missing_states = [item for item in all_states if item not in states_guessed]
        # missing_states = []
        # for i in all_states:
        #     if i not in states_guessed:
        #         missing_states.append(i)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in all_states and answer not in states_guessed:
        states_guessed.append(answer)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)

    else:
        pass

screen.exitonclick()
