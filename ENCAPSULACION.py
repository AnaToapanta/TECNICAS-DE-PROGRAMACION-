# Definimos una clase base 'Animal' con un método abstracto 'hablar'
class Animal:
    def hablar(self):
        pass  # Método vacío que se sobrescribirá en las clases hijas

# Definimos una clase hija 'Perro' que hereda de 'Animal'
class Perro(Animal):
    def hablar(self):
        return "Guau!"

# Definimos otra clase hija 'Gato' que también hereda de 'Animal'
class Gato(Animal):
    def hablar(self):
        return "Miau!"

# Creamos instancias de las clases 'Perro' y 'Gato'
mi_perro = Perro()
mi_gato = Gato()

# Llamamos al método 'hablar' de ambas instancias
print(mi_perro.habl