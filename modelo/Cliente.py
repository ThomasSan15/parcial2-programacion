from __future__ import annotations
from .Factura import Factura

class Cliente:
    def __init__(self, nombre: str, cedula: int):
        self._nombre = nombre
        self._cedula = int(cedula)
        self._pedidos = []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, v):
        self._nombre = v

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, v):
        self._cedula = int(v)

    @property
    def pedidos(self):
        return self._pedidos[:]

    def AgregarFactura(self, factura: Factura):
        if not isinstance(factura, Factura):
            raise TypeError("Debe agregar una instancia de Factura")
        self._pedidos.append(factura)

    def MostrarDatos(self):
        print(f"Nombre: {self._nombre}")
        print(f"Cédula: {self._cedula}")
        print(f"Pedidos: [{', '.join(str(id(f)) for f in self._pedidos)}]")

    def MostrarPedidos(self):
        if not self._pedidos:
            print("No tiene facturas.")
            return
        print("\nHistorial de facturas del cliente:")
        for f in self._pedidos:
            print(f"{f}")

    def __str__(self):
        return f"Cliente: {self._nombre}, Cédula: {self._cedula}, Facturas: {len(self._pedidos)}"
