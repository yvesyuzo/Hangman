# Yves Yuzo Sakamoto
# Jogo da Forca

import turtle


'''entrada = open("entrada.txt", encoding="utf-8")
conteudo = entrada.readlines()'''

results = []
with open('entrada.txt') as inputfile:
    for line in inputfile:
        results.append(line.strip())


window = turtle.Screen()
window.bgcolor("white")
window.title("Forca")
turtle2 = turtle.Turtle()
turtle2.hideturtle()

turtle3 = turtle.Turtle()
turtle3.pu ()
turtle3.setpos(100, -200)
turtle3.shape("turtle")

turtle4 = turtle.Turtle()
turtle4.pu ()
turtle4.setpos(100, -230)

turtle5 = turtle.Turtle

reference = 1
chute = 0
variavel_texto = "n"

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
    
def cabeça ():
    pass
    

def sim(x, y):
    if 100 < x < 135 and -175 > y > -205:
          global chute
          chute += 1
          turtle3.forward(35)
          turtle3.left(90)
          turtle3.forward(10)
          turtle3.pd()
          turtle3.circle(20)
          turtle2.clear()
          turtle3.clear()
          turtle4.clear()
          if chute >= 1:
              print(results[2])
              
              variavel_texto = window.textinput("digite o seu chute", " ") 


              
                                      
while reference == 1:
    
   forca ()
   turtle2.pu()
   turtle2.setpos(-250,-200)
   turtle2.pd()
   turtle2.write("Você quer começar a jogar Forca?", move=False, align="left", font=("Arial", 16, "normal"))
   turtle3.write("Sim", move=False, align="left", font=("Arial", 16, "normal"))
   turtle4.write("Não", move=False, align="left", font=("Arial", 16, "normal"))
   turtle.onscreenclick(sim)  # Now clicking into the turtle will turn it.
   turtle.onclick(None)  # event-binding will be removed
   turtle.mainloop()
   
   
   
   
   
   '''
def linhas ()
   x =0
   for x <= len[palavra]:
       turtle.forward(20)
       turtle.pu()
       turtle.forward(10)
       turtle.pd()
       x += 1
        '''
          
 