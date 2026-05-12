from modelo.Fertilizante import Fertilizante
from modelo.ControlPlaga import ControlPlaga
from modelo.Antibiotico import Antibiotico
from datetime import date


class CrudProducto:
    def __init__(self):
        # Lista interna de productos registrados
        self._productos = []

    @property
    def productos(self):
        # Retorna una copia para evitar modificaciones externas
        return self._productos[:]

    def crear_fertilizante(
        self,
        nombre: str,
        valor: float,
        registro: str,
        frecuencia: str,
        fecha_aplicacion: date
    ):
        fertilizante = Fertilizante(
            nombre,
            valor,
            registro,
            frecuencia,
            fecha_aplicacion
        )
        self._productos.append(fertilizante)
        return fertilizante

    def crear_control_plaga(
        self,
        nombre: str,
        valor: float,
        registro: str,
        frecuencia: str,
        periodo_carencia: str
    ):
        control_plaga = ControlPlaga(
            nombre,
            valor,
            registro,
            frecuencia,
            periodo_carencia
        )
        self._productos.append(control_plaga)
        return control_plaga

    def crear_antibiotico(
        self,
        nombre: str,
        valor: float,
        dosis: float,
        tipo_animal: str
    ):
        antibiotico = Antibiotico(nombre, valor, dosis, tipo_animal)
        self._productos.append(antibiotico)
        return antibiotico

    def listar_productos(self):
        if not self._productos:
            print("No hay productos de control registrados aún.")
            return

        return self._productos[:]
