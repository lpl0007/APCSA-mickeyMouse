# L. Louque
# 1/17/2023
# mickeyMouse
# This program will draw an emoji

import turtle

t = turtle.Turtle()

def drawEars():
  #Left
  t.up()
  t.begin_fill()
  t.setpos(xValue-80, yValue+140)
  t.down()
  t.color(bodyColor)
  t.circle(55)
  t.end_fill()
  #Right
  t.up()
  t.begin_fill()
  t.setpos(xValue+80, yValue+140)
  t.down()
  t.color(bodyColor)
  t.circle(55)
  t.end_fill()
def drawEyes():
  #Whites
    #Left
  t.seth(0)
  t.up()
  t.begin_fill()
  t.setpos(xValue-20, yValue+100)
  t.down()
  t.color("white")
  t.circle(20)
  t.end_fill()
    #Right
  t.up()
  t.begin_fill()
  t.setpos(xValue+25, yValue+100)
  t.down()
  t.color("white")
  t.circle(20)
  t.end_fill()
  #Pupils
    #Left
  t.seth(0)
  t.up()
  t.begin_fill()
  t.setpos(xValue-20, yValue+110)
  t.down()
  t.color("black")
  t.circle(10)
  t.end_fill()
    #Right
  t.up()
  t.begin_fill()
  t.setpos(xValue+25, yValue+110)
  t.down()
  t.color("black")
  t.circle(10)
  t.end_fill()
def drawFace():
  t.up()
  t.setpos(xValue-77,yValue+35)
  t.seth(120)
  t.color(faceColor)
  t.down()
  t.begin_fill()
  t.circle(-25,140)
  t.seth(90)
  t.forward(60)
  t.circle(-25,160)
  t.seth(75)
  t.circle(-25,160)
  t.seth(-90)
  t.forward(60)
  t.seth(20)
  t.circle(-25,140)
  t.seth(-127)
  t.circle(-100,90)
  t.end_fill()
def drawHead():
  t.up()
  t.begin_fill()
  t.setpos(xValue, yValue)
  t.down()
  t.color(bodyColor)
  t.circle(100)
  t.end_fill()
def drawMouth():
    #Mouth
  t.up()
  t.color("maroon")
  t.setpos(xValue+50,yValue+60)
  t.down()
  t.begin_fill()
  t.setpos(xValue-50,yValue+60)
  t.seth(270)
  t.circle(50,180)
  t.end_fill()
    #Tongue
  t.up()
  t.color("brown1")
  t.setpos(xValue+25,yValue+16)
  t.down()
  t.begin_fill()
  t.seth(90)
  t.circle(15,180)
  t.end_fill()
  t.up()
  t.setpos(xValue+5,yValue+16)
  t.down()
  t.begin_fill()
  t.seth(90)
  t.circle(15,180)
  t.end_fill()
  t.up()
  t.down()
  t.begin_fill()
  t.seth(330)
  t.circle(50,60)
  t.end_fill()
def drawNose():
  t.up()
  t.begin_fill()
  t.setpos(xValue-10, yValue+70)
  t.seth(-45)
  t.down()
  t.color(bodyColor)
  for x in range(0,2):
    t.circle(15,90)
    t.circle(5,90)
  t.end_fill()
t.ht()

xValue = 0
yValue = 0

bodyColor = "gray10"
faceColor = "gray85"

drawEars()
drawHead()
drawFace()
drawEyes()
drawMouth()
drawNose()