class CodigoSeguridad:
    def __init__(self, codigo: int):
        self.codigo = codigo

    def validar_codigo_seguridad(self, codigo: int):
        resultado = False
        if codigo == self.codigo:
            resultado = True

        return resultado
