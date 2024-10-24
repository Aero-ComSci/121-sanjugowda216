# a121_catch_a_turtle.py
#-----import statements-----
import turtle
import random as rand
#-----game configuration----
color = "pink"
shape = 'triangle'
size = 3
score = 0
#-----initialize turtle-----
t = turtle.Turtle()
t.shape(shape)
t.shapesize(size)
t.fillcolor(color)
#-----game functions--------
def clicked(x,y):
    print("CLICKED AT:", x,y)
    change_positioncolor()
def change_positioncolor():
    t.penup()
    new_x = rand.randint(-200,200)
    new_y = rand.randint(-150,150)
    colors = ["gray","lightblue","purple"]
    new_color = rand.choice(colors)
    t.goto(new_x,new_y)
    wn.bgcolor(new_color)
#-----events----------------
wn = turtle.Screen()
wn.title("Catch a Turtle!!")
t.onclick(clicked)

wn.mainloop()
