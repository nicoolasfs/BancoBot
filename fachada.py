from numero_cuenta import NumeroCuenta
from codigo_seguridad import CodigoSeguridad
from fondos import Fondos


class BancoFacade:
    def __init__(self, numero_cuenta: int, codigo_seguridad: int):
        self.numero_cuenta = numero_cuenta
        self.codigo_seguridad = codigo_seguridad
        self.check_numero_cuenta = NumeroCuenta()
        self.check_codigo_seguridad = CodigoSeguridad()
        self.check_fondos = Fondos()

    def retirar_dinero(self, valor: float):
        if (
            self.check_numero_cuenta.validar_numero_cuenta(self.numero_cuenta)
            and self.check_codigo_seguridad.validar_codigo_seguridad(
                self.codigo_seguridad
            )
            and self.check_fondos.dinero_suficiente(valor)
        ):
            return (f"Transacción exitosa \n Retiro exitoso. \n Nuevo saldo: {self.check_fondos.dinero_cuenta}")
        else:
            return (f"Transacción fallida \n Error: No tiene dinero suficiente \n Saldo actual: {self.check_fondos.dinero_cuenta}")

    def depositar_dinero(self, valor: float):
        if self.check_numero_cuenta.validar_numero_cuenta(
            self.numero_cuenta
        ) and self.check_codigo_seguridad.validar_codigo_seguridad(
            self.codigo_seguridad
        ):
            self.check_fondos.hacer_deposito(valor)
            return (f"Transacción exitosa \n Deposito exitoso. Nuevo saldo: {self.check_fondos.dinero_cuenta}")
        else:
            return "Transacción fallida"
