def carnes (gallinas:float,gallos:float,pollitos:float) ->float:
    return gallinas*6+gallos*7+pollitos
if __name__ == "__main__":
    gallinas=float(input("Escribe cuantas gallinas se pesaran: "))
    gallos=float(input("Escribe cuantos gallos se pesaran: "))
    pollitos=float(input("Escribe cuantos pollitos se pesaran: "))
    kilos=carnes(gallinas,gallos,pollitos)
    print(f"En total se tienen {kilos} de carne")