class Producto:
    def __init__(
        self,
        nombre: str,
        valor: float,
        registro_ica: str,
        frecuencia_aplicacion: str
    ):
        self._nombre = nombre
        self._valor = float(valor)
        self._registro_ica = registro_ica
        self._frecuencia_aplicacion = frecuencia_aplicacion

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, v: str) -> None:
        self._nombre = v

    @property
    def valor(self) -> float:
        return self._valor

    @valor.setter
    def valor(self, v: float) -> None:
        self._valor = float(v)

    @property
    def registro_ica(self) -> str:
        return self._registro_ica

    @registro_ica.setter
    def registro_ica(self, v: str) -> None:
        self._registro_ica = v

    @property
    def frecuencia_aplicacion(self) -> str:
        return self._frecuencia_aplicacion

    @frecuencia_aplicacion.setter
    def frecuencia_aplicacion(self, v: str) -> None:
        self._frecuencia_aplicacion = v

    def __str__(self) -> str:
        return (
            f"{self.nombre} "
            f"(ICA: {self.registro_ica}, "
            f"Frecuencia: {self.frecuencia_aplicacion}) "
            f"- ${self.valor:.2f}"
        )
