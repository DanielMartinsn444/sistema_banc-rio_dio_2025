saldo= 0
extrato= ""
limite= 500
saque_diario= 0
LIMITE_SAQUE= 3

menu= """
Bem vindo ao banco!        

[1] Depósito
[2] Saques
[3] Extrato
[4] Sair
"""

while True:
    opcao= input(menu)
    if opcao == "1":
        valor=float(input("Digite o valor do depósito: "))
        if valor >0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido, digite o valor corretamente.")
    elif opcao == "2":
        valor= float(input("Digite o valor do saque: "))
        
        excedeu_saldo= valor > saldo
        excedeu_limite= valor > limite
        excedeu_saques= saque_diario >= LIMITE_SAQUE
        
        if excedeu_saldo:
            print("Erro! não há saldo suficiente.")
        
        elif excedeu_limite:
            print("Erro! o valor do saque excede o limite.")
        
        elif excedeu_saques:
            print("Erro! numero máximo de saques diários atingido.")
        
        elif valor > 0:
            saldo -= valor
            extrato +=  f"Saque: R$ {valor:.2f}\n"
            saque_diario += 1
            
        else:
            print("o valor informado é inválido.")
            
    elif opcao== "3":
        print("\n========== Extrato ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n=============================")
        
    elif opcao == "4":
        break
    else:
        print("Operação inválida! Selecione novamente a operação desejada.")
        