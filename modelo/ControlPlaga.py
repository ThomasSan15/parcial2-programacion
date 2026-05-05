from .ProductoControl import ProductoControl

class ControlPlaga(ProductoControl):
    def __init__(self, nombre: str, valor: float, registroICA: str, frecuenciaAplicacion: str, periodoCarencia: str):
        super().__init__(nombre, valor, registroICA, frecuenciaAplicacion)
        self._periodoCarencia = periodoCarencia

    @property
    def periodoCarencia(self) -> str:
        return self._periodoCarencia

    @periodoCarencia.setter
    def periodoCarencia(self, v: str) -> None:
        self._periodoCarencia = v

    def __str__(self) -> str:
        return (f"Control de plagas: {self.nombre} (Carencia: {self.periodoCarencia}, "
                f"Frecuencia: {self.frecuenciaAplicacion}) - ${self.valor:.2f}")
