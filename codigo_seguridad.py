class CodigoSeguridad:
    def __init__(self):
        self.codigo = 1234

    def validar_codigo_seguridad(self, codigo: int):
        resultado = False
        if codigo == self.codigo:
            resultado = True

        return resultado
