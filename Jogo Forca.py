# Yves Yuzo Sakamoto
# Jogo da Forca

import turtle
window = turtle.Screen()
window.bgcolor("white")
window.title("Forca")
turtle2 = turtle.Turtle()
turtle2.hideturtle()
turtle3 = turtle.Turtle()
turtle3.pu ()
turtle3.setpos(100, -200)
turtle4 = turtle.Turtle()
turtle4.pu ()
turtle4.setpos(100, -230)
turtle5 = turtle.Turtle
turtle5.setpos (100, -190)

reference = 1

def forca ():
    turtle.pu()
    turtle.setpos(-200,-100)
    turtle.pd()
    turtle.left(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(50)
    
def turn(x, y):
    if x>0:
        turtle.left(180)
        turtle.forward(100)
        
def sim(x, y):
    if 90 > x > 110 and -190 > y > -210:
        turtle3.hideturtle()
    
        
while reference == 1:
    
   forca ()
   turtle2.pu()
   turtle2.setpos(-250,-200)
   turtle2.pd()
   turtle2.write("Você quer começar a jogar Forca?", move=False, align="left", font=("Arial", 16, "normal"))
   turtle3.write("Sim", move=False, align="left", font=("Arial", 16, "normal"))
   turtle4.write("Não", move=False, align="left", font=("Arial", 16, "normal"))
#variavel_texto = window.textinput("Janela de Resposta", " ")
   turtle.onscreenclick(turn)  # Now clicking into the turtle will turn it.
   turtle.onclick(None)  # event-binding will be removed
   turtle.mainloop()
   
   
   
  
       
   
   
   
   