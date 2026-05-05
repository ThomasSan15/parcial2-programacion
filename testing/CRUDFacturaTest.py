import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from datetime import date
from CRUD.CRUDFactura import CRUDFactura
from CRUD.CRUDCliente import CRUDCliente
from CRUD.CRUDProducto import CRUDProducto


class TestCRUDFactura(unittest.TestCase):
    def setUp(self):
        self.clientes = CRUDCliente()
        self.facturas = CRUDFactura()
        self.productos = CRUDProducto()

        self.cliente = self.clientes.CrearCliente("Laura", 12345)
        self.factura = self.facturas.CrearFactura(self.cliente)

    def test_crear_factura(self):
        self.assertEqual(len(self.facturas._facturas), 1)
        self.assertEqual(self.factura.cliente.nombre, "Laura")
        self.assertIn(self.factura, self.cliente.pedidos)

    def test_agregar_productos_a_factura(self):
        productoFertilizante = self.productos.CrearFertilizante("AgroVida", 40000, "ICA-F-2024", "Cada 30 días", date(2025, 10, 25))
        productoControlPlaga = self.productos.CrearControlPlaga("Cyperkill", 32000, "ICA-C-8899", "Cada 15 días", "10 días")

        self.factura.AgregarProducto(productoFertilizante)
        self.factura.AgregarProducto(productoControlPlaga)

        total = self.factura.CalcularTotal()
        self.assertEqual(total, 72000)
        self.assertEqual(len(self.factura.productos), 2)

if __name__ == "__main__":
    unittest.main()
