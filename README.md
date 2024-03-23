# Reto-6
Por: Juan Diego Cárdenas Olarte
### Grupo: 
#### Infinity Bit Team (∞BT)
[![logo.jpg](https://i.postimg.cc/pdcVKPsT/logo.jpg)](https://postimg.cc/JyJWLCVV)

Este reto contiene las actividades propuestas para el reto#6.
### 1. Superficie y Volumen
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
