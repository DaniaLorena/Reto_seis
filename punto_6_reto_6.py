def total_contagiados (dias : int, num_contagiados : int) ->float:
    contagiados_total = num_contagiados * (2**dias)
    return contagiados_total

if __name__ == "__main__":
    num_contagiados = int (input("¿Cuantos contageados hay actualmentes?: "))
    dias = int (input ("¿Cuantos dias han pasado a partir de hoy?: "))
    total_contagiados = total_contagiados (dias, num_contagiados)
    print (f"Actualemente hay {total_contagiados} contagiados tras empezar con {num_contagiados} de contagiados y pasar {dias} dias")