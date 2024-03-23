def valor_prestamo (cant_dinero : float, interes : float, meses : float) ->float:
    prestamo = cant_dinero * (interes/100) * meses
    return prestamo

if __name__ == "__main__":
    cant_dinero = float (input("¿Cuanto dinero desear sacar prestado?:$ "))
    interes = float (input ("¿A que tasa de interes desea sacar?:$ "))
    meses = int (input("¿A cuantos meses va a pagar el prestamo?: "))
    valor_prestamo = valor_prestamo (cant_dinero, interes, meses)
    print (f"El costo total por sacar ${cant_dinero} con una tasa de interes de {interes}% por {meses} meses es de: ${cant_dinero + valor_prestamo} pesos")


