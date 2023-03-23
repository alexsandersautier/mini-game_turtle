from turtle import Turtle

turtlee = Turtle()

turtlee.speed(2)

def front(turtle,amount):
    turtle.forward(amount)

def back(turtle,amount):
    turtle.backward(amount)

def turn_right(turtle,amount):
    turtle.right(amount)
    front(turtle,amount)

def turn_left(turtle,amount):
    turtle.left(amount)
    front(turtle,amount)

while True:
    action = input('Do you want to move front, back, turn right or turn left? ')
    try:    
        if action == 'front':
            amount_front = int(input('Amount for front? '))
            front(turtlee,amount_front)
        elif action == 'back':
            amount_back = int(input('Amount for back? '))
            back(turtlee,amount_back)
        elif action == 'turn right':
            amount_right = int(input('Amount for right? '))
            turn_right(turtlee, amount_right)
        elif action == 'turn left':
            amount_left = int(input('Amount for left? '))
            turn_left(turtlee, amount_left)
        else:
            print('Invalid option!!!!')
        
        continues = input('Do you would like continue (y/n)? ')

        if continues == 'y':
            continue       
        else:
            break    
    except:
        print('Verificy!')