import turtle
import pandas
screen = turtle.Screen()
screen.title("US state game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


states = pandas.read_csv("50_states.csv")
st_list = states["state"].to_list()
# print(st_list)
guessed_states = []
game_on = True

while game_on:
    answer_state = screen.textinput(f"Guess the state {len(guessed_states)}/50", "Whats another state's name?").title()
    # print(states["state"])
    # if answer_state == "Exit" or "exit":
    #     break
    if answer_state == "Exit":
        missing_states = []
        for state in st_list:
            if state not in guessed_states:
                missing_states.append(state)
        with open("missed_state.csv",mode="w") as ms:
            for i in missing_states:
                ms.write(i + "\n")
        break
    if answer_state in guessed_states:
        pass
    elif answer_state in st_list:
        
        xy = states[states["state"] == answer_state]
        xx = xy['state']
        guessed_states.append(answer_state)
        # x = xx.x
        # y = xx.y
        print(xy.x)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(xy.x),int(xy.y))
        t.write(answer_state)
        print("True")

# states
with open("miss_states.csv", mode = "w") as c:
    c.write(states["state"].to_list() - guessed_states)

turtle.mainloop()

