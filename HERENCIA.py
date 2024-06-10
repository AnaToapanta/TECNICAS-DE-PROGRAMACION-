class Vehiculo:
    def _init_(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"


class Coche(Vehiculo):
    def _init_(self, marca, modelo, color):
        super()._init_(marca, modelo)
        self.color = color

    def describir(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}"


class Moto(Vehiculo):
    def _init_(self, marca, modelo, cilindrada):
        super()._init_(marca, modelo)
        self.cilindrada = cilindrada

    def describir(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Cilindrada: {self.cilindrada}cc"


mi_coche = Coche("Toyota", "Corolla", "Rojo")
mi_moto = Moto("Honda", "CBR600RR", 600)

print(mi_coche.describir())
print(mi_moto.describir())