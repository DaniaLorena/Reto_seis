def cant_carne (num_gallinas : int, num_gallo : int, num_pollito : float) -> float:
    cantidad_total = (6*num_gallinas) + (7*num_gallo)+(1*num_pollito)
    return cantidad_total

if __name__ == "__main__":
    num_gallinas = int (input("Ingrese el numero de gallinas: "))
    num_gallos = int (input("Ingrese el numero de gallos: "))
    num_pollitos = int (input("Ingrese el numero de pollitos: "))
    cant_total = cant_carne (num_gallinas, num_gallos, num_pollitos)
    print (f"La cantidad de carne entre gallinas, gallos y pollitos es de : {cant_total} [Kg]")


