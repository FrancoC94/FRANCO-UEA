def calcular_temperatura_promedio(datos_temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad.

    """
    promedios = {}
    for ciudad, temperaturas in datos_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        promedios[ciudad] = promedio
    return promedios

# Ciudades_Temperaturas = ¨[
datos = {
    'Qito': [20, 22, 19, 21],       #Temperatura diarias Quito
    'Cuenca': [15, 16, 14, 17],       #Temperaturas diarias Cuenca
    'Guayaquil': [30, 32, 31, 33]       #Temperaturas diarias Guayaquil
}
print("El promedio de temperatura de las ciudades son: ")
print(calcular_temperatura_promedio(datos))
