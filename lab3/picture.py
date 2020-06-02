from graph import *

windowSize(500, 400)
penSize(0)
brushColor(64, 213, 233)
rectangle(0, 0, 1000, 180)
brushColor(81, 68, 233)
rectangle(0, 180, 1000, 280)
brushColor(244, 241, 156)
rectangle(0, 280, 1000, 400)
penSize(1)
penColor(200, 200, 200)
brushColor("white")
x = 70
y = 40
for i in range(1,9):
    if i % 2 == 1:
        circle(x, y, 15)
        x -= 13
        y += 12
    else:
        circle(x, y, 15)
        x += 32
        y -= 12
penSize(0)
brushColor("yellow")
circle(450, 50, 40)
penSize(8)
penColor(153, 51, 0)
line(80, 370, 80, 230)
run()