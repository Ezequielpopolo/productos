from datetime import datetime
class Producto:
    def __init__(self, id, nombre, precio, stock, codigo_barras, marca):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.codigo_barras = codigo_barras
        self.marca = marca
    def __repr__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}, Código de Barras: {self.codigo_barras}, Marca: {self.marca}"
class Venta:
    def __init__(self,lista_productos,comprador,vendedor):
        self.fecha = datetime.now().date()
        self.comprador = comprador
        self.vendedor = vendedor

class main:
    def __init__(self):
     self.lista_productos = []
     self.datos_productos = []
     self.contador_id = 0
     self.datos_venta = []
    def mostrar_productos(self):
        for productos in self.datos_productos:
            print(productos)
     
    def agregar_producto(self):
        nombre = input("Ingresá el nombre del producto: ")
        precio = float(input("Ingresá el precio del producto: "))
        stock = int(input("Ingresa el stock del producto: "))
        codigo_barras = input("Ingresá el codigo de barras del producto:")
        marca = input("Ingresá la marca del producto: ")
        id = self.contador_id
        self.contador_id +=1
        producto = Producto(id,nombre,precio,stock,codigo_barras,marca)
        self.datos_productos.append(producto)
        print("Producto agregado correctamente")
        
    def modificar_producto(self):
        productos.mostrar_productos()
        modificar_id = int(input("Ingrese el ID de la materia que desea modificar: "))
        
        if 0 <= modificar_id < len(self.datos_productos):    
            producto = self.datos_productos[modificar_id]
            nombre_modificado = input("Ingresa el nuevo nombre del producto: ")   
            precio_modificado = float(input("Ingrese el nuevo precio del producto: "))        
            stock_modificado = int(input("Ingresa el nuevo stock del producto: ")) 
            codigo_barras_modificado = input("Ingrese el nuevo codigo de barras del producto: ")
            marca_modificada = input("Ingrese la nueva marca del producto :")
            
            producto.nombre = nombre_modificado
            producto.precio = precio_modificado
            producto.stock = stock_modificado
            producto.codigo_barras = codigo_barras_modificado
            producto.marca = marca_modificada

            print("Datos modificados correctamente")
        else:
            print("ID no válido. No se realizaron modificaciones.")

        return self.datos_productos
    
    def eliminar_productos(self):
        productos.mostrar_productos()
        eliminar_id = int(input("Ingrese el ID de la persona que desea eliminar: "))
        
        producto_a_eliminar = None
        for producto in self.datos_productos:
            if producto.id == eliminar_id:
                producto_a_eliminar = producto
                break

        if producto_a_eliminar is not None:
            self.datos_productos.remove(producto_a_eliminar)
            print("Producto eliminado correctamente.")
        else:
            print("ID no válido. No se ha eliminado ningun producto.")
        return self.datos_productos
    
    def crear_venta(self):
        while True:
            vendedor = input("Ingrese el nombre del vendedor: ")
            comprador = input("Ingrese el nombre del comprador: ")
            for productos in self.datos_productos:
                print(productos)                
            p = input("Desea ingresar otro producto? ")
            if p == "no":
                break
        suma_productos = sum(producto.precio for producto in self.datos_productos)
        self.monto = suma_productos
        venta = Venta(self.lista_productos,comprador,vendedor)
        self.datos_venta.append(venta)
        print(f"""Vendedor: {vendedor}
                  Comprador: {comprador}
                  Fecha: {self.fecha}
                  El monto total es de {self.monto} pesos""")
productos = main()
while True:
    pregunta = input("""
1- Agregar producto
2- Mostrar Productos
3- Modificar producto
4- Eliminar producto
5- Crear una venta
6- Salir
Elija una opción: """).lower()
    
    if pregunta == "1":
        productos.agregar_producto()
        
    elif pregunta == "2":
        productos.mostrar_productos()
        
    elif pregunta == "3":
        productos.modificar_producto()
        
    elif pregunta == "4":
        productos.eliminar_productos()
    elif pregunta == "5":
        productos.crear_venta()
    elif pregunta == "6":
        break
        
        