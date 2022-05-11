class NumeroCuenta:
    _cuentas = {12345678:[1234,540000.0], 
                987654321:[5678,100000.0], 
                666554433:[8888,200000.0],
                555443322:[9999,300000.0],
                444332211:[4031,400000.0],
                333221100:[1111,500000.0],
                222110000:[2222,600000.0],
                111000000:[3333,700000.0],
                121000765:[4444,800000.0]}

    def __init__(self, numero_cuenta: int):
        self.numero_cuenta = numero_cuenta

    def validar_numero_cuenta(self, numero: int):
        resultado = [False,0,0]
        if self.numero_cuenta in self._cuentas.keys():
            resultado = [True,self._cuentas[self.numero_cuenta][0],self._cuentas[self.numero_cuenta][1]]
        return resultado
    
