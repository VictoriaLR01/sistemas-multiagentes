import ClasesRepaso

if __name__ == "__main__":
    bus1 = ClasesRepaso.Autobus("Independencia",29060,4,30)
    bus2 = ClasesRepaso.Autobus("Circunvalación",18891,8,51)
   
    ambulancia1 = ClasesRepaso.Ambulancia("Zambrano",135972,10,70)
    ambulancia2 = ClasesRepaso.Ambulancia("Los Angeles",8753,1,130)
    
    
    lista = [bus1,bus2,ambulancia1,ambulancia2]

    for elem in lista:
        if isinstance(elem,ClasesRepaso.Autobus):
            print(f'{elem} es Autobus')
            elem.ahorra()
        elif isinstance(elem,ClasesRepaso.Ambulancia):
            print(f'{elem} es Ambulancia')
            elem.en_peligro()
