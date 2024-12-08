import turtle

def draw_square():
    """Dibuja un cuadrado usando el módulo turtle."""
    window = turtle.Screen()  # Crear una ventana
    window.bgcolor("white")   # Configurar color de fondo

    square_turtle = turtle.Turtle()  # Crear la tortuga
    square_turtle.color("blue")      # Color de la tortuga
    square_turtle.speed(2)           # Velocidad de dibujo

    for _ in range(4):               # Dibujar cuatro lados
        square_turtle.forward(100)   # Avanzar 100 píxeles
        square_turtle.left(90)       # Girar 90 grados a la izquierda

    window.mainloop()  # Mantener la ventana abierta

if __name__ == "__main__":
    # Llamar a la función
    draw_square()