import math
pi=math.pi
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