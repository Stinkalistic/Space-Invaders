import turtle
import time
current = time.time()
start_time = current

display = turtle.Screen()
display.setup(430,430)
display.bgpic("space.jpg")

player = turtle.Turtle()
player.speed(0)
display.addshape("spaceship.png")
player.shape("spaceship.png")
player.pu()
player.goto(0,-180)
player.left(90)
player.speed(7)
 
lasers = []
laserframecounter = 0 
def  space():
  global laserframecounter
  if laserframecounter > 45     :
    laser = turtle.Turtle()
    laser.hideturtle()
    display.addshape("laser.png")
    laser.shape("laser.png")
    laser.tracer(0,0) 
    laser.color("red") 
    laser.pu()
    laser.goto(player.xcor(),player.ycor())
    lasers.append(laser)
    laser.left(90)
    laser.showturtle()
    laserframecounter = 0
    
def checkhitplayer():
  for alien in aliens: 
    if alien.distance(player) < 35  and alien.isvisible():
      global game_over
      print("dead") 
      game_over = True
score = 0
display.onkey(space, "space")
alien_xpos = 0
def makealien(alien, alienycor):
  global alien_xpos
  global alienxdir
  alien.pu()
  display.addshape("alien.png")
  alien.speed(0)
  alien.shape("alien.png")
  alien.goto(alien_xpos,alienycor)
  alien_xpos = (alien_xpos + 35)
  alien.color("green")
  alien.left(90)
  alien.speed(5) 
  alien.tracer(0,0)
  alienxdir = 2

aliens = [turtle.Turtle(),turtle.Turtle(),turtle.Turtle()]
for alien in aliens:
  makealien(alien,200)

def alienmove(xchange):
  for alien in aliens:
    alien.goto(alien.xcor()+xchange,alien.ycor())
def aliendrop():
  for alien in aliens:
    alien.sety(alien.ycor()-20)
def alienmostx():
  most = -200
  for alien in aliens:
    if alien.xcor() > most and alien.isvisible():
      most = alien.xcor()
  return most
def alienleastx():
  least = 200
  for alien in aliens:
    if alien.xcor() < least and alien.isvisible():
      least = alien.xcor()
  return least
  
def lasermove(speed):
  for laser in lasers:
    laser.sety(laser.ycor()+speed)
def checkhit():
  for laser in lasers:
    for alien in aliens:
      global score
      if alien.distance(laser) < 20 and alien.isvisible() == True:
        alien.hideturtle()
        score = (score+1)
        
        
scorewrite = turtle.Turtle()
scorewrite.pu()
scorewrite.goto(-180,180)
scorewrite.pd()
scorewrite.color("white")
scorewrite.hideturtle()

timer = 0
def reset_timer():
  global start_time
  start_time = time.time()

def time_passed():
  return time.time() - start_time

def left():
  player.goto(player.xcor()-5,player.ycor())
def right():
  player.goto(player.xcor()+5,player.ycor())

display.onkey(right,"right")
display.onkey(left,"left")
display.listen()

alienperwave = 3

game_over = False
while game_over == False:
  if time_passed() > 9.9:
    alien_xpos = -100
    alienperwave = (alienperwave + 1)
    for i in range(alienperwave): 
      aliens.append(turtle.Turtle())
      if alien_xpos > 200:
        alien_xpos = -100 
      makealien(aliens[-1],150)
    reset_timer()
  checkhitplayer()
  scorewrite.clear()
  scorewrite.write(score) 
  laserframecounter = (laserframecounter+1)
  prevy_pos = alien.ycor()
  if not alienmostx() > 200:
    alienmove(alienxdir)
  if alienmostx() > 200:
    aliendrop()
    if not alien.ycor == prevy_pos:
      alienxdir = (alienxdir * -1)
      alienmove(alienxdir * 2)
   
  if not alienleastx() < -200:
    alienmove(alienxdir)
  if alienleastx() < -200:
    aliendrop()
    if not alien.ycor == prevy_pos:
      alienxdir = (alienxdir * -1)
      alienmove(alienxdir * 2)
  alien.update()
  
  lasermove(10)
  checkhit()
