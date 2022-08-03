num_leap_year = 0                                            # Iniciar la variable para almacenar el número de años.
leap_year = int(input("Introduce un año para calcular..."))  # Pregunta el año de inicio.

for i in range(leap_year, leap_year + 100, 1):               # Bucle para comprobar los años bisiestos.
    if i % 4 == 0:                                           # Comprobación inicial.
        num_leap_year += 1                                   # Incrementa contador.
        if i % 100 == 0 and i % 400 != 0:                    # Comprueba años múltiplos de 100 y 400.
            num_leap_year -= 1                               # Decrementa contador.

print("El número de años bisiestos es", num_leap_year)       # Imprime resultado.
