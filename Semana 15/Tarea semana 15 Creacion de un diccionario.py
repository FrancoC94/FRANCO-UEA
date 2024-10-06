#  Diccionario
informacion_personal = {
    "nombre": " Pedro Alvarado",
    "edad": 27,
    "ciudad": "Quevedo",
    "profesion": "Ingeniero"
}

# Acceder y Modificar Valores
ciudad_actual = informacion_personal["ciudad"]
print(f"Ciudad actual: {ciudad_actual}")

# Modificar la ciudad
informacion_personal["ciudad"] = "Quevedo"

# Agregar nueva clave-valor para la profesion
informacion_personal["profesion"] = "Ingeniero en Sistemas"

# Verificar Existencia de Claves
if "telefono" not in informacion_personal:
    informacion_personal["celular"] = "0949765321"

# Eliminamos la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]


# Imprimimos el Diccionario Final
print("Diccionario final:")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")