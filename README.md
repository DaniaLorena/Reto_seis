# Reto_seis
### Reto 6, programación de Computadoras
#### Primer punto
Dado la figura de la imagen, desarrolle:

[![Captura-de-pantalla-2024-03-22-211204.png](https://i.postimg.cc/0Q8q22M3/Captura-de-pantalla-2024-03-22-211204.png)](https://postimg.cc/B8wzm3Cc)

Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
Revise como utilizar el valor de pi usando import math y math.pi
```
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
```
#### Segundo punto
Dado la figura de la imagen, desarrolle:

[![Captura-de-pantalla-2024-03-22-211208.png](https://i.postimg.cc/MHg6TJ8Q/Captura-de-pantalla-2024-03-22-211208.png)](https://postimg.cc/30C5S6N8)

Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b
```
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
```
#### Tercer punto
Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.
```
def cant_carne (num_gallinas : int, num_gallo : int, num_pollito : float) -> float:
    cantidad_total = (6*num_gallinas) + (7*num_gallo)+(1*num_pollito)
    return cantidad_total

if __name__ == "__main__":
    num_gallinas = int (input("Ingrese el numero de gallinas: "))
    num_gallos = int (input("Ingrese el numero de gallos: "))
    num_pollitos = int (input("Ingrese el numero de pollitos: "))
    cant_total = cant_carne (num_gallinas, num_gallos, num_pollitos)
    print (f"La cantidad de carne entre gallinas, gallos y pollitos es de : {cant_total} [Kg]")
```
#### Cuarto punto
Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.
```
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
```
#### Quinto punto
Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.
```
def valor_prestamo (cant_dinero : float, interes : float, meses : float) ->float:
    prestamo = cant_dinero * (interes/100) * meses
    return prestamo

if __name__ == "__main__":
    cant_dinero = float (input("¿Cuanto dinero desear sacar prestado?:$ "))
    interes = float (input ("¿A que tasa de interes desea sacar?:$ "))
    meses = int (input("¿A cuantos meses va a pagar el prestamo?: "))
    valor_prestamo = valor_prestamo (cant_dinero, interes, meses)
    print (f"El costo total por sacar ${cant_dinero} con una tasa de interes de {interes}% por {meses} meses es de: ${cant_dinero + valor_prestamo} pesos")
```
#### Sexto punto
El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
```
def total_contagiados (dias : int, num_contagiados : int) ->float:
    contagiados_total = num_contagiados * (2**dias)
    return contagiados_total

if __name__ == "__main__":
    num_contagiados = int (input("¿Cuantos contageados hay actualmentes?: "))
    dias = int (input ("¿Cuantos dias han pasado a partir de hoy?: "))
    total_contagiados = total_contagiados (dias, num_contagiados)
    print (f"Actualemente hay {total_contagiados} contagiados tras empezar con {num_contagiados} de contagiados y pasar {dias} dias")
```
#### Septimo punto
Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
##### El promedio
```
def promedio (num_1 : float, num_2 : float, num_3 : float, num_4 : float, num_5 : float) ->float:
    promedio = (num_1 + num_2 + num_3 + num_4 + num_5)/5
    return promedio
```
##### La mediana
```
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
```
##### El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
```
def prom_mutiplicativo (num_1 : float, num_2 : float, num_3 : float, num_4 : float, num_5 : float) ->float:
    prom_mutiplicativo = (num_1*num_2*num_3*num_4*num_5)**(1/5)
    return prom_mutiplicativo
```
##### Ordenar los números de forma ascendente
```
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
```
##### Ordenar los números de forma descendente
```
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
```
##### La potencia del mayor número elevado al menor número
```
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
```
##### La raíz cúbica del menor número
```
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
```
##### Funcion principal main
```
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
```
#### Octavo punto
Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.
```
from funciones_punto_8 import *

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
```
#### Noveno punto
###### Consultar qué es y cómo funciona pip en python.
* Pip (Python Package Index)
Es el sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python.
Pip en python es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python y descargarlos a nuestra computadora con la finalidad de integrarlos a nuestros desarrollos realizado en python. Muchos paquetes pueden ser encontrados en el Python Package Index (PyPI). Python 2.7.9 y posteriores (en la serie Python2), Python 3.4 y posteriores incluyen pip (pip3 para Python3) por defecto; lo cual no es necesario instalarlo en nuestra pc ya que al instalar python en la version 3.4 o superior en automaático se instala el gestor de paquetes.

#### Décimo punto
Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.
* pip install requests (permite hacer peticiones HTTP)
(Se sigue la siguiente ruta (File - Settings - Project - Python Interpreter.), Una vez allí buscas el icono "+", En el buscador (lupa) digitas request.
Seleccionas el resultado y finalmente das clic en el boton Install Package, Esperas que el proceso de instalación finalice y ya queda listo.)
* PIP install Numpy (da soporte para crear vectores y matrices grandes multidimensionales,incluyendo funciones matemáticas de alto nivel)
* PIP install Matplotlib (realizar gráficas de funciones matemáticas.)
* PIP install Scipy (Optimiza, y contiene operaciones de álgebra lineal, integración, interpolación, funciones especiales, FFT, procesamiento de señales y de imagen, entre otras)
* PIP intall Tkinter (Sirve para la creación y el desarrollo de aplicaciones de escritorio.)
* PIP intall OpenCV (Permite desarrollar aplicaciones de visión artificial)
* PIP intall Pandas (Sirve para la manipulación y el análisis de datos en el lenguaje Python)
* PIP intall Pillow(o PIL) (Agrega soporte para abrir, manipular y guardar muchos formatos de archivo de imagen diferentes)

### Referencias
* https://jpromanonet.medium.com/como-instalar-python-y-sus-modulos-m%C3%A1s-utilizados-7ff41913de1d
* https://www.codificandobits.com/curso/numpy-ciencia-de-datos-machine-learning/2-instalacion-numpy/#instalaci%C3%B3n
* http://blog.espol.edu.ec/ccpg1001/descargas/pip-instalar-librerias/
* https://keepcoding.io/blog/que-es-tkinter/#:~:text=Tkinter%20es%20una%20librer%C3%ADa%20del,Python%20para%20interactuar%20con%20Tk.
* https://es.wikipedia.org/wiki/Pillow_(biblioteca_de_c%C3%B3digo_abierto)#:~:text=Pillow%20es%20una%20biblioteca%20adicional,Mac%20OS%20X%20y%20Linux.
