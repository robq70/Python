import turtle

# Creating turtle screen - ship
t = turtle.Turtle()
t.pensize(10)
t.color("red")
t.goto(0, 100)
t.goto(0, 0)

t.color("green")
t.goto(100, 0)
t.goto(0, 0)

t.color("blue")
t.goto(0, -100)
t.goto(0, 0)

t.color("yellow")
t.goto(-100, 0)
t.goto(0, 0)


turtle.mainloop()
