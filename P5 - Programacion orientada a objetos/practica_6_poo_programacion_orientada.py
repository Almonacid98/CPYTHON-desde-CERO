class Camisetas:
    def __init__(self, marca, precio, talla, color):
        self.marca = marca
        self.precio = precio
        self.talla = talla
        self.color = color
        self.rebajado = False

    def aplicar_descuento(self, porcentaje):
        self.precio = self.precio - self.precio*porcentaje/100
        if porcentaje < 100:
            self.rebajado = True

    def info_producto(self):
        info = f"Descripcion de la camiseta:\nMarca: {self.marca}\nPrecio: ${self.precio:.2f}\nTalla: {self.talla}\nColor: {self.color}\n"
        if self.rebajado:
            info += "ESTE PRODUCTO ESTA REBAJADO\n"
        return info


camiseta = Camisetas("Nike", 100.12, "S", "azul")
camiseta_adidas = Camisetas("Adidas", 20.1, "M", "Verde")
print(camiseta_adidas.precio)

print(camiseta_adidas.precio)

camiseta.aplicar_descuento(20)
print(camiseta.precio)

print(camiseta.info_producto())
print(camiseta_adidas.info_producto())