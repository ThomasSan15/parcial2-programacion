from modelo.Fertilizante import Fertilizante
from modelo.ControlPlaga import ControlPlaga
from modelo.Antibiotico import Antibiotico
from datetime import date

class CRUDProducto:
    def __init__(self):
        self._productos = []

    @property
    def productos(self):
        return self._productos[:]

    def CrearFertilizante(self, nombre: str, valor: float, registro: str, frecuencia: str, fechaAplicacion: date):
        fertilizante = Fertilizante(nombre, valor, registro, frecuencia, fechaAplicacion)
        self._productos.append(fertilizante)
        return fertilizante

    def CrearControlPlaga(self, nombre: str, valor: float, registro: str, frecuencia: str, periodoCarencia: str):
        controlPlaga = ControlPlaga(nombre, valor, registro, frecuencia, periodoCarencia)
        self._productos.append(controlPlaga)
        return controlPlaga
    
    def CrearAntibiotico(self, nombre: str, valor: float, dosis: float, tipoAnimal: str):
        antibiotico = Antibiotico(nombre, valor, dosis, tipoAnimal)
        self._productos.append(antibiotico)
        return antibiotico
    
    def ListarProductos(self):
        if not self._productos:
            print("No hay productos de control registrados aún.")
            return 
        return self._productos[:]
