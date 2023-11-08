#!/usr/bin/env python3

import time
import turtle as t
import random


block_list = []
current_time = time.time()
winner_count_left = 0
winner_count_left = 0
home_initialised = False
game_over_initialised = False
launch_player = 'right'
ball_moving = False
last_hit_player = None
block_break_count_left = 0
block_break_count_right = 0
end_match = False
home_button_exists = False
winner_count_left = 0
winner_count_right = 0
block_grid = [[0 for _ in range(5)] for _ in range(24)]
starting_x = None
starting_y = None

total_points_right = 0
total_points_left = 0

debug_mode = False




block_width = 10
block_height = 10
gap = 20
number_of_rows = 24
number_of_columns = 5

window = t.Screen()
window.addshape('local.gif')
window.addshape('home.gif')
window.bgpic("tutorial.gif")
window.setup(width=1000, height=700)
window.tracer(0)

def set_game_state(state):
    global current_state
    current_state = state

def local_state(x,y): 
    global current_state

    current_state = 'local'

def help_state(x,y): 
    global current_state,on_help_screen
    if on_help_screen == False:
     current_state = 'help'
     on_help_screen = True
    else:
        current_state = 'home'
        on_help_screen = False


def home_state(x,y): 
    global current_state
    print(current_state)
    current_state = 'home'

# Function to handle home screen logic
def home_screen():
    global button_local,home_initialised,window,debug_mode
    global home_button
    window.bgpic("tutorial.gif")
    if debug_mode == True:
     print(home_initialised)
    #Init Local button
    if home_initialised == False:
      home_initialised = True

      print(home_initialised)
      button_local = t.Turtle()

    button_local.showturtle()
    button_local.shape('local.gif')
    button_local.shapesize(stretch_wid=0.001, stretch_len=1000)
    
    button_local.penup()
    button_local.goto(0,-100)
    button_local.onclick(local_state)
    window.update()



def hide_home():
  global button_local,window
  button_local.hideturtle()

  

    
    

# Function for LocalCoOp state
def local_coop():
    global current_game_state,block_list,current_time,winner_count_left,winner_count_right,window,last_hit_player, block_break_count_left, block_break_count_right,end_match
    # Your existing game code goes here, integrated as part of local_coop
    global winner_count_left,winner_count_right,block_break_count_right,block_break_display_left,help_button
    global ball,left_paddle,right_paddle,count_display_right,count_display_left,block_break_display_right,block_break_display_left,help_button
    global total_points_left,total_points_right
    hide_home()
    window.bgcolor("black")
    window.bgpic("nopic")
    button_local.hideturtle()

    #initilaise the Block class
    class Block:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.block_turtle = t.Turtle()  
            self.block_turtle.shape("square")  
            self.block_turtle.color("green")  
            self.block_turtle.penup()  
            self.set_position(x, y)  
            
        def set_position(self, x, y):
            self.block_turtle.goto(x, y)  

        def hide(self):
            self.block_turtle.hideturtle() 

        def get_position(self):
            return self.x, self.y


    def is_collision(block, ball):
        return abs(block.block_turtle.xcor() - ball.xcor()) < 5 and abs(block.block_turtle.ycor() - ball.ycor()) < 5

    def collision(block,ball):
        return abs(ball.distance(block.block_turtle)) <30





    def setup():
        t.penup()
        t.hideturtle()
        t.pencolor("white")
        t.fillcolor("white")
        t.pensize(4)
        t.goto(-500, 350)
        t.pendown()
        
        for i in range(2):
            t.forward(1000)
            t.right(90)
            t.forward(700)
            t.right(90)
        

    # Left Paddle setup
    left_paddle = t.Turtle()
    left_paddle.speed(0)
    left_paddle.shape("square")
    left_paddle.color("#FF4500")
    left_paddle.shapesize(stretch_wid=7, stretch_len=1)
    left_paddle.penup()
    left_paddle.goto(-450, 0)

    # Right Paddle setup
    right_paddle = t.Turtle()
    right_paddle.speed(0)
    right_paddle.shape("square")
    right_paddle.color("#007BFF")
    right_paddle.shapesize(stretch_wid=7, stretch_len=1)
    right_paddle.penup()
    right_paddle.goto(450, 0)

    ball = t.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(right_paddle.xcor() - 20, right_paddle.ycor())
    ball.dx = 7.5
    ball.dy = -7.5



    current_time = time.time()

    time_delta = 0


    def launch_ball():
            global ball_moving,launch_player
            if not ball_moving:
                if launch_player == 'right':
                    
                    ball.goto(right_paddle.xcor() - 50, right_paddle.ycor())
                else:
                    
                    ball.goto(left_paddle.xcor() + 20, left_paddle.ycor())
                ball_moving = True

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
    window.onkeypress(launch_ball, 'space')




    gameover = False
      
    winner_count_left = 0
    winner_count_right = 0
    block_break_count_right = 0
    block_break_count_left = 0
    block_list = []

    def blocks():
        global starting_x, starting_y
        global block_list
        global block_grid  # Make sure to include the block_grid
        global block_width,block_height,gap,number_of_rows,number_of_columns
        # Constants

        # Calculate total dimensions
        total_width = (block_width * number_of_columns) + (gap * (number_of_columns - 1))
        total_height = (block_height * number_of_rows) + (gap * (number_of_rows - 1))

        # Calculate starting points
        starting_x = -total_width / 2
        starting_y = total_height / 2

        for row in range(number_of_rows):
            for col in range(number_of_columns):
                # Only try to spawn a block if there isn't one already at this grid position
                if block_grid[row][col] == 0:
                    if random.randint(0, 8) == 1:
                        x = starting_x + (block_width + gap) * col
                        y = starting_y - (block_height + gap) * row
                        block = Block(x, y)  # Instantiate a Block object
                        block.set_position(x, y)
                        block_list.append(block)
                        block_grid[row][col] = 1  # Update the block_grid to show a block exists at this position



    
    def main():
     global winner_count_right
     global winner_count_left
     global last_hit_player, block_break_count_left, block_break_count_right,end_match
     global ball,left_paddle,right_paddle,count_display_right,count_display_left,block_break_display_right,block_break_display_left

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
     count_display_left.pencolor("white")
     count_display_right.pencolor("white")
     count_display_left.write('0',align="left",font=('',30,'normal'))
     count_display_right.write('0',align="right",font=('',30,'normal'))








     gameover = False
     global current_time,ball_moving,launch_player,tutorial,spawning
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
              winner_count_right+=5
          else:
              winner_count_left+=5
          print(total_points_left)
          print(total_points_right)
          count_display_right.clear()
          count_display_left.clear()
          count_display_left.write(winner_count_left,align="left",font=('',30,'normal'))
          count_display_right.write(winner_count_right,align="right",font=('',30,'normal'))

          test = ball.goto(right_paddle.xcor()-40,right_paddle.ycor())
          print(test)
          if x < 0:
              launch_player = 'right'
          else:
              launch_player = 'left'
          launch_ball()
          ball_moving = False
          gameover=False


        # Calculate the time delta
        new_time = time.time()
        time_delta = new_time - current_time
        current_time = new_time
        
        if ball_moving == True:
            ball.setx(ball.xcor() + (ball.dx * time_delta * 60))
            ball.sety(ball.ycor() + (ball.dy * time_delta * 60))
        
        if ball_moving == False:
          if launch_player == 'right':
            ball.sety(right_paddle.ycor()) 
            ball.setx(right_paddle.xcor() - 20)  
          else:
            ball.sety(left_paddle.ycor())
            ball.setx(left_paddle.xcor() + 20)



        move_paddles()
        window.update()
        
        x= (ball.xcor())
        
        if x < -200:
           last_hit_player == 'left'
        elif x > 200:
            last_hit_player == 'right'
        if random.randint(0,200)==1:
            blocks()


        for block in block_list:
         x, y = block.get_position()
         col = int((x - starting_x) / (block_width + gap))
         row = int((starting_y - y) / (block_height + gap))

         if collision(block, ball): 
            block_grid[row][col] = 0
            block.hide()
            block_list.remove(block)

            if last_hit_player == 'left':
                    winner_count_left += 1
                    count_display_left.clear()
                    count_display_left.write(winner_count_left,align="left",font=('',30,'normal'))
                    window.update()
        
            elif last_hit_player == 'right':
                    winner_count_right += 1
                    count_display_right.clear()
                    count_display_right.write(winner_count_right,align="right",font=('',30,'normal'))
                    window.update()
                   



        # Determine the side where the collision happened 
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
            last_hit_player = 'right'
        
        if (ball.dx < 0) and (ball.xcor() < -420 and ball.xcor() > -450) and (ball.ycor() > left_paddle.ycor() - 70 and ball.ycor() < left_paddle.ycor() + 100):
            ball.dx *= -1
            last_hit_player = 'left'


        if end_match == False :
          total_points_left = winner_count_left
          total_points_right = winner_count_right
          if winner_count_left >= 10 or winner_count_right >= 10:
           print("game over!!")
           end_match = True
           
           set_game_state("over")
           print(current_state)
           window.update()
           break

    blocks()
    setup()
    main()

def online_coop():
   
    pass


def game_over():
    
    global window,ball,left_paddle,right_paddle,count_display_right,count_display_left,block_break_display_right,block_break_display_left,game_over_initialised,winner_count_left,winner_count_right,block_break_count_right,block_break_count_left,home_button_exists,home_button,end_match

    global winner
    global total_points_right
    global total_points_left
    end_match = False 
    window.bgpic("bg.gif")
    winner = t.Turtle()
    winner.speed(0)
    winner.goto(0,150)
    winner.hideturtle()
    winner.pencolor("white")
    count_display_left.clear()
    count_display_right.clear()
    
    if game_over_initialised == False:
     t.clear()
     print("test")
     ball.hideturtle()
     left_paddle.goto(300,500)
     print(ball.xcor())
     right_paddle.hideturtle()
     count_display_right.hideturtle()
     count_display_left.hideturtle()



     for block in block_list:
      block.hide()
    
     print(total_points_right)
     print(total_points_left)
     if winner_count_left > winner_count_right:
            winner.clear()
            winner.write('Winner is red!',align="center", font=('', 30, 'normal'))
            print("test")
     else:
            winner.clear()
            winner.write('Winner is blue!',align="center", font=('', 30, 'normal'))
            print("test")

    home_button = t.Turtle()
    home_button.shape('home.gif')
    home_button.shapesize(stretch_wid=0.001, stretch_len=1000)
    
    home_button.penup()
    home_button.goto(0,0)
    home_button.onclick(home_state)
    home_initialised = False
    home_button_exists = True
    
    while current_state == 'over':
     window.update()

    
    


    





# Initialize turtle window

# Start game at the home screen
set_game_state("home")

# Main game loop
while True:
    if debug_mode == True:
     print("in loop")
    if current_state == "home":
        if home_button_exists == True:
            home_button.hideturtle()
            winner.clear()
        home_screen()
    elif current_state == "local":
        home_initialised = False  # Reset flag since we're no longer in home screen
        local_coop()
    elif current_state == "online":
        home_initialised = False  # Reset flag since we're no longer in home screen
        online_coop()
    elif current_state == 'over':
        home_initialised = False
        game_over()
        
    time.sleep(0.1)  # Add a slight delay to avoid overwhelming the CPU





















