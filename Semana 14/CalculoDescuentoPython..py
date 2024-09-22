def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento y devuelve el monto del descuento.

    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento (default es 10).
    :return: Monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


if __name__ == "__main__":
    # Primera llamada a la función
    monto1 = 100  # Monto total de la compra
    descuento1 = calcular_descuento(monto1)
    total_final1 = monto1 - descuento1
    print(f"Monto Total: {monto1}, Descuento: {descuento1}, Total a Pagar: {total_final1}")

    # Segunda llamada a la función con un porcentaje de descuento diferente
    monto2 = 200  # Monto total de la compra
    porcentaje2 = 15  # Porcentaje de descuento
    descuento2 = calcular_descuento(monto2, porcentaje2)
    total_final2 = monto2 - descuento2
    print(f"Monto Total: {monto2}, Descuento: {descuento2}, Total a Pagar: {total_final2}")
