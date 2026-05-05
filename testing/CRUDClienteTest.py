import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from datetime import date
from CRUD.CRUDCliente import CRUDCliente
from CRUD.CRUDFactura import CRUDFactura
from CRUD.CRUDProducto import CRUDProducto


class TestCRUDCliente(unittest.TestCase):
    def setUp(self):
        self.clientes = CRUDCliente()
        self.facturas = CRUDFactura()
        self.productos = CRUDProducto()

    def test_crear_y_buscar_cliente(self):
        cliente = self.clientes.CrearCliente("Carlos Ramírez", 789654)
        self.assertEqual(cliente.nombre, "Carlos Ramírez")
        self.assertEqual(cliente.cedula, 789654)

        encontrado = self.clientes.BuscarPorCedula(789654)
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.nombre, "Carlos Ramírez")

    def test_cliente_con_factura_y_productos(self):
        cliente = self.clientes.CrearCliente("Lucía Gómez", 111222)
        factura = self.facturas.CrearFactura(cliente)

        f = self.productos.CrearFertilizante("AgroVida", 40000, "ICA-F-2024", "Cada 30 días", date(2025, 10, 25))
        c = self.productos.CrearControlPlaga("Cyperkill", 32000, "ICA-C-8899", "Cada 15 días", "10 días")

        factura.AgregarProducto(f)
        factura.AgregarProducto(c)

        total = factura.CalcularTotal()
        self.assertEqual(total, 72000)
        self.assertEqual(len(cliente.pedidos), 1)
        self.assertEqual(len(cliente.pedidos[0].productos), 2)

    def test_mostrar_facturas_por_cedula(self):
        cliente = self.clientes.CrearCliente("Laura", 333444)
        factura = self.facturas.CrearFactura(cliente)

        p = self.productos.CrearFertilizante("FertiMax", 50000, "ICA-F-5555", "Cada 30 días", date(2025, 11, 1))
        factura.AgregarProducto(p)
        factura.CalcularTotal()

        print("\n===== RESULTADO MOSTRAR FACTURAS POR CÉDULA =====")
        self.clientes.MostrarFacturasPorCedula(333444)

if __name__ == "__main__":
    unittest.main()
