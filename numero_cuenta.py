class NumeroCuenta:
    def __init__(self):
        self.numero_cuenta = 123456

    def validar_numero_cuenta(self, numero: int):
        resultado = False
        if numero == self.numero_cuenta:
            resultado = True

        return resultado
