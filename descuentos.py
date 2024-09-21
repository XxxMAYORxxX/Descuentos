def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcular el monto del descuento
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Llamada a la función (primer caso: solo monto total)
monto_compra1 = 150.00
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1

# Llamada a la función (segundo caso: monto total y porcentaje de descuento)
monto_compra2 = 200.00
porcentaje_descuento2 = 15
descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
monto_final2 = monto_compra2 - descuento2

# Mostrar resultados
print(f"Monto de la compra 1: ${monto_compra1:.2f}")
print(f"Descuento aplicado: ${descuento1:.2f}")
print(f"Monto final a pagar: ${monto_final1:.2f}\n")

print(f"Monto de la compra 2: ${monto_compra2:.2f}")
print(f"Descuento aplicado: ${descuento2:.2f}")
print(f"Monto final a pagar: ${monto_final2:.2f}")
