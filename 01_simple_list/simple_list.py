class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        else:
            self.cabeza = nuevo_nodo

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=' ')
            actual = actual.siguiente
        print()


def main():
    lista = ListaEnlazada()
    while True:
        print("\nMenu:")
        print("1. Insertar elemento en la lista")
        print("2. Mostrar lista")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            dato = input("Ingrese el valor a insertar: ")
            lista.insertar(dato)
            print(f"Valor {dato} insertado.")
        elif opcion == '2':
            print("Contenido de la lista:")
            lista.imprimir()
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()