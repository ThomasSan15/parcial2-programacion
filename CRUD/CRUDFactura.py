from datetime import date
from modelo.Factura import Factura
from modelo.Cliente import Cliente


class CrudFactura:
    def __init__(self):
        # Lista interna de facturas registradas
        self._facturas = []

    def crear_factura(self, cliente: Cliente):
        factura = Factura(date.today(), cliente)
        self._facturas.append(factura)
        cliente.agregar_factura(factura)  # Relación cliente-factura
        return factura

    def listar_facturas(self):
        return [str(factura) for factura in self._facturas]
