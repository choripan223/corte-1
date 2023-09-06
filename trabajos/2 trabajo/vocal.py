ef es_vocal_letra(letra):
    vocales = ['a', 'e', 'i', 'o', 'u']
    return letra.lower() in vocales

def main():
    caracter = input("pon una letra del abecedario: ")

    if len(caracter) == 1 and caracter.isalpha():
        if es_vocal_letra(caracter):
            print(f"{caracter} es  vocal.")
        else:
            print(f"{caracter} es  consonante.")
    else:
        print("Por favor, ingrese un único caracter del abecedario.")

if __name__ == "__main__":
    main()
