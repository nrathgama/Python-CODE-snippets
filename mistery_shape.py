# Mystery Shape

import turtle 
misty = turtle.Turtle()
misty.color("red")
misty.width(5)

angles=[-90,0,0,-90,135,0,0,0,90,0,0,0,135,-90,0,0,90,0,0,0]

for angle in angles:
    misty.right(angle)
    misty.forward(25)

#if you run the code you will see a tiny house!! :)