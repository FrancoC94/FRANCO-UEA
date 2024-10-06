# Vamos a crear un nuevo archivo llamado my_notes.txt
with open('my_notes.txt', 'w') as file:
    # Escribimos nuestras notas personales
    file.write("Nota 1: No olvides la cita con el doctor el martes.\n")
    file.write("Nota 2: Recuerda terminar las tareas antes del fin de semana.\n")
    file.write("Nota 3: Asegúrate de que todo esté en orden al final del día.\n")
    file.write("Nota 4: Comprar frutas y verduras para la semana.\n")  # Nueva nota
    file.write("Nota 5: Llamar a mamá para ver cómo ha estado últimamente.\n")  # Nueva nota

# Leemos el contenido de my_notes.txt
with open('my_notes.txt', 'r') as file:
    # Leer línea por línea
    for line in file:
        # Muestra en la consola cada línea leída
        print(line.strip())  # Usamos strip() para eliminar espacios en blanco



