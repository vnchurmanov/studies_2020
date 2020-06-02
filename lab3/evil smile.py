from graph import *

penColor("black")
penSize(1)
brushColor("yellow")
circle(250, 250, 150)
x = 190
y = 200
r = 30
for i in range(2):
    brushColor("red")
    circle(x, y, r)
    brushColor("black")
    circle(x, y, r / 2)
    x += 130
    r -= 5
penSize(10)
line(233, 190, 140, 115)
line(285, 190, 383, 115)
penSize(20)
line(190, 330, 320, 330)

run()
