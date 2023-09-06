
def encontrar_divisores(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def es_numero_perfecto(numero):
    divisores = encontrar_divisores(numero)
    suma_divisores = sum(divisores)
    return suma_divisores == numero

def main():
    cantidad_perfectos = int(input("Ingrese la cantidad  que desea encontrar (máximo 10): "))
    numeros_perfectos = []
    
    numero = 1
    while len(numeros_perfectos) < cantidad_perfectos and numero <= 10_000: 
        if es_numero_perfecto(numero):
            numeros_perfectos.append(numero)
        numero += 1
    
    print(f"Los {cantidad_perfectos} primeros números perfectos son:")
    for num in numeros_perfectos:
        print(num)

if __name__ == "__main__":
    main()

