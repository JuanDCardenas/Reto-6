def prestamo (capital_inicial:float,interes:float,tiempo:float)->float:
    return capital_inicial*(1+(interes/100))**tiempo
if __name__ == "__main__":
    capital_inicial=float(input("Escriba el capital inicial del prestamo: "))
    interes=float(input("Escriba el porcentaje de interes mensual del prestamo: "))
    tiempo=float(input("Escriba en cuantos meses se pagara el prestamo: "))
    valor_final=prestamo(capital_inicial,interes,tiempo)
    print(f"Con un prestamo inicial de {capital_inicial} a una tasa del {interes}% mensual durante {tiempo} meses se debera un total de {valor_final} pesos.")
