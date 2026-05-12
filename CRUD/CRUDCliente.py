from modelo.Cliente import Cliente


class CrudCliente:
    def __init__(self):
        # Lista interna de clientes registrados
        self._clientes = []

    @property
    def clientes(self):
        # Retorna una copia para evitar modificaciones externas
        return self._clientes[:]

    def crear_cliente(self, nombre: str, cedula: int):
        cliente = Cliente(nombre, cedula)
        self._clientes.append(cliente)
        return cliente

    def buscar_por_cedula(self, cedula: int):
        for cliente in self._clientes:
            if cliente.cedula == cedula:
                return cliente
        return None

    def listar_clientes(self):
        # Retorna una lista de clientes en formato string
        return [str(cliente) for cliente in self._clientes]

    def mostrar_facturas_por_cedula(self, cedula: int):
        cliente = self.buscar_por_cedula(cedula)

        if not cliente:
            print(f"No se encontró cliente con cédula {cedula}.")
            return

        print(f"\nCliente: {cliente.nombre} ({cliente.cedula})")
        print(f"Tiene {len(cliente.pedidos)} facturas asociadas.\n")

        for factura in cliente.pedidos:
            nombres = [p.nombre for p in factura.productos]
            print(
                f"Factura del {factura.fecha} -> "
                f"Total: {factura.total} | Productos: {nombres}"
            )
