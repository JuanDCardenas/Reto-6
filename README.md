# Reto-6
Por: Juan Diego Cárdenas Olarte
### Grupo: 
#### Infinity Bit Team (∞BT)

[![logo.jpg](https://i.postimg.cc/pdcVKPsT/logo.jpg)](https://postimg.cc/JyJWLCVV)

Este reto contiene las actividades propuestas para el reto#6.
>### 1. Superficie y Volumen
El primer punto del reto plantea que: Dada la siguiente imagen realizar:

  [![img1.png](https://i.postimg.cc/KjK42S6m/img1.png)](https://postimg.cc/tnj93fRc)
  
* Una función matemática para calcular el volumen y el área superficial.
```python
#Función matemática: V= (4/3)π(r**3)+(1/3)π(r**2)h    S=4π(r**2)+ πr(r**2+h**2)**0.5+π(r**2)
```
* Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
 
```python
def volumen (radio_esfera:float,radio_cono:float,altura_cono:float) -> float :
    volumen_esfera:float= (4/3)*pi*(radio_esfera)**3
    volumen_cono:float= (1/3)*pi*(radio_cono)**2*(altura_cono)
    return volumen_cono+volumen_esfera

def superficie (radio_esfera:float,radio_cono:float,alatura_cono:float) -> float:
    superficie_esfera:float= 4*pi*(radio_esfera)**2
    superficie_cono:float= pi*(radio_cono)*((radio_cono**2+alatura_cono**2)**0.5)+pi*(radio_cono)**2
    return superficie_esfera+superficie_cono


if __name__ == "__main__":
    radio_esfera=float(input("Escribe el radio de la esfera: "))
    radio_cono=float(input("Escribe el radio de el cono: "))
    altura_cono=float(input("Escribe la altura del cono: "))
    volumen_total=volumen(radio_esfera,radio_cono,altura_cono)
    superficie_total=superficie(radio_esfera,radio_cono,altura_cono)
    print(f"La superficie de la figura segun las medidas dadas es de {superficie_total}")
    print(f"El volumen de la figura segun las medidas dadas es de volumen_total {volumen_total}")
```
* Revise como utilizar el valor de pi usando import math y math.pi
Se importara la libreria math para posteriormente inicializar una variable con valor de la funcion math.pi == 3.1416...
```python
import math
pi=math.pi
```

*Desarrollo y funcionamiento del progrma completo en los codigos adjuntos reto_6.1*

>### 2. Area y Perimetro
El segundo punto del reto plantea que: Dada la figura de la imagen realice:

  [![img2.png](https://i.postimg.cc/0yFPrHhW/img2.png)](https://postimg.cc/pmfg6kWz)

* Una función matemática para calcular el área y el perimetro.
  ```python
  # Funcion matematica:  A= ab+2π(r**2)   P=2a+2b+2πr
  ```
* Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
  ```python
    def area (radio_circulos:float,lado_a:float,lado_b:float) -> float:
    area_rectangulo:float=lado_a*lado_b
    area_circulos:float=2*pi*(radio_circulos**2)
    return area_circulos+area_rectangulo
  def perimetro (radio_circulos:float,lado_a:float,lado_b:float) -> float:
    perimetro_rectangulo:float=2*lado_a+2*lado_b
    perimetro_circulo:float=2*pi*radio_circulos
    return perimetro_circulo+perimetro_rectangulo
  if __name__== "__main__":
    radio_circulos=float(input("Escribe un radio para los circulos: "))
    lado_a=float(input("Escribe un lado a para el rectangulo: "))
    lado_b=float(input("Escribe un lado b para el rectangulo: "))
    area_total=area(radio_circulos,lado_a,lado_b)
    perimetro_total=perimetro(radio_circulos,lado_a,lado_b)
    print(f"El area de la figura con las medidas dadas es de {area_total}")
    print(f"El perimetro de la figura con las medidas dadas es de {perimetro_total}")
  ```
* Revise como utilizar el valor de pi usando import math y math.pi
Este punto ya fue explicado al realizar *reto_6.1*

*Desarrollo y funcionamiento del progrma completo en los codigos adjuntos reto_6.2*

>### 3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.
  ```python
def carnes (gallinas:float,gallos:float,pollitos:float) ->float:
    return gallinas*6+gallos*7+pollitos
if __name__ == "__main__":
    gallinas=float(input("Escribe cuantas gallinas se pesaran: "))
    gallos=float(input("Escribe cuantos gallos se pesaran: "))
    pollitos=float(input("Escribe cuantos pollitos se pesaran: "))
    kilos=carnes(gallinas,gallos,pollitos)
    print(f"En total se tienen {kilos} de carne")
  ```
*Desarrollo y funcionamiento del progrma completo en los codigos adjuntos reto_6.3*

>### 4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

  ```python
def compras (pan:float,leche:float,huevos:float,billete:float)->float:
    return (pan*300+leche*3300+huevos*350)-billete
if __name__ == "__main__":
    pan=float(input("Escribe cuantos panes se compran: "))
    leche=float(input("Escribe cuantas bolsas de leche se compran: "))
    huevos=float(input("Escribe cuantos huevos se compran: "))
    billete=float(input("Escribe con cuanto se pagara: "))
    vuelto=compras(pan,leche,huevos,billete)
    if vuelto==0:
        print("No hay vueltos")
    elif vuelto>0:
        print(f"Se deben {vuelto} pesos")
    else :
        print(f"El vuelto es de {-(vuelto)} pesos")
  ```

*Desarrollo y funcionamiento del progrma completo en los codigos adjuntos reto_6.4*

>### 5. Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

  ```python
def prestamo (capital_inicial:float,interes:float,tiempo:float)->float:
    return capital_inicial*(1+(interes/100))**tiempo
if __name__ == "__main__":
  capital_inicial=float(input("Escriba el capital inicial del prestamo: "))
  interes=float(input("Escriba el porcentaje de interes mensual del prestamo: "))
  tiempo=float(input("Escriba en cuantos meses se pagara el prestamo: "))
  valor_final=prestamo(capital_inicial,interes,tiempo)
  print(f"Con un prestamo inicial de {capital_inicial} a una tasa del {interes}% mensual durante {tiempo} meses se debera un total de {valor_final} pesos.")
  ```

*Desarrollo y funcionamiento del progrma completo en los codigos adjuntos reto_6.5*

>### 6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

  ```python
def contagiados (dias_transcurridos:float,contagiados_iniciales:float)->float:
    return contagiados_iniciales*(2**dias_transcurridos)
if __name__ == "__main__":
  contagiados_iniciales=float(input("Escriba el numero de contagiados que habia en un principio: "))
  dias_transcurridos=float(input("Escriba cuantos dias han transcurrido: "))
  contagiados_finales=contagiados(dias_transcurridos,contagiados_iniciales)
  print(f"El numero de contagiados tras {dias_transcurridos} dias de que hubieran {contagiados_iniciales} contagiados es de {contagiados_finales}")
  ```
*Desarrollo y funcionamiento del progrma completo en los codigos adjuntos reto_6.6*

>### 7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:

Para la amyoria de las funciones que se realizaron para este punto se usa una misma linea de instrucciones, que es la siguiente:

  ```python
  if a<=b and a<=c and a<=d and a<=e :
    n1=a
    if b<=c and b<=d and b<=e :
        n2=b
        if c<=d and c<=e :
            n3=c
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=c and d<=e :
            n3=d
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif e<=c and e<=d :
            n3=e
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
    elif c<=b and c<=d and c<=e :
        n2=c
        if b<=d and b<=e :
            n3=b
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=b and d<=e :
            n3=d
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=d :
            n3=e
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
    elif d<=b and d<=c and d<=e :
        n2=d
        if b<=c and b<=e :
            n3=b
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=b and c<=e :
            n3=c
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=c :
            n3=e
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
    elif e<=b and e<=c and e<=d :
        n2=e
        if b<=c and b<=d :
            n3=b
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=b and c<=d :
            n3=c
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif d<=b and d<=c :
            n3=d
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
  elif b<=a and b<=c and b<=d and b<=e :
    n1=b
    if a<=c and a<=d and a<=e :
        n2=a
        if c<=d and c<=e :
            n3=c
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=c and d<=e :
            n3=d
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif e<=c and e<=d :
            n3=e
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
    elif c<=a and c<=d and c<=e :
        n2=c
        if a<=d and a<=e :
            n3=a
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=a and d<=e :
            n3=d
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=d :
            n3=e
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
    elif d<=a and d<=c and d<=e :
        n2=d
        if a<=c and a<=e :
            n3=a
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=a and c<=e :
            n3=c
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=c :
            n3=e
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
    elif e<=a and e<=c and e<=d :
        n2=e
        if a<=c and a<=d :
            n3=a
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=a and c<=d :
            n3=c
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
        elif d<=a and d<=c :
            n3=d
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
  elif c<=a and c<=b and c<=d and c<=e :
    n1=c
    if a<=b and a<=d and a<=e :
        n2=a
        if b<=d and b<=e :
            n3=b
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=b and d<=e :
            n3=d
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=d :
            n3=e
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
    elif b<=a and b<=d and b<=e :
        n2=b
        if a<=d and a<=e :
            n3=a
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=a and d<=e :
            n3=d
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=d :
            n3=e
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
    elif d<=a and d<=b and d<=e :
        n2=d
        if a<=b and a<=e :
            n3=a
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif b<=a and b<=e :
            n3=b
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=b :
            n3=e
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
    elif e<=a and e<=b and e<=d :
        n2=e
        if a<=b and a<=d :
            n3=a
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif b<=a and b<=d :
            n3=b
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
        elif d<=a and d<=b :
            n3=d
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
  elif d<=a and d<=b and d<=c and d<=e :
    n1=d
    if a<=b and a<=c and a<=e :
        n2=a
        if b<=c and b<=e :
            n3=b
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=b and c<=e :
            n3=c
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=c :
            n3=e
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
    elif b<=a and b<=c and b<=e :
        n2=b
        if a<=c and a<=e :
            n3=a
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=a and c<=e :
            n3=c
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=c :
            n3=e
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
    elif c<=a and c<=b and c<=e :
        n2=c
        if a<=b and a<=e :
            n3=a
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif b<=a and b<=e :
            n3=b
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=b :
            n3=e
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
    elif e<=a and e<=b and e<=c :
        n2=e
        if a<=b and a<=c :
            n3=a
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
        elif b<=a and b<=c :
            n3=b
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
        elif c<=a and c<=b :
            n3=c
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
  elif e<=a and e<=b and e<=c and e<=d :
    n1=e
    if a<=b and a<=c and a<=d :
        n2=a
        if b<=c and b<=d :
            n3=b
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=b and c<=d :
            n3=c
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif d<=b and d<=c :
            n3=d
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
    elif b<=a and b<=c and b<=d :
        n2=b
        if a<=c and a<=d :
            n3=a
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=a and c<=d :
            n3=c
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
        elif d<=a and d<=c :
            n3=d
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
    elif c<=a and c<=b and c<=d :
        n2=c
        if a<=b and a<=d :
            n3=a
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif b<=a and b<=d :
            n3=b
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
        elif d<=a and d<=b :
            n3=d
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
    elif d<=a and d<=b and d<=c :
        n2=d
        if a<=b and a<=c :
            n3=a
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
        elif b<=a and b<=c :
            n3=b
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
        elif c<=a and c<=b :
            n3=c
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
  ```

Estas instrucciones permiten organizar los datos segun cual es mayor y cual menor.
Por cuestiones de optimizar el contenido del README, a esta linea de instrucciones se le denotara como <organizar> de aqui en adelante.

* El promedio

  ```python
  def promedio (a:float,b:float,c:float,d:float,e:float)->float:
      return (a+b+c+d+e)/5
  ```
* La mediana
  
  ```python
  def mediana (a:float,b:float,c:float,d:float,e:float)->float:
      <organizar>
      return n3
  ```
* El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  
  ```python
  def promedio_multiplicativo (a:float,b:float,c:float,d:float,e:float)->float:
    return(a*b*c*d*e)**0.5
  ```
* Ordenar los números de forma ascendente
  
  ```python
  def orden_ascendente (a:float,b:float,c:float,d:float,e:float)->float:
    <organizar>
     return n1, n2, n3, n4, n5
  ````
* Ordenar los números de forma descendente

  ```python
  def orden_descendente (a:float,b:float,c:float,d:float,e:float)->float:
    <organizar>
    return n5, n4, n3, n2, n1
  ````
* La potencia del mayor número elevado al menor número
  ```python
  def mayor_elevado_menor (a:float,b:float,c:float,d:float,e:float)->float:
    <organizar>
    return n5**n1
  ````
  
* La raíz cúbica del menor número
  
  ```python
  def raiz_menor (a:float,b:float,c:float,d:float,e:float)->float:
    <organizar>
    return n1**(1/3)
  ````

Para finalizar con este punto se inicializan las variables necesarias y se imprimen los datos requeridos.

  ```python
if __name__ == "__main__":
    a=float(input("Escribe un numero: "))
    b=float(input("Escribe otro numero: "))
    c=float(input("Escribe otro numero: "))
    d=float(input("Escribe otro numero: "))
    e=float(input("Escribe un ultimo numero: "))
promedio_one=promedio(a,b,c,d,e)
mediana_one=mediana(a,b,c,d,e)
promedio_multiplicativo_one=promedio_multiplicativo(a,b,c,d,e)
orden_ascendente_one=orden_ascendente(a,b,c,d,e)
orden_descendente_one=orden_descendente(a,b,c,d,e)
mayor_elevado_menor_one=mayor_elevado_menor(a,b,c,d,e)
raiz_menor_one=raiz_menor(a,b,c,d,e)
print(f"El promedio de {a}, {b},{c}, {d} y {e} es {promedio_one}")
print(f"La mediana de {a}, {b},{c}, {d} y {e} es {mediana_one}")
print(f"El promedio multiplicativo de {a}, {b},{c}, {d} y {e} es {promedio_multiplicativo_one}")
print(f"Ordenados de forma ascendente {a}, {b},{c}, {d} y {e} serian {orden_ascendente_one}")
print(f"Ordenados de forma descendente {a}, {b},{c}, {d} y {e} serian {orden_descendente_one}")
print(f"El resultado de elevar el numero mayor al menor es {mayor_elevado_menor_one}")
print(f"El resultado de sacarle la raiz cubica al numero menor es {raiz_menor_one}")
  ````
*Todo el codigo se encuentra unido, y listo para su comprobacion en los aduntos, punto_6.7*
