import random
import time
import os
import turtle

t = turtle.Turtle()
t.hideturtle()
t.pensize(5)
t.penup()

def head():
        t.setpos(0,0)
        t.pendown()
        t.circle(50)
        t.penup()


def body():
    t.setpos(0,-150)
    t.pendown()
    t.circle(75)
    t.penup()


def legs():
    t.setpos(0,-350)
    t.pendown()
    t.circle(100)
    t.penup()


def vedro():
    t.penup()
    t.setpos(-38,100)
    t.pendown()
    t.color('red')
    t.goto(38,100)
    t.goto(19,195)
    t.goto(-19,195)
    t.goto(-38,100)
    t.penup()


def mokovi():
    t.penup()
    t.setpos(0,55)
    t.pendown()
    t.color('blue')
    t.goto(40,40)
    t.goto(0,35)
    t.goto(0,55)


def glaza():
    t.penup()
    t.setpos(-18,67)
    t.pendown()
    t.goto(-19,67)
    t.penup()
    t.setpos(18,67)
    t.pendown()
    t.goto(19,67)


def ruki():
    t.penup()
    t.setpos(-75,-75)
    t.pendown()
    t.goto(-150,125)
    t.penup()
    t.setpos(75,-75)
    t.pendown()
    t.goto(150,125)


def snowman():
        if count_wrong_letters == 0:
                legs()
        elif count_wrong_letters == 1:
                body()
        elif count_wrong_letters == 2:
                head()
        elif count_wrong_letters == 3:
                ruki()
        elif count_wrong_letters == 4:
                glaza()
        elif count_wrong_letters == 5:
                mokovi()

words = [
	'привет',
	'пока',
	'лондон',
	'париж',
	'стриж',
]
word = random.choice(words)
star = '*'*len(word)

user_alpha = ""
count_wrong_letters = 0
count_stars = len(word)
max_wrong_letters = len(word)
max_good_letters = len(word)

loss = False

user_input = '''Введи букву:
>>>'''

print('Я загадал слово, попробуй отгадай!')


time.sleep(5)


while loss == False:
        os.system('cls||clear')
        
        print(star)
        print("колличество ошибок:" ,count_wrong_letters)
        
        user_alpha = input(user_input)
        
        if user_alpha in word:
                for i in range(len(word)):
                        if user_alpha == word[i]:
                                star = star[:i] + word[i] + star[i+1:]
                                count_stars = count_stars - 1
                                if count_stars == 0:
                                        os.system('cls||clear')
                                        print(word)
                                        print("Ты выйграл!")
                                        
                                        loss = True
        else:
                snowman()
                count_wrong_letters += 1
                
                if count_wrong_letters == 7:

                        vedro()
                        
                        os.system('cls||clear')
                        
                        print(word)
                        print("Ты проиграл!")
                        
                        loss = True