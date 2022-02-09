import turtle
bob = turtle.Turtle()

length = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

bob.color ("Yellow")
bob.width(5)

for length in length:
    bob.forward(length)
    bob.right(90)
