def pulgadas_a_milimetros(pulgadas):
    milimetros = pulgadas * 25.4
    return milimetros

try:
    pulgadas = float(input("Ingrese una medida en pulgadas: "))
    milimetros = pulgadas_a_milimetros(pulgadas)
    print(f"{pulgadas} pulgadas equivale a {milimetros:.2f} milímetros.")
except ValueError:
    print("Error: Por favor ingrese un número decimal válido.")