"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

#Importación de librerías
from random import randrange
from turtle import *
from freegames import vector

#Variables utilizadas en el juego
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

#Esta función obtiene información para la velocidad de la bola según el lugar donde hagas click
def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200

#Esta función crea las pelotas y los globos
def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

#Aqui se hace que los globos aparezcan de manera aleatoria y que se muevan hacia la izquierda
def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)
        
    #Esto establece la dirección y velocidad de los globos    
    for target in targets:
        target.x -= 0.5
    
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()
    
    ontimer(move, 25)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()