from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import date
from .Producto import Producto

if TYPE_CHECKING:
    from .Cliente import Cliente

class Factura:
    def __init__(self, fecha: date, cliente: Cliente):  
        if not isinstance(fecha, date):
            raise TypeError("fecha debe ser datetime.date")
        self._fecha = fecha
        self._cliente = cliente
        self._productos = []
        self._total = 0.0

    @property
    def fecha(self):
        return self._fecha

    @property
    def cliente(self):
        return self._cliente

    @property
    def productos(self):
        return self._productos[:]

    @property
    def total(self):
        return self._total

    def AgregarProducto(self, producto: Producto):
        if not isinstance(producto, Producto):
            raise TypeError("Se debe agregar una instancia de Producto")
        self._productos.append(producto)
        self._RecalcularSuma()

    def _RecalcularSuma(self):
        self._total = sum(p.valor for p in self._productos)

    def CalcularTotal(self):
        self._RecalcularSuma()
        return self._total

    def __str__(self):
        nombres = [p.nombre for p in self._productos]
        return (f"Factura del {self._fecha} para {self._cliente.nombre}, "
                f"productos: {nombres}, total pagado: {int(self._total)}")
