from turtle import *

i = 1
line = 0
while True:
    line += 1
    forward(i)
    left(90)
    if i % 2 == 0:
        i += 1
    else:
        i += 2

    if line == 100:
        break
