from datetime import date
from modelo.Factura import Factura
from modelo.Cliente import Cliente

class CRUDFactura:
    def __init__(self):
        # Lista interna de facturas registradas
        self._facturas = []

    def CrearFactura(self, cliente: Cliente):
        
        factura = Factura(date.today(), cliente)
        self._facturas.append(factura)
        cliente.AgregarFactura(factura)  # Relación cliente-factura
        return factura

    def ListarFacturas(self):
        return [str(facturas) for facturas in self._facturas]
