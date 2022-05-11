from fachada import BancoFacade

if __name__ == "__main__":
    cuenta = BancoFacade(666554433,8888)
    
    retiro = cuenta.retirar_dinero(100.0)
    retiro1 = cuenta.retirar_dinero(900.0)
    retiro2 = cuenta.retirar_dinero(900.0)
    deposito = cuenta.depositar_dinero(200)
    print(retiro)
    print(retiro1) 
    print(retiro2)
    print(deposito)
    
