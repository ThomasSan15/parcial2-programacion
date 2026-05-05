# ui/Menu.py
from CRUD.CRUDCliente import CRUDCliente
from CRUD.CRUDProducto import CRUDProducto
from CRUD.CRUDFactura import CRUDFactura
from datetime import date

class Menu:
    def __init__(self):
        self._clientes = CRUDCliente()
        self._productos = CRUDProducto()
        self._facturas = CRUDFactura()

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
            c = self._clientes.CrearCliente(nombre, int(cedula))
            print("Cliente creado:", c)
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
            animal = input("Tipo de animal (Bovino/Porcino/Caprino): ").strip()
            try:
                p = self._productos.CrearAntibiotico(nombre, valor, dosis, animal)
                print("Antibiótico creado:", p)
            except Exception as e:
                print("Error:", e)
        elif tipo == "2":
            registro = input("Registro ICA: ").strip()
            frecuencia = input("Frecuencia de aplicación: ").strip()
            fecha_txt = input("Fecha última aplicación (YYYY-MM-DD): ").strip()
            from datetime import datetime
            try:
                fecha = datetime.strptime(fecha_txt, "%Y-%m-%d").date()
                p = self._productos.CrearFertilizante(nombre, valor, registro, frecuencia, fecha)
                print("Fertilizante creado:", p)
            except Exception as e:
                print("Error:", e)
        elif tipo == "3":
            registro = input("Registro ICA: ").strip()
            frecuencia = input("Frecuencia de aplicación: ").strip()
            periodo = input("Periodo de carencia: ").strip()
            try:
                p = self._productos.CrearControlPlaga(nombre, valor, registro, frecuencia, periodo)
                print("Control de plagas creado:", p)
            except Exception as e:
                print("Error:", e)
        else:
            print("Tipo no válido.")

    def _op_crear_factura(self):
        cedula = input("Cédula del cliente: ").strip()
        cliente = self._clientes.BuscarPorCedula(int(cedula))
        if cliente is None:
            print("Cliente no encontrado.")
            return
        print("Seleccione productos por número (separados por coma):")
        prods = self._productos.ListarProductos()
        if not prods:
            print("No hay productos registrados.")
            return
        for i, p in enumerate(prods, start=1):
            print(f"{i}. {p}")
        indices_txt = input("Indices: ").strip()
        try:
            indices = [int(x)-1 for x in indices_txt.split(",") if x.strip()]
            seleccion = [prods[i] for i in indices]
            factura = self._facturas.CrearFactura(cliente, seleccion, date.today())
            print("Factura creada:", factura)
        except Exception as e:
            print("Error al crear factura:", e)

    def _op_buscar_por_cedula(self):
        cedula = input("Cédula: ").strip()
        cliente = self._clientes.BuscarPorCedula(int(cedula))
        if cliente is None:
            print("Cliente no encontrado.")
            return
        print(f"\nCliente: {cliente.nombre} ({cliente.cedula})")
        self._clientes.MostrarFacturasPorCedula(cliente.cedula)

    def _op_listar_productos(self):
        prods = self._productos.ListarProductos()
        if not prods:
            print("No hay productos.")
            return
        print("\nProductos registrados:")
        for p in prods:
            print(" -", p)

    def _op_listar_clientes(self):
        cl = self._clientes.ListarClientes()
        if not cl:
            print("No hay clientes.")
            return
        print("\nClientes registrados:")
        for c in cl:
            print(" -", c)
