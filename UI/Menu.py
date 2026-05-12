# ui/Menu.py
from CRUD.CRUDCliente import CrudCliente
from CRUD.CRUDProducto import CrudProducto
from CRUD.CRUDFactura import CrudFactura
from datetime import date


class Menu:
    def __init__(self):
        self._clientes = CrudCliente()
        self._productos = CrudProducto()
        self._facturas = CrudFactura()

    def mostrar_menu(self):

        while True:
            print("\n=== SISTEMA DE FACTURACIÓN AGRÍCOLA ===")
            print("1. Registrar cliente")
            print("2. Registrar producto de control / antibiótico")
            print("3. Crear factura (vender productos)")
            print("4. Buscar cliente por cédula y mostrar facturas")
            print("5. Listar productos")
            print("6. Listar clientes")
            print("7. Salir")

            op = input("Seleccione una opción: ").strip()

            if op == "1":
                self._op_registrar_cliente()
            elif op == "2":
                self._op_registrar_producto()
            elif op == "3":
                self._op_crear_factura()
            elif op == "4":
                self._op_buscar_por_cedula()
            elif op == "5":
                self._op_listar_productos()
            elif op == "6":
                self._op_listar_clientes()
            elif op == "7":
                print("Saliendo...")
                break
            else:
                print("Opción no válida.")

    def _op_registrar_cliente(self):
        nombre = input("Nombre: ").strip()
        cedula = input("Cédula: ").strip()

        try:
            cliente = self._clientes.crear_cliente(
                nombre,
                int(cedula)
            )
            print("Cliente creado:", cliente)

        except Exception as e:
            print("Error:", e)

    def _op_registrar_producto(self):

        print("\nTipo de producto:")
        print("1. Antibiótico")
        print("2. Fertilizante")
        print("3. Control de plagas")

        tipo = input("Seleccione: ").strip()
        nombre = input("Nombre: ").strip()
        valor = float(input("Valor: ").strip())

        if tipo == "1":
            dosis = float(input("Dosis (400-600): ").strip())
            animal = input(
                "Tipo de animal (Bovino/Porcino/Caprino): "
            ).strip()

            try:
                producto = self._productos.crear_antibiotico(
                    nombre,
                    valor,
                    dosis,
                    animal
                )
                print("Antibiótico creado:", producto)

            except Exception as e:
                print("Error:", e)

        elif tipo == "2":
            registro = input("Registro ICA: ").strip()
            frecuencia = input(
                "Frecuencia de aplicación: "
            ).strip()

            fecha_txt = input(
                "Fecha última aplicación (YYYY-MM-DD): "
            ).strip()

            from datetime import datetime

            try:
                fecha = datetime.strptime(
                    fecha_txt,
                    "%Y-%m-%d"
                ).date()

                producto = self._productos.crear_fertilizante(
                    nombre,
                    valor,
                    registro,
                    frecuencia,
                    fecha
                )

                print("Fertilizante creado:", producto)

            except Exception as e:
                print("Error:", e)

        elif tipo == "3":
            registro = input("Registro ICA: ").strip()
            frecuencia = input(
                "Frecuencia de aplicación: "
            ).strip()

            periodo = input(
                "Periodo de carencia: "
            ).strip()

            try:
                producto = self._productos.crear_control_plaga(
                    nombre,
                    valor,
                    registro,
                    frecuencia,
                    periodo
                )

                print("Control de plagas creado:", producto)

            except Exception as e:
                print("Error:", e)

        else:
            print("Tipo no válido.")

    def _op_crear_factura(self):

        cedula = input("Cédula del cliente: ").strip()

        cliente = self._clientes.buscar_por_cedula(
            int(cedula)
        )

        if cliente is None:
            print("Cliente no encontrado.")
            return

        print(
            "Seleccione productos por número "
            "(separados por coma):"
        )

        productos = self._productos.listar_productos()

        if not productos:
            print("No hay productos registrados.")
            return

        for i, producto in enumerate(
            productos,
            start=1
        ):
            print(f"{i}. {producto}")

        indices_txt = input("Indices: ").strip()

        try:
            indices = [
                int(x) - 1
                for x in indices_txt.split(",")
                if x.strip()
            ]

            seleccion = [
                productos[i]
                for i in indices
            ]

            factura = self._facturas.crear_factura(
                cliente
            )

            print("Factura creada:", factura)

        except Exception as e:
            print("Error al crear factura:", e)

    def _op_buscar_por_cedula(self):

        cedula = input("Cédula: ").strip()

        cliente = self._clientes.buscar_por_cedula(
            int(cedula)
        )

        if cliente is None:
            print("Cliente no encontrado.")
            return

        print(
            f"\nCliente: "
            f"{cliente.nombre} "
            f"({cliente.cedula})"
        )

        self._clientes.mostrar_facturas_por_cedula(
            cliente.cedula
        )

    def _op_listar_productos(self):

        productos = self._productos.listar_productos()

        if not productos:
            print("No hay productos.")
            return

        print("\nProductos registrados:")

        for producto in productos:
            print(" -", producto)

    def _op_listar_clientes(self):

        clientes = self._clientes.listar_clientes()

        if not clientes:
            print("No hay clientes.")
            return

        print("\nClientes registrados:")

        for cliente in clientes:
            print(" -", cliente)
