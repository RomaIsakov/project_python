from turtle import *
t = Turtle()
class Button():

    x = 0
    y = 0
    width = 100
    height = 25
    
    fcol = "black" 
    def drow (self) :
        t.penup()
        t.color(self.fcol)
        t.goto(self.x, self.y)
        t.begin_fill()
        t.goto(self.x + self.width, self.y)
        t.goto(self.x + self.width, self.y + self.height)
        t.goto(self.x, self.y + self.height)
        t.end_fill()
b = Button()
b.fcol = "green"
b.x = 1
b.y = - 1
b.width = 10
b.height = 150
b.drow()

d = Button()
d.fcol = "black"
d.x = 1
d.y = 75
d.width = 150
d.height = 10
d.drow()

ñ = Button()
ñ.fcol = "black"
ñ.x = 1
d.y = 75
d.width = 150
d.height = 10
d.drow()














exitonclick()