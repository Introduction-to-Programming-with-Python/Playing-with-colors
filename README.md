# Playing with colors

This project aims to apply some programming foundations concepts and Python functionalities applied to a image visualizer and editor program.

## Respository structure

- The folder [code](/code/) contains the code of this project.
- The folder [documentation](/documentation/) contains the repository documentation files and context about this project.
- The folder [data](/data/) contains the images to visualize.

## Statement

This [document](/documentation/statement.pdf) contains the context of the problem, requirments and functionality for each file and function.

## Objectives

This project aims to apply the following functionalities:

- Visualize images with [Matplotlib](https://matplotlib.org/).
- Load images as RGB pixels and manipulate them.

## How does it work?

Once you execute the application, the options will be displayed by the console and you can start to navegate and interact with the program with the console. The responses will be showed in a [Matplotlib](https://matplotlib.org/) window.

The file [consola_visor_imagenes.py](/code/consola_visor_imagenes.py) has one function for each requirment executing the neccesary functions from the file [visor_imagenes.py](/code/asistencia_congreso.py) that help to solve the requirments. The file [colores.py](/code/colores.py) is an additional file, this file contains functions to create colors in different ways.

You need to have installed [Matplotlib](https://matplotlib.org/).


## Execution

To execute the program you have to execute the [consola_visor_imagenes.py](/code/consola_visor_imagenes.py) file.

Before any other option, in each execution you have to execute the first option to load the one image and be able to continue with the others. Once you execute the first option you should type the data file name, it can be "imagen2.png" or "imagen3.png" .

If you want another image, you should to add it to the [data](/data/) folder.

There is not a console file to the [colores.py](/code/colores.py) file, if you want to execute any function of it, you have to write in the end of the file and without any function the following code:

    print([name of the function]([insert the parameters of the function if it is neccesary]))

Example: 

If i want to execute the "crear_matriz_de_pixeles" function I write:

    print(visualizar_imagen(crear_matriz_de_pixeles(255,255)))

And execute the [colores.py](/Code/colores.py) file.
