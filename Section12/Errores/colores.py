class ColorNoValidoError(Exception):
    def __init__(self, color)-> None:
        super().__init__(f"El color {color} no se encuentra en la lista...")

def colores(color):
    lista_colores = ["azul", "verde", "rojo", "amarillo"]

    if color not in lista_colores:
        raise ColorNoValidoError(color)
    

try:    
    colores("morado")
except ColorNoValidoError as error:
    print(f"Error: {error}")