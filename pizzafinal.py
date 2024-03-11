import random

from turtle import *

speed(0)

screen=Screen()
screen.setup(width=500, height=500)


def pizza_shape(pshape):
    if pshape == "circle":
        penup()
        right(90)
        forward(200)   
        right(270)  
        pendown() 
        begin_fill()
        fillcolor("tan")
        circle(200)
        penup() 
        home()
        end_fill()

def inner_circle(fill_color):
    penup()
    right(90)
    forward(170)
    right(270)
    pendown() 
    begin_fill()
    fillcolor(fill_color)
    circle(170) 
    penup()
    home()
    end_fill()

def pizza_sauce(psauce):
    if psauce == "marinara":
        inner_circle("red")
    elif psauce == "white sauce":
        inner_circle("white")
    else: 
        psauce == "bbq sauce"
        inner_circle("brown")
    

def pizza_cheese(pcheese):
    if pcheese == "mozzerella":
       inner_circle("yellow")
    else: 
        pcheese == "cheddar"
        inner_circle("orange")

def pizza_toppings(ptoppings):
   for item in ptoppings:
    if item == "pepperoni":
        dpepperoni()
    elif item == "sausage":
        dsausage()
    elif item == "green pepper":
        dgreenpepper()
    elif item == "pineapple":
        dpineapple()
    elif item == "ham":
        dham()
    item = item
    
    


def dpepperoni():
   for x in range(5):
            penup()
            goto(random_coordinates())
            begin_fill()
            fillcolor("red")
            for i in range(3):
                circle(40)
            end_fill()
   

def dsausage():
    for x in range(5):
            penup()
            goto(random_coordinates())
            begin_fill()
            fillcolor("brown")
            for i in range(3):
                circle(30)
            end_fill()

def dgreenpepper():
    for x in range(5):
        penup()
        goto(random_coordinates())
        begin_fill()
        fillcolor("green")
        for i in range(3):
            forward(30)
            right(90)
            forward(15)
            right(90)
            forward(30)
            right(90)
            forward(15)
            right(90)
        end_fill()


def dpineapple():
    for x in range(5):
        penup()
        goto(random_coordinates())
        begin_fill()
        fillcolor("yellow") 
        for i in range(3):
                forward(30)
                left(120)
        end_fill()

def dham():
    for x in range(5):
        penup()
        goto(random_coordinates())
        begin_fill()
        fillcolor("pink") 
        for i in range(3):
                forward(30)
                left(120)
        end_fill()

# Function to generate random x, y coordinates
def random_coordinates():
    x = random.randint(-110, 110)  # Adjust the range based on your needs
    y = random.randint(-110, 110)
    return x, y



def pizza_list(pshape, psauce, pcheese, ptoppings):
    pizza_shape(pshape)
    pizza_sauce(psauce)
    pizza_cheese(pcheese)
    pizza_toppings(ptoppings)
    
   

shape = {
    'circle': "cicrle"
}

sauce = {
    'marinara': "red",
    'white sauce': "white",
    'bbq sauce': 'brown'
}

cheese = {
    'mozzerella': "yellow",
    'cheddar': "orange"
}

toppings = {
    'pepperoni': "pepperoni", 
    'sausage': "sausage", 
    'green pepper': "green pepper", 
    'pineapple': "pineapple", 
    'ham': "ham"
}

for key in sauce.keys():
    psauce = random.choice(list(sauce))

for key in shape.keys():
    pshape = random.choice(list(shape)) 

for key in cheese.keys():
    pcheese = random.choice(list(cheese))

for key in toppings.keys():
    toppingslist = (list(toppings))

toppingsnumber = random.randrange(1,5)

ptoppings = (random.sample(toppingslist,toppingsnumber))

pizza_list(pshape, psauce, pcheese, ptoppings)


hideturtle()

done()