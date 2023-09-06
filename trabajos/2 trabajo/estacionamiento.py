def costo(tiempo_minutos, costo_por_minuto):
    costototal = tiempo_minutos * costo_por_minuto
    iva = costototal * 0.16  # 16% iva 
    costo_iva = costototal + iva
    costo_aproximado = round(costo_iva / 50) * 50  # Aproximar al siguiente múltiplo de $50
    return costo_aproximado

def main():
    try:
        tiempo_minutos = int(input("Ingrese el tiempo de parqueo en minutos: "))
        costo_por_minuto = 139
        
        costototal = costo(tiempo_minutos, costo_por_minuto)
        
        print(f"Costo total: ${costototal:.2f}")
        
    except ValueError:
        print("Por favor, ingrese un valor numérico válido para el tiempo de parqueo.")

if __name__ == "__main__":
    main()
