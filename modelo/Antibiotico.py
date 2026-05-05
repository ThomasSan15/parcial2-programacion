from .Producto import Producto

class Antibiotico(Producto):
    def __init__(self, nombre: str, valor: float, dosis: float, tipoAnimal: str):
        super().__init__(nombre, valor)
        # Validación de rango de dosis (según enunciado: entre 400 y 600)
        if not (400 <= float(dosis) <= 600):
            raise ValueError("Dosis debe estar entre 400 y 600")
        tipo = tipoAnimal.strip().capitalize()
        if tipo not in ("Bovino", "Porcino", "Caprino"):
            raise ValueError("tipoAnimal debe ser 'Bovino', 'Porcino' o 'Caprino'")
        self._dosis = float(dosis)
        self._tipoAnimal = tipo

    @property
    def dosis(self) -> float:
        return self._dosis

    @dosis.setter
    def dosis(self, v: float) -> None:
        if not (400 <= float(v) <= 600):
            raise ValueError("Dosis debe estar entre 400 y 600")
        self._dosis = float(v)

    @property
    def tipoAnimal(self) -> str:
        return self._tipoAnimal

    @tipoAnimal.setter
    def tipoAnimal(self, v: str) -> None:
        t = v.strip().capitalize()
        if t not in ("Bovino", "Porcino", "Caprino"):
            raise ValueError("tipoAnimal debe ser 'Bovino', 'Porcino' o 'Caprino'")
        self._tipoAnimal = t

    def __str__(self) -> str:
        return (f"Antibiótico: {self.nombre} (Dosis: {self.dosis} mg, "
                f"Animal: {self.tipoAnimal}) - ${self.valor:.2f}")
