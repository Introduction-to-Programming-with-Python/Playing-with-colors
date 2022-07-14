import matplotlib.pyplot as plt
import random
import matplotlib.image as mpimg

def cargar_imagen(ruta_imagen: str)-> list:
    """ Carga la imagen que se encuentra en la ruta dada.
    Parámetros:
        ruta_imagen (str) Ruta donde se encuentra la imagen a cargar.
    Retorno:
        list: Matriz de MxN con tuplas (R,G,B).
    """
    matriz = mpimg.imread(ruta_imagen).tolist()
    alto = len(matriz)
    ancho = len(matriz[0])
    imagen = []
    for i in range(alto):
        fila = []
        for j in range(ancho):
            tupla = tuple(matriz[i][j])
            fila.append(tupla)
        imagen.append(fila)
    return imagen

def visualizar_imagen(matriz:list)->None:
    """ Muestra la imagen recibida
    Parámetros:
        imagen (list): Matriz de MxN con tuplas (R,G,B) que representan la imagen a visualizar.
    """
    plt.figure(figsize = (1,1))
    plt.axis('off')
    plt.imshow(matriz)
    plt.show()

def convertir_negativo(imagen: list) -> list:
    """  Convierte la imagen en negativo.
    El negativo se calcula cambiando cada componente RGB, tomando el valor absoluto de restarle al componente 1.0.
    Parámetros:
        imagen (list) Matriz de MxN con tuplas (R,G,B) que representan la imagen a convertir a negativo.
    """
    copia = []
    alto = len(imagen)
    ancho = len(imagen[0])

    for i in range(alto):
        fila = []
        for j in range(ancho):
            r, g, b = imagen[i][j]
            nuevo = (abs(r-1.0), abs(g-1.0), abs(b-1.0))
            fila.append(nuevo)
        copia.append(fila)
    return copia

def reflejar_imagen(imagen: list)->list:
    """Refleja la imagen.
    Consiste en intercambiar las columnas enteras de la imagen, de las finales a la iniciales.
    Parámetros:
        imagen (list) Matriz de MxN con tuplas (R,G,B) que representan la imagen a reflejar.
    """
    copia = []
    alto = len(imagen)
    ancho = len(imagen[0])

    for i in range(-1, -(alto), -1):
        fila = []
        for j in range(ancho):
            r, g, b = imagen[i][j]
            nuevo = (r, g, b)
            fila.append(nuevo)
        copia.append(fila)
    return copia

def binarizar_imagen(imagen: list, umbral: float)->list:
    """ Binariza la imagen.
    Consiste en llevar cada pixel de una imagen a negro o blanco.
    Para ello se requiere un umbral: si el promedio de los componentes RGB del pixel está por encima o igual se lleva a blanco y si está por debajo se lleva a negro.
    Parámetros:
        imagen (list) Matriz de MxN con tuplas (R,G,B) que representan la imagen a binarizar.
        umbral (float) Umbral de la binarización.
     """
    copia = []
    alto = len(imagen)
    ancho = len(imagen[0])

    for i in range(alto):
        fila = []
        for l in range(ancho):
            r, g, b = imagen[i][l]
            promedio = (r + g + b) / 3
            if promedio >= umbral:
                r, g, b = 1.0, 1.0, 1.0
            else:
                r, g, b = 0, 0, 0
            pixel = (r, g, b)
            fila.append(pixel)
        copia.append(fila)

    return copia

def convertir_a_grises(imagen: list)->list:
    """ Convierte la imagen a escala de grises.
    Para ello promedia los componentes de cada pixel y crea un nuevo color donde cada componente (RGB) tiene el valor de dicho promedio.
    Parámetros:
        imagen (list) Matriz de MxN con tuplas (R,G,B) que representan la imagen a convertir a grises.
    """
    copia = []
    
    alto = len(imagen)
    ancho = len(imagen[0])

    for i in range(alto):
        fila = []
        for l in range(ancho):
            r, g, b = imagen[i][l]
            promedio = (r + g + b) / 3
            r, g , b = promedio, promedio, promedio
            pixel = (r, g, b)
            fila.append(pixel)
        copia.append(fila)

    return copia