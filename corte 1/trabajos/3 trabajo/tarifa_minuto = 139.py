tarifa_minuto = 139

minutos_estacionamiento = int(input("Ingrese la cantidad de minutos de estacionamiento: "))


costo_sin_iva = tarifa_minuto * minutos_estacionamiento


iva = costo_sin_iva * 0.16


costo_total_con_iva = costo_sin_iva + iva


costo_redondeado = ((costo_total_con_iva + 49) // 50) * 50


print(f"Costo total sin IVA: ${costo_sin_iva}")
print(f"IVA (16%): ${iva}")
print(f"Costo total con IVA: ${costo_total_con_iva}")
print(f"Costo redondeado al siguiente múltiplo de $50: ${costo_redondeado}")
