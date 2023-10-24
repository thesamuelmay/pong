#!/usr/bin/env python3

import time
import turtle as t



# Initialize a game state variable

block_list = []
current_time = time.time()
winner_count_left = 0
winner_count_left = 0
home_initialised = False

window = t.Screen()
window.addshape('local.gif')
window.bgpic("bg.gif")
window.setup(width=1000, height=700)
window.tracer(0)

def set_game_state(state):
    global current_state
    current_state = state

def local_state(x,y): 
    global current_state
    current_state = 'local'
    # some motion 

# Function to handle home screen logic
def home_screen():
    global button_local,home_initialised,window
    
    #Init Local button
    if home_initialised == False:
      home_initialised = True
      print(home_initialised)
      button_local = t.Turtle()
      button_local.shape('local.gif')
      button_local.shapesize(stretch_wid=0.001, stretch_len=1000)
      
      button_local.penup()
      button_local.goto(0,60)
      button_local.onclick(local_state)
    window.update()


def hide_home():
  global button_local,window
  button_local.hideturtle()
  
    

# Function for LocalCoOp state
def local_coop():
    global current_game_state,block_list,current_time,winner_count_left,winner_count_right,window
    # Your existing game code goes here, integrated as part of local_coop
    hide_home()
    window.bgcolor("black")
    window.bgpic("nopic")

    #initilaise the Block class
    class Block:
        def __init__(self, x, y):
            self.block_turtle = t.Turtle()  
            self.block_turtle.shape("square")  
            self.block_turtle.color("green")  
            self.block_turtle.penup()  
            self.set_position(x, y)  
            
        def set_position(self, x, y):
            self.block_turtle.goto(x, y)  

        def hide(self):
            self.block_turtle.hideturtle() 


    def is_collision(block, ball):
        return abs(block.block_turtle.xcor() - ball.xcor()) < 10 and abs(block.block_turtle.ycor() - ball.ycor()) < 10

    def collision(block,ball):
        return abs(ball.distance(block.block_turtle)) <30





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
    left_paddle.shapesize(stretch_wid=7, stretch_len=1)
    left_paddle.penup()
    left_paddle.goto(-450, 0)

    # Right Paddle setup
    right_paddle = t.Turtle()
    right_paddle.speed(0)
    right_paddle.shape("square")
    right_paddle.color("black")
    right_paddle.shapesize(stretch_wid=7, stretch_len=1)
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
        if y+70 < 350:
            left_paddle.sety(y)

    def move_left_paddle_down():
        y = left_paddle.ycor()
        y -= 10
        if y-70 > -350:
            left_paddle.sety(y)

    def move_right_paddle_up():
        y = right_paddle.ycor()
        y += 10
        if y+70 < 350:
            right_paddle.sety(y)

    def move_right_paddle_down():
        y = right_paddle.ycor()
        y -= 10
        if y-70 > -350:
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
    block_list = []
    def blocks():
     global block_list

     # Constants
     block_width = 10
     block_height = 10
     gap = 20
     number_of_rows = 24
     number_of_columns = 10

     # Calculate total dimensions
     total_width = (block_width * number_of_columns) + (gap * (number_of_columns - 1))
     total_height = (block_height * number_of_rows) + (gap * (number_of_rows - 1))

     # Calculate starting points
     starting_x = -total_width / 2
     starting_y = total_height / 2

     for row in range(number_of_rows):
         for col in range(number_of_columns):
             x = starting_x + (block_width + gap) * col
             y = starting_y - (block_height + gap) * row
             block = Block(x, y)  # Instantiate a Block object
             block.set_position(x, y)
             block_list.append(block)




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
     global block_list
     while gameover == False:
        dist = ball.distance(left_paddle)
        if dist < 20:
         print("distance"+ str(dist))
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
        for block in block_list:
         
         if block.block_turtle.xcor() > 30 and block.block_turtle.xcor() <-30:
            block.hide()
            block_list.remove(block)
         if collision(block, ball):  # Assuming you have a function to check collision
            block.hide()
            block_list.remove(block)

        # Determine the side where the collision happened (this is a simplified example)
            dx = abs(block.block_turtle.xcor() - ball.xcor())
            dy = abs(block.block_turtle.ycor() - ball.ycor())

        # Flip ball direction based on the collision side
            if dx > dy:
                ball.dx *= -1
            else:
                ball.dy *= -1



        if ball.xcor() > 490 or ball.xcor() < -490:
            ball.dx *= -1

        if ball.ycor() > 340 or ball.ycor() < -340:
            ball.dy *= -1
        
        if (ball.dx > 0) and (ball.xcor() > 420 and ball.xcor() < 450) and (ball.ycor() > right_paddle.ycor() - 70 and ball.ycor() < right_paddle.ycor() + 100):
            ball.dx *= -1
        
        if (ball.dx < 0) and (ball.xcor() < -420 and ball.xcor() > -450) and (ball.ycor() > left_paddle.ycor() - 70 and ball.ycor() < left_paddle.ycor() + 100):
            ball.dx *= -1
        

    blocks()
    setup()
    main()

    t.done()
    pass

    # ... (rest of your existing code)

    # At the end of the game, you can change the current_game_state to 'GameOver' or 'HomeScreen', like this:
    # current_game_state = "GameOver"
 # Function for OnlineCoOp state

def online_coop():
    # Logic for running the online co-op game
    pass

# Function for GameOver state (Optional)
def game_over():
    # Logic for displaying game over screen
    pass





# Initialize turtle window

# Start game at the home screen
set_game_state("home")

# Main game loop
while True:
    if current_state == "home":
        home_screen()
    elif current_state == "local":
        home_displayed = False  # Reset flag since we're no longer in home screen
        local_coop()
    elif current_state == "online":
        home_displayed = False  # Reset flag since we're no longer in home screen
        online_coop()
        
    time.sleep(0.1)  # Add a slight delay to avoid overwhelming the CPU





















