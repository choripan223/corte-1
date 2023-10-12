def calcular_imc(estatura_cm, peso_kg):
    estatura_m = estatura_cm / 100
    imc = peso_kg / (estatura_m ** 2)
    return imc

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidad Clase 1"
    elif 35 <= imc < 39.9:
        return "Obesidad Clase 2"
    else:
        return "Obesidad Clase 3"

def main():
    personas = [
        {"nombre": "Pedro Caceres", "estatura_cm": 188, "peso_kg": 97},
        {"nombre": "Maria Pérez", "estatura_cm": 160, "peso_kg": 47},
        {"nombre": "Julian Dominguez", "estatura_cm": 158, "peso_kg": 58},
        {"nombre": "Jessica Fuentes", "estatura_cm": 170, "peso_kg": 73},
    ]

    for persona in personas:
        nombre = persona["nombre"]
        estatura_cm = persona["estatura_cm"]
        peso_kg = persona["peso_kg"]
        
        imc = calcular_imc(estatura_cm, peso_kg)
        categoria = clasificar_imc(imc)
        
        print(f"{nombre}:")
        print(f"IMC: {imc:.2f}")
        print(f"Categoría IMC: {categoria}")
        print()

if __name__ == "__main__":
    main()