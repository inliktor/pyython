from turtle import *
from time import *
from random import *
# Создай объект "черепашка", установи форму, цвет, скорость
t1= Turtle()
t1.shape('turtle')
t1.color('red')
def rand_move():
    num=randint(1,3)
    if num==1:
        t1.forward(randint(1,11))
    elif num==2:
        t1.left(randint(1,10))
    else:
        t1.right(randint(1,11))
rand_move()