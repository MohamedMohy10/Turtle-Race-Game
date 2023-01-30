from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("lightgreen")
user_guess = screen.textinput(title="Make prediction", prompt="Which turtle will win the race ? Enter a color :").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [75, 50, 25, 0, -25, -50]
all_turtles = []

for turtl in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtl])
    new_turtle.penup()
    new_turtle.setpos(x=-230, y=y_positions[turtl])
    all_turtles.append(new_turtle)

if user_guess:
    race_on = True
    while race_on:
        for turtle in all_turtles:
            turtle.forward(randint(0, 10))
            if turtle.xcor() >= 230:
                winner = turtle.fillcolor()
                race_on = False

if user_guess == winner:
    print(f"You Won , the winner is {winner.upper()} turtle")
else:
    print(f"You lose , the winner is {winner.upper()} turtle")



screen.exitonclick()