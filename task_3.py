from turtle import *


dots = []


for x in open("dots.txt", encoding="utf-8"):
    data = x.strip().split()
    x, y = int(data[0]), int(data[1])
    dots.append((x, y))



OFFSET_X = -500
OFFSET_Y = 300


pu()
s_x, s_y = dots[0]
goto(s_x + OFFSET_X, - s_y + OFFSET_Y)
pd()

for x, y in dots:
    goto(x + OFFSET_X, - y + OFFSET_Y)

exitonclick()