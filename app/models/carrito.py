from app.models.plato import Plato

class Carrito:
    def __init__(self):
        self.carrito = []

    def agregar_producto(self, id, cantidad):
        plato = Plato.query.get(id)
        if plato:
            item = {'plato': plato, 'cantidad': cantidad}
            self.carrito.append(item)

    def eliminar_producto(self, id):
        # Buscar el item con el id del plato dado
        print(f"entra a e producto {id}")
        for item in self.carrito:
            if item['plato'].id == id:
                self.carrito.remove(item)
                break  # Romper el bucle una vez se encuentra y elimina el item
    
    def editar_producto(self, id, nueva_cantidad):
        # Buscar el ítem con el id del plato dado
        for item in self.carrito:
            if item['plato'].id == id:
                item['cantidad'] = nueva_cantidad
                break  # Romper el bucle una vez se encuentra y edita el ítem
    
    def calcular_total(self):
        return sum(item['plato'].precio * item['cantidad'] for item in self.carrito)
    
    def tamañoD(self):   
        return len(self.carrito)

    def getItems(self):
        return self.carrito
    
    def vaciarcarrito(self):
        self.carrito = []
    