import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("bouncing ball")
wn.tracer(0)

balls = []

for _ in range(20):
    balls.append(turtle.Turtle())

colors = ['blue', 'red', 'green', 'purple', 'yellow', 'white']
shapes = ['circle', 'triangle', 'square', ]
for ball in balls:
    ball.shape(random.choice(shapes))
    ball.color(random.choice(colors))
    ball.penup()
    ball.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(200, 400)
    ball.goto(x, y)
    ball.dy = 0
    ball.dx = random.randint(-3, 3)
    ball.da = random.randint(-5, 5)

gravity = 0.1

while True:
    wn.update()

    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)

        #check collision
        if ball.xcor() > 300:
            ball.dx *= -1

        if ball.xcor() < -300:
            ball.dx *= -1
            ball.da *= -1

        #check bounce
        if ball.ycor() < -300:
            ball.dy *= -1
            ball.da *= -1



wn.mainloop()