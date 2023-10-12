def calcular_iva(precio_producto):
    iva = 0.19  #   es 19%
    valor_iva = precio_producto * iva
    return valor_iva

def main():
    try:
        precio_producto = float(input("Ingrese el precio del producto: "))
        valor_iva = calcular_iva(precio_producto)
        print(f"El valor del IVA es: {valor_iva:.2f}")
        precio_total_con_iva = precio_producto + valor_iva

    except ValueError:
        print("Por favor, ingrese un número válido para el precio.")

if __name__ == "__main__":
    main()
