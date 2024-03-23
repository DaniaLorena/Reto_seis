from math import *

def volumen_total (radio_uno: float, radio_dos : float, altura : float) ->float:
    volumen_esfera = (4*pi*radio_uno**3)/3
    volumen_cono = (pi*altura*radio_dos)/3
    volumen_total = volumen_cono + volumen_esfera
    return volumen_total

def area_total (radio_uno: float, radio_dos : float, altura : float) ->float:
    area_cono : float= pi*radio_dos*(radio_dos + sqrt(radio_dos**2+altura**2))
    area_esfera = 4*pi*radio_uno**2
    area_total = area_cono + area_esfera
    return area_total


if __name__ == "__main__":
    radio_uno = float (input("Ingrese el radio de la esfera: "))
    radio_dos = float (input("Ingrese el radio del cono: "))
    altura = float (input ("Ingrese la altura del cono: "))
    opcion = int (input("Ingrese el numero de la opcion que desea saber , [1]Volumen, [2]Area Superficial: "))
    if (opcion == 1):
        volumen_total = volumen_total (radio_uno, radio_dos, altura)
        print (f"El volumento total de las figuras es: {volumen_total} [m^3]")
    if (opcion == 2):
        area_total = area_total (radio_uno, radio_dos, altura)
        print (f"El volumento total de las figuras es: {area_total} [m^2]")
else: 
    print ("Esa opcion no es adecuada")