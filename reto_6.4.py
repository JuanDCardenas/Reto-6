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

