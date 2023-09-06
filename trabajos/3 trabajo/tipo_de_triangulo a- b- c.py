def tipo_de_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"


def es_triangulo(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)


a = float(input("ingresa el lado a: "))
b = float(input("Ingresa el lado b: "))
c = float(input("Ingresa el lado c: "))


if es_triangulo(a, b, c):
    tipo = tipo_de_triangulo(a, b, c)
    print(f"Se puede formar un triángulo {tipo}.")
else:
    print("No se puede formar un triángulo con estas longitudes.")