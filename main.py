#!/usr/bin/env python3

import time
import turtle as t

window = t.Screen()
window.bgcolor("black")
window.setup(width=1000, height=700)
window.tracer(0)

def setup():
    t.penup()
    t.pencolor("white")
    t.fillcolor("white")
    t.goto(-500, 350)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.forward(1000)
        t.right(90)
        t.forward(700)
        t.right(90)
    t.end_fill()

# Left Paddle setup
left_paddle = t.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("black")
left_paddle.shapesize(stretch_wid=10, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-450, 0)

# Right Paddle setup
right_paddle = t.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("black")
right_paddle.shapesize(stretch_wid=10, stretch_len=1)
right_paddle.penup()
right_paddle.goto(450, 0)

ball = t.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 4.5
ball.dy = -4.5



current_time = time.time()
time_delta = 0


pressed_keys = set()

def on_key_press(key):
    pressed_keys.add(key)

def on_key_release(key):
    pressed_keys.remove(key)

def move_paddles():
    if 'w' in pressed_keys:
        move_left_paddle_up()
    if 's' in pressed_keys:
        move_left_paddle_down()
    if 'Up' in pressed_keys:
        move_right_paddle_up()
    if 'Down' in pressed_keys:
        move_right_paddle_down()

def move_left_paddle_up():
    y = left_paddle.ycor()
    y += 10
    if y+100 < 350:
        left_paddle.sety(y)

def move_left_paddle_down():
    y = left_paddle.ycor()
    y -= 10
    if y-100 > -350:
        left_paddle.sety(y)

def move_right_paddle_up():
    y = right_paddle.ycor()
    y += 10
    if y+100 < 350:
        right_paddle.sety(y)

def move_right_paddle_down():
    y = right_paddle.ycor()
    y -= 10
    if y-100 > -350:
        right_paddle.sety(y)

window.listen()
window.onkeypress(lambda: on_key_press('w'), 'w')
window.onkeypress(lambda: on_key_press('s'), 's')
window.onkeypress(lambda: on_key_press('Up'), 'Up')
window.onkeypress(lambda: on_key_press('Down'), 'Down')
window.onkeyrelease(lambda: on_key_release('w'), 'w')
window.onkeyrelease(lambda: on_key_release('s'), 's')
window.onkeyrelease(lambda: on_key_release('Up'), 'Up')
window.onkeyrelease(lambda: on_key_release('Down'), 'Down')



gameover = False
  
winner_count_left = 0 
winner_count_right = 0

setup()
def main():
 global winner_count_right
 global winner_count_left

 count_display_left = t.Turtle()
 count_display_right = t.Turtle()
 count_display_right.hideturtle()
 count_display_left.hideturtle()
 count_display_left.speed(0)
 count_display_right.speed(0)
 count_display_left.penup()
 count_display_right.penup()
 count_display_left.setpos(-450,300)
 count_display_right.setpos(450,300)
 count_display_left.write('0',font=('impact',30,'normal'))
 count_display_right.write('0',font=('impact',30,'normal'))

 gameover = False
 global current_time
 while gameover == False:
    move_paddles()
    window.update()
    x = ball.xcor()
    if x > 460 or x < -460:
      gameover = True
      x= (ball.xcor())
      print(x)
      if x < 0:
          winner_count_right+=1
      else:
          winner_count_left+=1
      print(winner_count_left)
      print(winner_count_right)

      count_display_right.clear()
      count_display_left.clear()
      count_display_left.write(winner_count_left,font=('impact',30,'normal'))
      count_display_right.write(winner_count_right,font=('impact',30,'normal'))

      
      ball.goto(0,0)
      gameover=False
      


    # Calculate the time delta
    new_time = time.time()
    time_delta = new_time - current_time
    current_time = new_time
    
    # Update the ball position based on time delta
    ball.setx(ball.xcor() + (ball.dx * time_delta * 60))
    ball.sety(ball.ycor() + (ball.dy * time_delta * 60))

    move_paddles()
    window.update()
    
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.xcor() > 490 or ball.xcor() < -490:
        ball.dx *= -1

    if ball.ycor() > 340 or ball.ycor() < -340:
        ball.dy *= -1
    
    if (ball.dx > 0) and (ball.xcor() > 440 and ball.xcor() < 450) and (ball.ycor() > right_paddle.ycor() - 100 and ball.ycor() < right_paddle.ycor() + 100):
        ball.dx *= -1
    
    if (ball.dx < 0) and (ball.xcor() < -440 and ball.xcor() > -450) and (ball.ycor() > left_paddle.ycor() - 100 and ball.ycor() < left_paddle.ycor() + 100):
        ball.dx *= -1


setup()
main()

t.done()
