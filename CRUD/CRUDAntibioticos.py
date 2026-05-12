from modelo.Antibiotico import Antibiotico


class CrudAntibiotico:
    def __init__(self):
        # Lista interna de antibióticos
        self._antibioticos = []

    @property
    def antibioticos(self):
        return self._antibioticos[:]

    def crear_antibiotico(
        self,
        nombre: str,
        valor: float,
        dosis: float,
        tipo_animal: str
    ):
        antibiotico = Antibiotico(
            nombre,
            valor,
            dosis,
            tipo_animal
        )

        self._antibioticos.append(
            antibiotico
        )

        return antibiotico

    def listar_antibioticos(self):
        if not self._antibioticos:
            print(
                "No hay antibióticos "
                "registrados aún."
            )
            return

        return self._antibioticos[:]
