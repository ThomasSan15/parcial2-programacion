from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import date
from .Producto import Producto

if TYPE_CHECKING:
    from .Cliente import Cliente


class Factura:
    def __init__(self, fecha: date, cliente: Cliente):
        if not isinstance(fecha, date):
            raise TypeError(
                "fecha debe ser datetime.date"
            )

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

    def agregar_producto(
        self,
        producto: Producto
    ):
        if not isinstance(
            producto,
            Producto
        ):
            raise TypeError(
                "Se debe agregar una "
                "instancia de Producto"
            )

        self._productos.append(
            producto
        )

        self._recalcular_suma()

    def _recalcular_suma(self):
        self._total = sum(
            p.valor
            for p in self._productos
        )

    def calcular_total(self):
        self._recalcular_suma()
        return self._total

    def __str__(self):
        nombres = [
            p.nombre
            for p in self._productos
        ]

        return (
            f"Factura del {self._fecha} "
            f"para {self._cliente.nombre}, "
            f"productos: {nombres}, "
            f"total pagado: "
            f"{int(self._total)}"
        )
