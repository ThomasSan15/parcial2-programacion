from modelo.Fertilizante import Fertilizante
from modelo.ControlPlaga import ControlPlaga
from datetime import date


class CrudProductoControl:
    def __init__(self):
        # Lista interna de productos de control
        self._productos_control = []

    @property
    def productos_control(self):
        return self._productos_control[:]

    def crear_fertilizante(
        self,
        nombre: str,
        valor: float,
        registro_ica: str,
        frecuencia_aplicacion: str,
        fecha_aplicacion: date
    ):
        fertilizante = Fertilizante(
            nombre,
            valor,
            registro_ica,
            frecuencia_aplicacion,
            fecha_aplicacion
        )

        self._productos_control.append(
            fertilizante
        )

        return fertilizante

    def crear_control_plaga(
        self,
        nombre: str,
        valor: float,
        registro_ica: str,
        frecuencia_aplicacion: str,
        periodo_carencia: str
    ):
        control_plaga = ControlPlaga(
            nombre,
            valor,
            registro_ica,
            frecuencia_aplicacion,
            periodo_carencia
        )

        self._productos_control.append(
            control_plaga
        )

        return control_plaga

    def listar_productos_control(self):
        if not self._productos_control:
            print(
                "No hay productos de "
                "control registrados aún."
            )
            return

        return self._productos_control[:]
