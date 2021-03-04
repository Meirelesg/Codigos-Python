while True:

    try:
        salario = float(input("Insira o seu salário: "))
    except Exception as ta:
        print("Você não pode inserir valores STR em INT")
    else: 
        break
        
print("O seu salário é: R$", salario)
    
