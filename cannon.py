#A00827826 Edgar Castillo
#A01570852 Luis Martínez

"""
Programa del juego Cannon o tiro parabólico.
"""

#Librerías
from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200) #Posición inicial de la pelota cuando se lanza.
speed = vector(0, 0)
targets = [] #Vector indefinido de objetivos o globos.
color = ['blue','yellow','green','pink','orange','black','brown','purple'] #Colores que pueden tomar los objetivos.
index = randrange(8) #Cada vez que se abre un nuevo juego los objetivos toman un color distinto.


def tap(x, y):
    """Función que hace que la pelota se lance según el click del usuario. Si clickea fuera
    se interpreta como si estuviera al borde de los límites.
    """
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):
    """Función que denota si una pelota o un objetivo está dentro o fuera de la ventana.
    Si está dentro regresa True.
    """
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    """Función en la que se dibujan tanto objetivos como la pelota. Como se dijo antes todos los
    objetivos tomarán un color distinto cada vez que se corra el código. La pelota se mantendrá con
    un color blanco.
    """
    clear()
    
    #Para objetivos
    for target in targets:
        goto(target.x, target.y)
        dot(20, color[index])

    #Para la pelota
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'white')

    update()

def move():
    """Función que describe el movimiento de los objetivos y la pelota.
    """
    
    #Se crean los globos de manera aleatoria. Se les da una altura específica pero randomizada.
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    #Se reduce un poco el eje x de los objetivos.
    for target in targets:
        target.x -= 0.5
    
    #Se reduce la velocidad de la pelota.
    if inside(ball):
        speed.y -= 0.2 #Se reduce menos velocidad (Antes era de -0.35)
        ball.move(speed)
    
    #Líneas de código para eliminar los globos cuando pasa la pelota sobre ellos. Se crea otra lista igual a la de objetivos.
    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()
    
    #Esto hace que el juego sea infinito y lo que se sale de la ventana vuelva a reaparecer al inicio de la misma
    for target in targets:
        if not inside(target):
            target.x = 200
    
    #Con esto se aumenta la velocidad de todo el juego. Estaba en 50, fue cambiado a 25. La función move será llamada cada 25 milisegundos.
    ontimer(move, 15)
    

#Características de la ventana.
setup(420, 420, 370, 0) #Dimensiones
bgcolor('black') #Color
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()