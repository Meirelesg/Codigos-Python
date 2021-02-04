while True:
    login = input("Informe o seu usuário: ")
    senha = input("Informe a sua senha: ")

    if login != senha:
        while True:
            login2 = input("Informe o seu usuário 2.0: ")
            senha2 = input("Informe a sua senha 2.0: ")

            if login2 != login and login2 != senha2: 
                break
            else:
                print("Login e Senha iguais ou o login é o mesmo da 1º pessoa")
        break
        
    else:
        print("Você informou valores iguais no Usuário e Senha!\n\n")
        
