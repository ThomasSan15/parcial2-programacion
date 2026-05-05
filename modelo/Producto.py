class Producto:
    def __init__(self, nombre: str, valor: float):
        self._nombre = nombre
        self._valor = float(valor)

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

    def __str__(self) -> str:
        return f"{self._nombre} - ${self._valor:.2f}"
