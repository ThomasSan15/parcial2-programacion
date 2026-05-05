from .Producto import Producto

class ProductoControl(Producto):
    def __init__(self, nombre: str, valor: float, registroICA: str, frecuenciaAplicacion: str):
        super().__init__(nombre, valor)
        self._registroICA = registroICA
        self._frecuenciaAplicacion = frecuenciaAplicacion

    @property
    def registroICA(self) -> str:
        return self._registroICA

    @registroICA.setter
    def registroICA(self, v: str) -> None:
        self._registroICA = v

    @property
    def frecuenciaAplicacion(self) -> str:
        return self._frecuenciaAplicacion

    @frecuenciaAplicacion.setter
    def frecuenciaAplicacion(self, v: str) -> None:
        self._frecuenciaAplicacion = v

    def __str__(self) -> str:
        return (f"{self.nombre} (ICA: {self._registroICA}, "
                f"Frecuencia: {self._frecuenciaAplicacion}) - ${self.valor:.2f}")
