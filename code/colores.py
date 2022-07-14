import matplotlib.pyplot as plt
import random
import matplotlib.image as mpimg

def visualizar_imagen(matriz:list)->None:
    """ Muestra la imagen recibida
    Parámetros:
        imagen (list): Matriz de MxN con tuplas (R,G,B) que representan la imagen a visualizar.
    """
    plt.figure(figsize = (10,10))
    plt.axis('off')
    plt.imshow(matriz)
    plt.show()

def crear_pixel(r:int,g:int,b:int)->list:
    """Crea una imagen de 1 pixel. Recibe los valores de rojo, verde, y azul del pixel."""
    pixel = (r,g,b)
    I = [[pixel]]
    return I

def dar_color_aleatorio()->tuple:
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def crear_fila_pixeles():
    I = [[]]
    for i in range(0,256,5):
        c = (i,0,0)
        I[0].append(c)
    return I

def crear_rampas():
    I = [[],[],[]]
    for i in range(0,256,5):
        r = (i,0,0)
        g = (0,i,0)
        b = (0,0,i)
        I[0].append(r)
        I[1].append(g)
        I[2].append(b)
    return I

def crear_matriz_de_pixeles(ancho:int,alto:int)->list:
    I = []
    for i in range(0,alto):
        fila = []
        for j in range(0,ancho):
            fila.append(dar_color_aleatorio())
        I.append(fila)
    return I

print(visualizar_imagen(crear_matriz_de_pixeles(255,255)))