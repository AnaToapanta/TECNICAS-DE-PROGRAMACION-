class Animal:
    def hablar(self):
        raise NotImplementedError("Subclase debe implementar este método")


class Perro(Animal):
    def hablar(self):
        return "¡Guau!"


class Gato(Animal):
    def hablar(self):
        return "¡Miau!"


def hacer_hablar(animal):
    return animal.hablar()


mi_perro = Perro()
mi_gato = Gato()

print(hacer_hablar(mi_perro))
print(hacer_hablar(mi_gato))