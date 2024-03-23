def contagiados (dias_transcurridos:float,contagiados_iniciales:float)->float:
    return contagiados_iniciales*(2**dias_transcurridos)
contagiados_iniciales=float(input("Escriba el numero de contagiados que habia en un principio: "))
dias_transcurridos=float(input("Escriba cuantos dias han transcurrido: "))
contagiados_finales=contagiados(dias_transcurridos,contagiados_iniciales)
print(f"El numero de contagiados tras {dias_transcurridos} dias de que hubieran {contagiados_iniciales} contagiados es de {contagiados_finales}")