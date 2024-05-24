class Inventario:
    productos = []

    def __init__(self, nombre =None, categoria=None, precio=None, cantidad=None, proveedor=None):
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio
        self._cantidad = cantidad
        self._proveedor = proveedor
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria
    
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, precio):
        self._precio = precio
    
    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad
    
    @property
    def proveedor(self):
        return self._proveedor
    
    @proveedor.setter
    def proveedor(self, proveedor):
        self._proveedor = proveedor

    def agregar_producto(self):
        proveedor = input('Ingrese el nombre del proveedor: ')
        categoria = input('Ingrese la categoria del producto: ')
        nombre = input('Ingrese el nombre del producto: ')
        cantidad = input('Ingrese la cantidad de productos: ')
        precio = float(input('Ingrese el precio del producto: '))

        producto = Inventario(proveedor, categoria, nombre, cantidad, precio)
        Inventario.productos.append(producto)
    
    def actualizar_producto(self):
        nombre = input('Ingrese el nombre del producto a actualizar: ')
        producto_encontrado = False

        for producto in Inventario.productos:
            if producto.nombre == nombre:
                producto.proveedor = input('Ingrese el nombre del nuevo proveedor: ')
                producto.categoria = input('Ingrese el nuevo nombre: ')
                producto.cantidad = input('Ingrese la nueva cantidad: ')
                producto.precio = float(input('Ingrese el nuevo precio: '))
                producto_encontrado = True
                break
        
        if not producto_encontrado:
            print('No se encontró el producto.')
    
    def eliminar_producto(self):
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        producto_encontrado = False

        for i, producto in enumerate(Inventario.productos):
            if producto.nombre == nombre:
                del Inventario.productos[i]
                producto_encontrado = True
                break
        
        if not producto_encontrado:
            print("No se encontró el producto.")

    def mostrar_inventario(self):
        if not Inventario.productos:
            print("El inventario está vacío.")
        else:
            for producto in Inventario.productos:
                print(f"Nombre: {producto.nombre}")
                print(f"Categoría: {producto.categoria}")
                print(f"Precio: {producto.precio}")
                print(f"Cantidad: {producto.cantidad}")
                print(f"Proveedor: {producto.proveedor}")
                print()

    def buscar_producto(self):
        criterio_busqueda = input("Ingrese el criterio de búsqueda: ")
        productos_encontrados = []

        for producto in Inventario.productos:
            if criterio_busqueda.lower() in producto.nombre.lower() or \
                criterio_busqueda.lower() in producto.categoria.lower():
                productos_encontrados.append(producto)

        if productos_encontrados:
            for producto in productos_encontrados:
                print(f"Nombre: {producto.nombre}")
                print(f"Categoría: {producto.categoria}")
                print(f"Precio: {producto.precio}")
                print(f"Cantidad: {producto.cantidad}")
                print(f"Proveedor: {producto.proveedor}")
                print()
        else:
            print("No se encontraron productos.")

inventario = Inventario()

# Bucle principal
while True:
    print("\nMenú:")
    print("1. Agregar producto")
    print("2. Actualizar producto")
    print("3. Eliminar producto")
    print("4. Mostrar inventario")
    print("5. Buscar producto")
    print("6. Salir")

    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        Inventario().agregar_producto()
    elif opcion == "2":
        Inventario().actualizar_producto()
    elif opcion == "3":
        Inventario().eliminar_producto()
    elif opcion == "4":
        Inventario().mostrar_inventario()
    elif opcion == "5":
        Inventario().buscar_producto()
    elif opcion == "6":
        break
    else:
        print("Opción no válida.")
