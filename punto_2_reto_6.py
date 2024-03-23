import math

def area_total (base : float, altura : float, radio : float) -> float:
    area_cuadrado = base *altura
    area_circulo = math.pi*radio**2
    area_total = area_cuadrado + 2*area_circulo
    return area_total

def perimetro_total (base : float, altura : float, radio : float) -> float:
    perimetro_cuadrado = 2*(base+altura)
    perimetro_circulo = 2*math.pi*radio
    perimetro_total = perimetro_cuadrado + 2*perimetro_circulo
    return perimetro_total

if __name__ == "__main__":
    base = float (input("Ingrese la base del rectangulo: "))
    altura = float (input("Ingrese la altura del rectangulo: "))
    radio = float (input("Ingrese el radio de los circulos: "))
    perimetro_total = perimetro_total (base, altura, radio )
    print (f"El perimetro total del rectangulo con el circulo es: {perimetro_total} [m]")
    area_total = area_total (base, altura, radio )
    print (f"El area total del rectangulo con el circulo es: {area_total} [m^2]")
    