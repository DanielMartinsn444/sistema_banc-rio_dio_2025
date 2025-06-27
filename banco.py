saldo= 0
extrato= ""
limite= 500
saque_diario= 0
LIMITE_SAQUE= 3
usuarios=[]



menu= """
Bem vindo ao banco!        

[1] Depósito
[2] Saques
[3] Extrato
[4] Criar Usuário
[5] Sair
"""
def filtrar_usuario(cpf,usuarios):
    for user in usuarios:
        if user.get("cpf") == cpf:
            return user
    return None

def criar_usuario(usuarios):
    cpf= input("digite o cpf desejado: ")
    cpf_filtro= cpf.replace(".-", '')
    usuario= input("Digite seu nome: ")
    data_nascimento= input("Data de nascimento: ")
    logradouro= input("Logradouro: ")
    endereco= input("Endereco: ")
    bairro=input("Bairro: ")
    cidade= input("Cidade: ")
    estado= input("Estado:   (ex: SP, MG...)")
    endereco_completo= f"{logradouro} - {endereco} - {cidade} - {bairro} - {estado}"
    chave_usuario= filtrar_usuario(cpf, usuarios)
    if chave_usuario == None:
        novo_usuario= {
            "nome":usuario,
            "cpf": cpf_filtro,
            "data_nascimento": data_nascimento,
            "endereco": endereco_completo
        }
        usuarios.append(novo_usuario)
        return usuarios
    else:
        print("não foi possivel realizar o cadastro: Dados Inconsistentes. ")
    return usuarios
   

def depositar(saldo,valor,extrato, /):
        if valor >0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            return saldo, extrato
        else:
            print( "Valor inválido, digite o valor corretamente.")
            return saldo, extrato
        
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
        excedeu_saldo= valor > saldo
        excedeu_limite= valor > limite
        excedeu_saques= numero_saques >= limite_saques
        
        if excedeu_saldo:
            print("limite de saldo para saque excedido")
            return saldo, extrato, numero_saques
        
        elif excedeu_limite:
            print("limite excedido.")
            return saldo, extrato, numero_saques
        
        elif excedeu_saques:
            print("limite saque excedido")
            return saldo,extrato, numero_saques
        
        elif valor > 0:
            saldo -= valor
            extrato +=  f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            return saldo, extrato, numero_saques
            
        else:
            print("o valor informado é inválido.")
            return saldo, extrato, numero_saques
        
        
def exibir_extrato(saldo,extrato):
     print("\n========== Extrato ==========")
     print("Não foram realizadas movimentações." if not extrato else extrato)
     print(f"\nSaldo: R$ {saldo:.2f}")
     print("\n=============================")
                
        
while True:
    opcao= input(menu)
    if opcao == "1":
        valor_deposito= float(input("Digite o valor do deposito: "))
        saldo, extrato = depositar(saldo, valor_deposito, extrato)
    elif opcao == "2":
        valor_saque= float(input("Digite o valor do saque: "))
        saldo, extrato, saque_diario = sacar(saldo=saldo, valor=valor_saque, extrato=extrato, limite=limite, numero_saques=saque_diario, limite_saques=LIMITE_SAQUE)
    elif opcao== "3":
        exibir_extrato(saldo,extrato)
        
    elif opcao == "4": 
        usuarios= criar_usuario(usuarios)
           
    elif opcao == "5":
        print("Saindo...")
        break     
    else:
        print("Operação inválida! Selecione novamente a operação desejada.")
        

