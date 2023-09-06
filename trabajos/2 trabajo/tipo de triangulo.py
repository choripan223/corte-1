def xd(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Equilátero"
        elif a == b or a == c or b == c:
            return "Isósceles"
        else:
            return "Escaleno"
    else:
        return "No es un triángulo"

def main():
    try:
        a = float(input(" la medida  longitud del primer lado: "))
        b = float(input("la medida longitud del segundo lado: "))
        c = float(input("la medida del tercer lado: "))
        
        triangulo = xd(a, b, c)
        print("triagulo es:", triangulo)
        
    except ValueError:
        print("lados o numerro eroneos.")

if __name__ == "__main__":
    main()
