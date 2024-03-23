def costo_compra (num_panes : int, num_leche : int, num_huevos : float) -> float:
    costo = (300*num_panes) + (3300*num_leche)+(350*num_huevos)
    return costo

if __name__ == "__main__":
    num_panes = int (input("Ingrese el numero de panes: "))
    num_leche = int (input("Ingrese el numero de bolsas de leche: "))
    num_huevos = int (input("Ingrese el numero de huevos: "))
    billete = float (input("Ingrese la cantidad del billete con el que va a pagar: "))
    costo_total = costo_compra (num_panes, num_leche, num_huevos)
    if (costo_total < billete):
        print (f"La compra fue por {costo_total} por lo cual le sobran $ {billete-costo_total} pesos")
    elif (costo_total > billete):
        print (f"La compra fue por {costo_total} por lo cual queda debiendo $ {costo_total-billete} pesos")
    else:
        print (f"La compra fue por $ {costo_total} y pago con $ {billete} por lo que no queda debiendo y ni le sobran vueltas")
