# Yves Yuzo Sakamoto
# Jogo da Forca
import random 
import turtle
import time

palavra_da_rodada = []
raw = open("entrada.txt", encoding="utf-8")
palavras = raw.readlines()
erros = 0
letras_chutadas = []
posições_das_letras = []

lista = []
for pa in palavras:
    x = pa.strip().lower()
    if x != "":
        lista.append(x)
         
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

turtle6 = turtle.Turtle()
turtle6.pu ()
turtle6.setpos(-200, -100)

reference = 1
chute = 0

##################################
  
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
                                                      
def traços (x):
    for i in range(0, x):
        turtle6.forward(5)
        turtle6.pd()
        turtle6.forward(15)
        turtle6.pu()

def ocorrencias (chute, segredo):
    pdl = list()
    for l in range(len(segredo)):
        if chute == segredo[l]:
            pdl.append(l)
        #segredo = segredo.replace("1", chute, 1)
        
    return pdl
    
def       
    
    
    
        
    
    
forca()     


while len(lista) != 0:
    segredo = random.choice(palavras)                
    traços (len(segredo))
    segredo_split = segredo.split
    while len(segredo) != 0:
        chute = window.textinput("Digite o seu chute", " ")
        if chute not in letras_chutadas:
            if chute in segredo:
                posições_das_letras = ocorrencias (chute, segredo)
                
            
            
            
        
    
    
        
        
        
    
    
    
        
            

  
              
turtle.done()