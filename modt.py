import turtle 

t = turtle.Turtle()
t.width(5)
t.color ("red")
t.penup()
t.back(100)
t.pendown

for step in range(21):
    t.forward(10)

if step%3 == 0:
    t.left(90)
else: 
    t.right(90)

t.hideturtle()