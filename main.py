from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Has tu apuesta", prompt="Ingresa el color de tu tortuga: ")
colors = ["orange", "green", "purple", "red", "yellow", "blue"]
all_turtles = []

y_coord = -200
for index in range(0, 6):
    y_coord += 60
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coord)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"¡Ganaste! ¡La tortuga {winning_color} es la ganadora!")
            else:
                print(f"¡Perdiste! ¡La tortuga {winning_color} es la ganadora!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
    
screen.exitonclick()