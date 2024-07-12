from turtle import Turtle, Screen
from random import randint
from colorgram import extract

# Extract colors from an image.
colors = extract('2024-06-28 110726.png', 12)
color_list = []

# 把讀取到的顏色打包成一個List
for color_object in colors:
    color_list.append(color_object.rgb)

# 基本設定
jimmi = Turtle()
screen = Screen()
# screen.colormode(255)
jimmi.speed(1)
jimmi.pencolor("")

# 變數
x_axis = 0
y_axis = 0
def ran_color():
    r = color_list[randint(0, len(color_list) - 1)].r
    g = color_list[randint(0, len(color_list) - 1)].g
    b = color_list[randint(0, len(color_list) - 1)].b
    random_color_tuple = (r , g, b)
    return random_color_tuple

for i in range(20):
    for i in range(4):
        jimmi.dot(20,ran_color())
        jimmi.forward(30)

    y_axis += 30
    jimmi.goto(x_axis, y_axis)

screen.exitonclick()
