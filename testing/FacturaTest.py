import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from datetime import date
from modelo.Factura import Factura
from modelo.Cliente import Cliente
from modelo.Antibiotico import Antibiotico
from modelo.Fertilizante import Fertilizante
from modelo.ControlPlaga import ControlPlaga


class TestFactura(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente("Laura Gómez", 987654321)
        self.factura = Factura(date(2025, 11, 3), self.cliente)

        self.a = Antibiotico("Amoxivet", 48000, 500, "Porcino")
        self.f = Fertilizante("AgroVida", 40000, "ICA-F-1010", "Cada 30 días", date(2025, 10, 20))
        self.c = ControlPlaga("Cyperkill", 32000, "ICA-C-8899", "Cada 15 días", "10 días")

        self.factura.agregarProducto(self.a)
        self.factura.agregarProducto(self.f)
        self.factura.agregarProducto(self.c)

    def test_datos_basicos_factura(self):
        self.assertEqual(self.factura.fecha, date(2025, 11, 3))
        self.assertEqual(self.factura.cliente.nombre, "Laura Gómez")
        self.assertEqual(len(self.factura.productos), 3)

    def test_calcular_total(self):
        total = self.factura.calcular_total()
        self.assertEqual(total, 120000)

    def test_str_factura(self):
        s = str(self.factura)
        self.assertIn("Laura Gómez", s)
        self.assertIn("120000", s)
        self.assertIn("AgroVida", s)


if __name__ == "__main__":
    unittest.main()
