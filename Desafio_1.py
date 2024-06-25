menu = """ 

    Banco Fulaninho

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input (menu)
    
    if opcao == "d":
        
        saldo_add = float(input("Deseja depositar quanto? "))
        saldo += saldo_add
        print(f"Saldo atualizado... voce tem agora ${saldo:.2f}")
        extrato += f"Deposito: ${saldo:.2f}\n"
        
    elif opcao == "s":
                
        retirada = float(input("Quanto deseja sacar? "))
        
        excedeu_saldo = saldo > saldo
        excedeu_limite = retirada > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if limite >= retirada:

            if excedeu_saldo:
                print("Saldo insuficiente")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
                
            elif saldo > 0:
                saldo -= retirada
                extrato += f"Saque: ${retirada:.2f}\n"
                numero_saques += 1
                print(f"Saldo atualizado é de: ${saldo:.2f}")
        else:
            print("Valor de saque superior ao permitido... Operação suspensa")
            
    elif opcao == "e":
        
        print("\n============Extrato============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: ${saldo:.2f}")
        print("================================")
        
    elif opcao == "q":
        break
    
    else:
        print("Operaçao Invalida, selecione novamente a operação desejada.")