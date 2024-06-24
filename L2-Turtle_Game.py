from turtle import Turtle, Screen
import random

screen = Screen()
angles = [-100, 100, -60, 60, -20, 20]
colors = ["green", "red", "blue", "pink", "black", "purple"]

screen.setup(500, 400)
user_input = screen.textinput(title="Turtle Bet", prompt="Choose the color:")
all_turtles = []


race_on = False
for t in range(0, 6):
    t1 = Turtle(shape="turtle")
    t1.color(colors[t])
    t1.penup()
    t1.goto(x=-230, y=angles[t])
    all_turtles.append(t1)
if user_input:
    race_on = True

while race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_turtle = turtle.pencolor()

            if winning_turtle == user_input:
                print(f"You won the winning turtle is {winning_turtle}")
            else:
                print(f"You lost the winning turtle is {winning_turtle}")

        turtle_dist = random.randint(1, 10)
        turtle.forward(turtle_dist)


screen.exitonclick()



