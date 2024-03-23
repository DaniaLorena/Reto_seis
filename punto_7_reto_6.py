def promedio (num_1 : float, num_2 : float, num_3 : float, num_4 : float, num_5 : float) ->float:
    promedio = (num_1 + num_2 + num_3 + num_4 + num_5)/5
    return promedio

def prom_mutiplicativo (num_1 : float, num_2 : float, num_3 : float, num_4 : float, num_5 : float) ->float:
    prom_mutiplicativo = (num_1*num_2*num_3*num_4*num_5)**(1/5)
    return prom_mutiplicativo

def mediana (num_1 : float, num_2 : float, num_3 : float, num_4 : float, num_5 : float) ->float:
    if num_1 > num_2 :
        num_1 , num_2 = num_2 , num_1
    if num_2 > num_3 :
        num_2 , num_3 = num_3 , num_2
    if num_3 > num_4:
        num_3 , num_4 = num_4, num_3
    if num_4 > num_5 :
        num_4 , num_5 = num_5 , num_4
    if num_1 > num_2 :
        num_1 , num_2 = num_2, num_1
    if num_2 > num_3 :
        num_2 , num_3 =num_3 , num_2
    if num_3 > num_4:
        num_3, num_4 = num_4 , num_3
    if num_1 > num_2 :
        num_1, num_2 = num_2 , num_1
    if num_2 > num_3 :
        num_2 , num_3 = num_3 , num_2
    if num_1 > num_2 :
        num_1 , num_2 = num_2 , num_1
    return num_3
              
def orden_ascedente (num_1 : float, num_2 : float, num_3 : float, num_4 : float, num_5 : float) ->float:
    if num_1 > num_2 :
        num_1 , num_2 = num_2 , num_1
    if num_2 > num_3 :
        num_2 , num_3 = num_3 , num_2
    if num_3 > num_4:
        num_3 , num_4 = num_4, num_3
    if num_4 > num_5 :
        num_4 , num_5 = num_5 , num_4
    if num_1 > num_2 :
        num_1 , num_2 = num_2, num_1
    if num_2 > num_3 :
        num_2 , num_3 =num_3 , num_2
    if num_3 > num_4:
        num_3, num_4 = num_4 , num_3
    if num_1 > num_2 :
        num_1, num_2 = num_2 , num_1
    if num_2 > num_3 :
        num_2 , num_3 = num_3 , num_2
    if num_1 > num_2 :
        num_1 , num_2 = num_2 , num_1
    return (num_1, num_2, num_3, num_4, num_5)

def orden_descendente (num_1 : float, num_2 : float, num_3 : float, num_4 : float, num_5 : float) ->float:
    if num_1 > num_2 :
        num_1 , num_2 = num_2 , num_1
    if num_2 > num_3 :
        num_2 , num_3 = num_3 , num_2
    if num_3 > num_4:
        num_3 , num_4 = num_4, num_3
    if num_4 > num_5 :
        num_4 , num_5 = num_5 , num_4
    if num_1 > num_2 :
        num_1 , num_2 = num_2, num_1
    if num_2 > num_3 :
        num_2 , num_3 =num_3 , num_2
    if num_3 > num_4:
        num_3, num_4 = num_4 , num_3
    if num_1 > num_2 :
        num_1, num_2 = num_2 , num_1
    if num_2 > num_3 :
        num_2 , num_3 = num_3 , num_2
    if num_1 > num_2 :
        num_1 , num_2 = num_2 , num_1
    return (num_5, num_4, num_3, num_2, num_1)

def potencia (num_1 : float, num_2 : float, num_3 : float, num_4 : float, num_5 : float) ->float:
    if num_1 > num_2 :
        num_1 , num_2 = num_2 , num_1
    if num_2 > num_3 :
        num_2 , num_3 = num_3 , num_2
    if num_3 > num_4:
        num_3 , num_4 = num_4, num_3
    if num_4 > num_5 :
        num_4 , num_5 = num_5 , num_4
    if num_1 > num_2 :
        num_1 , num_2 = num_2, num_1
    if num_2 > num_3 :
        num_2 , num_3 =num_3 , num_2
    if num_3 > num_4:
        num_3, num_4 = num_4 , num_3
    if num_1 > num_2 :
        num_1, num_2 = num_2 , num_1
    if num_2 > num_3 :
        num_2 , num_3 = num_3 , num_2
    if num_1 > num_2 :
        num_1 , num_2 = num_2 , num_1
    potencia = num_5**num_1
    return potencia

def raiz_cubica (num_1 : float, num_2 : float, num_3 : float, num_4 : float, num_5 : float) ->float:
    if num_1 > num_2 :
        num_1 , num_2 = num_2 , num_1
    if num_2 > num_3 :
        num_2 , num_3 = num_3 , num_2
    if num_3 > num_4:
        num_3 , num_4 = num_4, num_3
    if num_4 > num_5 :
        num_4 , num_5 = num_5 , num_4
    if num_1 > num_2 :
        num_1 , num_2 = num_2, num_1
    if num_2 > num_3 :
        num_2 , num_3 =num_3 , num_2
    if num_3 > num_4:
        num_3, num_4 = num_4 , num_3
    if num_1 > num_2 :
        num_1, num_2 = num_2 , num_1
    if num_2 > num_3 :
        num_2 , num_3 = num_3 , num_2
    if num_1 > num_2 :
        num_1 , num_2 = num_2 , num_1
    return num_1**1/3

if __name__ == "__main__":
    num_1 = int (input("Ingrese el primer numero: "))
    num_2 = int (input("Ingrese el segundo numero: "))
    num_3 = int (input("Ingrese el tercer numero: "))
    num_4 = int (input("Ingrese el cuarto numero: "))
    num_5 = int (input("Ingrese el quinto numero: "))
    promedio = promedio (num_1, num_2, num_3, num_4, num_5)
    print (f"El promedio es: {promedio}")
    promedio_multi =  prom_mutiplicativo (num_1, num_2, num_3, num_4, num_5)
    print (f"El pomedio multiplicativo de los numeros ingresados es: {promedio_multi}")
    mediana  = mediana (num_1, num_2, num_3, num_4, num_5)
    print (f"La mediana de los numeros igresados es: {mediana}")
    orden_ascende = orden_ascedente (num_1, num_2, num_3, num_4, num_5)
    print (f"Los numeros organizados de forma ascendente son: {orden_ascende}")
    orden_descen = orden_descendente (num_1, num_2, num_3, num_4, num_5)
    print (f"Los numeros organizados de forma descendetne son: {orden_descen}")
    potencia = potencia (num_1, num_2, num_3, num_4, num_5)
    print (f"La potencia del mayor numero elevado al menor es : {potencia}")
    raiz = raiz_cubica (num_1, num_2, num_3, num_4, num_5)
    print (f"La raiz cubica dem menor numero es: {raiz}")