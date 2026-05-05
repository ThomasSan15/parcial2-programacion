from modelo.Cliente import Cliente

class CRUDCliente:
    def __init__(self):
        self._clientes = []

    @property
    def clientes(self):
        return self._clientes[:]

    def CrearCliente(self, nombre: str, cedula: int):
        cliente = Cliente(nombre, cedula)
        self._clientes.append(cliente)
        return cliente

    def BuscarPorCedula(self, cedula: int):
        for cliente in self._clientes:
            if cliente.cedula == cedula:
                return cliente
        return None

    def ListarClientes(self):
        return [str(clientes) for clientes in self._clientes]

    def MostrarFacturasPorCedula(self, cedula: int):
        cliente = self.BuscarPorCedula(cedula)
        if not cliente:
            print(f"No se encontró cliente con cédula {cedula}.")
            return

        print(f"\nCliente: {cliente.nombre} ({cliente.cedula})")
        print(f"Tiene {len(cliente.pedidos)} facturas asociadas.\n")

        for facturas in cliente.pedidos:
            nombres = [p.nombre for p in facturas.productos]
            print(f"Factura del {facturas.fecha} -> Total: {facturas.total} | Productos: {nombres}")
