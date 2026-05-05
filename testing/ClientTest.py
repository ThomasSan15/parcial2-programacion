import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from datetime import date
from modelo.Cliente import Cliente
from modelo.Factura import Factura
from modelo.Antibiotico import Antibiotico
from modelo.Fertilizante import Fertilizante
from modelo.ControlPlaga import ControlPlaga


class TestCliente(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente("Carlos Ramírez", 123456789)
        self.factura1 = Factura(date(2025, 11, 1), self.cliente)
        self.factura2 = Factura(date(2025, 11, 2), self.cliente)

        self.antibiotico = Antibiotico("Penicilina", 48000, 500, "Porcino")
        self.fertilizante = Fertilizante("AgroVida", 40000, "ICA-F-2024", "Cada 30 días", date(2025, 10, 25))
        self.control_plaga = ControlPlaga("Cyperkill", 32000, "ICA-C-8899", "Cada 15 días", "10 días")

        self.factura1.agregarProducto(self.antibiotico)
        self.factura1.agregarProducto(self.fertilizante)
        self.factura2.agregarProducto(self.control_plaga)

        self.cliente.agregarFactura(self.factura1)
        self.cliente.agregarFactura(self.factura2)

    def test_cliente_datos_basicos(self):
        self.assertEqual(self.cliente.nombre, "Carlos Ramírez")
        self.assertEqual(self.cliente.cedula, 123456789)
        self.assertEqual(len(self.cliente.pedidos), 2)

    def test_facturas_asociadas(self):
        self.assertIn(self.factura1, self.cliente.pedidos)
        self.assertIn(self.factura2, self.cliente.pedidos)

    def test_historial_cliente(self):
        total1 = self.factura1.calcular_total()
        total2 = self.factura2.calcular_total()
        self.assertEqual(total1, 88000)
        self.assertEqual(total2, 32000)
        self.assertEqual(len(self.factura1.productos), 2)
        self.assertEqual(len(self.factura2.productos), 1)

    def test_str_cliente(self):
        s = str(self.cliente)
        self.assertIn("Carlos Ramírez", s)
        self.assertIn("Facturas: 2", s)


if __name__ == "__main__":
    unittest.main()
