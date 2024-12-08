try:
    with open("archivo.txt", "r") as archivo:
        contenido = archivo.read()

except FileNotFoundError:
    print("El archivo no se ha encontrado...")
    print("Creando el archivo...")
    with open("archivo.txt", "w") as archivo:
        archivo.write("Hola mundo")
else:
        print("Contenido del archivo: ")
        print(contenido)
""""finally:
    if archivo:
        archivo.close()"""