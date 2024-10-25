# a121_catch_a_turtle.py
#-----import statements-----
import turtle
import random as rand
#-----game configuration----
color = "pink"
shape = 'triangle'
stampcolor = ["green","black","yellow","red","lightpink","pink"]
size = 3
score = 0
#-----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----initialize turtle-----
t = turtle.Turtle()
score_display = turtle.Turtle()
counter =  turtle.Turtle()
counter.penup()
counter.goto(250,300)
score_display.penup()
score_display.goto(-300, 300)  
score_display.hideturtle()
t.shape(shape)
t.shapesize(size)
t.fillcolor(color)


#-----game functions--------
def clicked(x,y):
    global timer_up
    if timer_up==False:
        change_positioncolor()
        updatescore()
        stampcolors()
    else:
        t.hideturtle()
def change_positioncolor():
    t.penup()
    new_x = rand.randint(-300,300)
    new_y = rand.randint(-300,300)
    colors = ["gray","lightblue","purple"]
    new_color = rand.choice(colors)
    t.goto(new_x,new_y)
    wn.bgcolor(new_color)
    
def updatescore():
    global score
    font_setup = ("Arial", 20, "normal")
    score+=1
    score_display.clear() 
    score_display.write(score, align="center", font=font_setup)
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
def stampcolors():
    global stampcolor
    rightnow = rand.choice(stampcolor)
    t.fillcolor(rightnow)
    t.stamp()
    t.fillcolor("lightpink")

#-----events----------------
wn = turtle.Screen()
wn.ontimer(countdown, counter_interval) 

wn.title("Catch a Turtle!!")
t.onclick(clicked)
wn.bgcolor("pink")
wn.mainloop()
