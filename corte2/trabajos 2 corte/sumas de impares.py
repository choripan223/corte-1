def suma_impares(n):
    if n == 1:
        return 1
    else:
        return n + suma_impares(n - 2)
def suma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])

if __name__ == "__main__":
  
    lista_numeros = [1, 2, 3, 4, 5]
    resultado = suma_lista(lista_numeros)
    print(f"La suma de los elementos de la lista es: {resultado}")
        
    cantidad_impares = int(input("Ingrese la cantidad de números impares a sumar: "))
    resultado = suma_impares(2 * cantidad_impares - 1)
    print(f"La suma de los primeros {cantidad_impares} números impares es: {resultado}")
