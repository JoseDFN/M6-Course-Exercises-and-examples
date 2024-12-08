import turtle

def draw_triangle():
    """Dibuja un triángulo equilátero usando el módulo turtle."""
    window = turtle.Screen()  # Crear una ventana
    window.bgcolor("white")   # Configurar color de fondo

    triangle_turtle = turtle.Turtle()  # Crear la tortuga
    triangle_turtle.color("green")     # Color de la tortuga
    triangle_turtle.speed(2)           # Velocidad de dibujo
    triangle_turtle.pensize(3)         # Grosor del trazo

    for _ in range(3):                 # Dibujar tres lados
        triangle_turtle.forward(150)   # Avanzar 150 píxeles
        triangle_turtle.left(120)      # Girar 120 grados a la izquierda

    window.mainloop()  # Mantener la ventana abierta

if __name__ == "__main__":
    # Llamar a la función
    draw_triangle()
