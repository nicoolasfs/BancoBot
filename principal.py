from fachada import BancoFacade

class BancoBuilder:
    def __init__(self):
        self.numero_cuenta = None
        self.codigo_seguridad = None

    @staticmethod
    def crear_banco():
        return BancoBuilder()

    def set_numero_cuenta(self, numero_cuenta):
        self.numero_cuenta = numero_cuenta
        return self
    def set_codigo_seguridad(self, codigo_seguridad):
        self.codigo_seguridad = codigo_seguridad
        return self
    def build(self):
        return BancoFacade(self.numero_cuenta, self.codigo_seguridad)

