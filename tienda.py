class Producto:

    SUPERMERCADO: int = 1
    PAPELERIA: int = 2
    DROGUERIA: int = 3
    IVA_SUPERMERCADO: float = 0.04
    IVA_PAPELERIA: float = 0.16
    IVA_DROGUERIA: float = 0.12

    def __init__(self, nombre, tipo, precio, cantidad_bodega, cantidad_minima):
        self.nombre= nombre
        self.tipo = tipo
        self.cantidad_bodega = cantidad_bodega
        self.cantidad_minima = cantidad_minima
        self.unidades_vendidas = 0


class Tienda:
    def __init__(self):
        self.dinero_en_caja = 0

        self.productos = [
        Producto("Leche", Producto.SUPERMERCADO, 3000, 10, 3) ,
        Producto("Lapiz", Producto.PAPELERIA, 500, 50, 10) ,
        Producto("Caja de Aspirinas", Producto.DROGUERIA, 8000, 20, 5) ,
        Producto("Libra de Papa capira", Producto.SUPERMERCADO, 10000, 10, 4) 

        ]

        # self.producto_1 = Producto("Leche", Producto.SUPERMERCADO, 3000, 10, 3) 
        # self.producto_2 = Producto("Lapiz", Producto.PAPELERIA, 500, 50, 10) 
        # self.producto_3 = Producto("Caja de Aspirinas", Producto.DROGUERIA, 8000, 20, 5) 
        # self.producto_4 = Producto("Libra de Papa capira", Producto.SUPERMERCADO, 10000, 10, 4) 
