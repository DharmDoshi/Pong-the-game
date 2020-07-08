import turtle
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#score
score_a = 0
score_b = 0

#net
net = turtle.Turtle()
net.speed(0)
net.shape("square")
net.shapesize(stretch_wid = 300, stretch_len = 0.01)
net.color("white")
net.penup()
net.goto(0,0)

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = -0.2

#pen_a
pen_a = turtle.Turtle()
pen_a.speed(0)
pen_a.color("red")
pen_a.penup()
pen_a.hideturtle()
pen_a.goto(-100, 260)
pen_a.write("Player A: 0" , align="right", font=("Arial", 20, "normal"))

#pen_b
pen_b = turtle.Turtle()
pen_b.speed(0)
pen_b.color("blue")
pen_b.penup()
pen_b.hideturtle()
pen_b.goto(100, 260)
pen_b.write("Player B: 0" , align="left", font=("Arial", 20, "normal"))


#function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 50
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 50
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 50
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 50
    paddle_b.sety(y)

#keyboard input
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

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
        score_a += 1
        pen_a.clear()
        pen_a.write("Player A: {} ".format(score_a), align="right", font=("Arial", 20, "normal"))



    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen_b.clear()
        pen_b.write("Player B: {} ".format(score_b), align="left", font=("Arial", 20, "normal"))


    #paddle and ball
    if ball.xcor() > 330 and (ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40) and (ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(330)
        ball.dx *= -1

    if ball.xcor() < -330 and (ball.xcor() < -320) and (ball.ycor() < paddle_a.ycor() + 40) and (ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-330)
        ball.dx *= -1
