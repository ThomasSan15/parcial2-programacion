from .ProductoControl import ProductoControl
from datetime import date

class Fertilizante(ProductoControl):
    def __init__(self, nombre: str, valor: float, registroICA: str, frecuenciaAplicacion: str, fechaUltimaAplicacion: date):
        super().__init__(nombre, valor, registroICA, frecuenciaAplicacion)
        if not isinstance(fechaUltimaAplicacion, date):
            raise TypeError("fechaUltimaAplicacion debe ser datetime.date")
        self._fechaUltimaAplicacion = fechaUltimaAplicacion

    @property
    def fechaUltimaAplicacion(self) -> date:
        return self._fechaUltimaAplicacion

    @fechaUltimaAplicacion.setter
    def fechaUltimaAplicacion(self, v: date) -> None:
        self._fechaUltimaAplicacion = v

    def __str__(self) -> str:
        return (f"Fertilizante: {self.nombre} (Última aplicación: {self._fechaUltimaAplicacion}, "
                f"Frecuencia: {self.frecuenciaAplicacion}) - ${self.valor:.2f}")
