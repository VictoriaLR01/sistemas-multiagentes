class Vehiculo():
    def __init__(self, nombre, kilometraje, antiguedad):
        self.nombre = nombre
        self.kilometraje = kilometraje
        self.antiguedad = antiguedad
    def calcula_tarifa(self):
        return (self.antiguedad * 10 + 100 / self.kilometraje)
    def muestra_anuncio(self):
        print(f'nombre: {self.nombre}')
        print(f'datos kilometraje: {self.kilometraje}')
        print(f'datos antiguedad: {self.antiguedad}')

class Autobus(Vehiculo):
     def __init__(self, nombre, kilometraje, antiguedad,cantidad_asientos):
         super().__init__(nombre,kilometraje,antiguedad)
         self.cantidad_asientos = cantidad_asientos
     def ahorra(self):
         if self.cantidad_asientos>50:
            print('True')
            return True
         else:
            print('False')
            return False
class Ambulancia(Vehiculo):
    def __init__(self, nombre, kilometraje, antiguedad,velocidad_maxima):
        super().__init__(nombre,kilometraje,antiguedad)
        self.velocidad_maxima = velocidad_maxima
    def en_peligro(self):
        if self.velocidad_maxima >120:
            print('EMERGENCIA')
        else:
            print("EN ESPERA")
    
            