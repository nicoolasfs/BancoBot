class Fondos:
    def __init__(self, dinero_cuenta: float):
        self.dinero_cuenta = dinero_cuenta

    def retirar_dinero(self, valor: float):
        self.dinero_cuenta -= valor

    def depositar_dinero(self, valor: float):
        self.dinero_cuenta += valor

    def dinero_suficiente(self, valor_para_retirar: float) -> float:
        if valor_para_retirar > self.dinero_cuenta:
            return False
        else:
            self.retirar_dinero(valor=valor_para_retirar)
            return True

    def hacer_deposito(self, valor_a_depositar: float):
        self.depositar_dinero(valor=valor_a_depositar)
