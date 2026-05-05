import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from datetime import date
from CRUD.CRUDProducto import CRUDProducto


class TestCRUDProducto(unittest.TestCase):
    def setUp(self):
        self.crud_producto = CRUDProducto()

    def test_crear_fertilizante(self):
        f = self.crud_producto.CrearFertilizante(
            "AgroVida", 40000, "ICA-F-2024", "Cada 30 días", date(2025, 10, 25)
        )
        self.assertEqual(f.nombre, "AgroVida")
        self.assertEqual(f.valor, 40000)
        self.assertIn(f, self.crud_producto.productos)

    def test_crear_control_plaga(self):
        c = self.crud_producto.CrearControlPlaga(
            "Cyperkill", 32000, "ICA-C-8899", "Cada 15 días", "10 días"
        )
        self.assertEqual(c.nombre, "Cyperkill")
        self.assertEqual(c.periodoCarencia, "10 días")
        self.assertIn(c, self.crud_producto.productos)

    def test_listar_productos(self):
        self.crud_producto.CrearFertilizante("FertiMax", 45000, "ICA-F-3030", "Cada 20 días", date(2025, 10, 30))
        self.crud_producto.CrearControlPlaga("BioKill", 35000, "ICA-C-9999", "Cada 15 días", "7 días")
        productos = self.crud_producto.productos
        self.assertEqual(len(productos), 2)
        self.assertEqual(productos[0].nombre, "FertiMax")
        self.assertEqual(productos[1].nombre, "BioKill")

if __name__ == "__main__":
    unittest.main()
