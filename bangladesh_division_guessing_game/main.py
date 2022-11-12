import turtle
import pandas

screen = turtle.Screen()
screen.title("Bangladesh Division Finding Game")

image = "blank_division_img.gif"
turtle.addshape(image)

turtle.shape(image)
data = pandas.read_csv("all_division_name.csv")

all_division = data.division.tolist()
guessed_division = []

while len(guessed_division) < 8:
    answer_division = screen.textinput(title=f"{len(guessed_division)}/8 Division Correct",
                                    prompt="What's another division's name?").title()
    if answer_division == "Exit":
        missing_division = []
        for division in all_division:
            if division not in guessed_division:
                missing_division.append(division)
        new_data = pandas.DataFrame(missing_division)
        new_data.to_csv("division_to_learn.csv")
        break
    if answer_division in all_division:
        guessed_division.append(answer_division)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        division_data = data[data.division == answer_division]
        t.goto(int(division_data.x), int(division_data.y))
        # t.write(state_data.state.item())
        t.write(answer_division)

screen.exitonclick()