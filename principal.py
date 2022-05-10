from fachada import BancoFacade

if __name__ == "__main__":
    cuenta = BancoFacade(numero_cuenta=123456, codigo_seguridad=1234)
    retiro = cuenta.retirar_dinero(100.0)
    retiro1 = cuenta.retirar_dinero(900.0)
    retiro2 = cuenta.retirar_dinero(900.0)
    deposito = cuenta.depositar_dinero(200)
    print(retiro, retiro1, retiro2, deposito)
    