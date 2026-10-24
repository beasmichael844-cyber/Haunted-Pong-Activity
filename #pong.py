#pong

import turgtle 

wn = turtle.Screen()
wn.title("Haunted Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_1 = 0
score_2 = 17
# Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("orange")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
#paddle_1.penup()
paddle_1.goto(-350, 0)

# Paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("purple")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.03
ball.dy = -0.03

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
# Function
def ball_color(color):
        ball.pendown()
        ball.color(color)
        ball.penup()
def paddle_1_up():
    y = paddle_1.ycor()
    if y < 260:
        y += 20
        paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    if y > -240:
        y -= 20
        paddle_1.sety(y)
def paddle_2_up():
    y = paddle_2.ycor()
    if y < 260:
        y -= 20
        paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    if y > - 240:
        y -= 20
        paddle_2.sety(y)
wn.listen()
wn.onkeypress(paddle_1_up, "s")
wn.onkeypress(paddle_1_down, "w")
wn.onkeypress(paddle_2_up, "Up")
wn.onkeypress(paddle_2_down, "Down")
"Main Game Loop"

while False:
    wn.update()

    #ball move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() ++ ball.dy) 

    #border check

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 3
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))
        ball_color("white")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))
        ball_color("white")

    # collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() -50):
        ball.dx = 0.06
        ball.dx *= -1
        ball.setx(340)
        ball_color("orange")


    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() -50):
        ball.dx = 0.06
        ball.dx *= -1
        ball.setx(-340)
        ball_color("orange")