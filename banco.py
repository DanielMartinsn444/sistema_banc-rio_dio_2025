clientes=[]
contas= []



class Cliente:
     def __init__(self, nome, data_nascimento, cpf, endereco):
         self.nome = nome
         self.data_nascimento = data_nascimento
         self.cpf = cpf
         self.endereco = endereco

def criar_usuario(clientes_existentes):
    cpf= input("digite o cpf desejado: ")
    cpf_filtro= ''.join(filter(str.isdigit, cpf))
    cliente_existente = filtrar_usuario(cpf_filtro, clientes_existentes)
    
    if cliente_existente:
        print("\nOps!, Não foi possivel realizar o cadastro pois este CPF já está cadastrado.")
        return None
    
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    logradouro = input("Logradouro: ")
    numero_endereco = input("Número e Complemento: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado (ex: SP, MG): ")
    
    endereco_completo = f"{logradouro}, {numero_endereco} - {bairro} - {cidade}/{estado}"
    
    novo_cliente= Cliente(nome=nome, data_nascimento=data_nascimento, cpf=cpf_filtro, endereco=endereco_completo)
    
    clientes_existentes.append(novo_cliente)
    print(f"\nUsuário '{novo_cliente.nome}' Criado com sucesso!")
    return novo_cliente


def filtrar_usuario(cpf,clientes):
    for cliente_obj in clientes:
        if cliente_obj.cpf == cpf:
            return cliente_obj
    return None


class Conta:
    def __init__(self,numero,agencia,cliente, limite= 500, limite_saques=3):
        self.saldo= 0
        self.numero= numero
        self.agencia= agencia
        self.cliente= cliente
        self.historico= []
        self.limite= limite
        self.limite_saques=limite_saques
        self.numero_saque= 0
        
    def depositar(self,valor):
        if valor >0:
            self.saldo += valor
            self.historico.append (f"Depósito: R$ {valor:.2f}")
            return True
            
        else:
            print( "Valor inválido, digite o valor corretamente.")
            return False
    
    def sacar(self, valor):
        excedeu_saldo= valor > self.saldo
        excedeu_limite= valor > self.limite
        excedeu_saques= self.numero_saque >= self.limite_saques
        
        if excedeu_saldo:
            print("limite de saldo para saque excedido")
            return False
            
        
        elif excedeu_limite:
            print("limite excedido.")
            return False
            
        
        elif excedeu_saques:
            print("limite saque excedido")
            return False
           
        
        elif valor > 0:
            self.saldo -= valor
            self.historico.append(f"Saque: R$ {valor:.2f}")
            self.numero_saque += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            return True    
        else:
            print("o valor informado é inválido.")
            return False
          
    def exibir_extrato(self):
     print("\n========== Extrato ==========")
     if not self.historico:
         print('Não foram realizadas movimentações.')
     else:
         for transacao in self.historico:
            print(f"{transacao}.")
           
     print(f"Saldo: R$ {self.saldo:.2f}")
     print("\n=============================")
     
class ContaCorrente(Conta):
     def __init__(self,numero,agencia,cliente, limite= 500, limite_saques=3):
         super().__init__(numero,agencia,cliente, limite= limite, limite_saques=limite_saques)
                
def encontrar_conta_por_cpf(cpf, contas_existentes):
    for conta_obj in contas_existentes:
       
        if conta_obj.cliente.cpf == cpf:
            return conta_obj 
    return None

def obter_nome_cliente_para_despedida(cpf_digitado, clientes_existentes):
    
    cliente_encontrado = filtrar_usuario(cpf_digitado, clientes_existentes)
    if cliente_encontrado:
        return cliente_encontrado.nome 
    return "Visitante" 



menu= """
Bem vindo ao banco!        

[1] Depósito
[2] Saques
[3] Extrato
[4] Criar Usuário
[5] Sair
"""   
     
ultimo_cpf_interagido = None 

while True:
    opcao = input(menu)

    if opcao == "1": 
        cpf = input("Informe o CPF do cliente para depósito: ")
        
        cpf_limpo = ''.join(filter(str.isdigit, cpf))
        conta_alvo = encontrar_conta_por_cpf(cpf_limpo, contas) 
        
        if conta_alvo:
            try:
                valor_deposito = float(input("Digite o valor do depósito: "))
                conta_alvo.depositar(valor_deposito)
                ultimo_cpf_interagido = cpf_limpo 
            except ValueError:
                print("Operação falhou! Valor inválido. Por favor, digite um número.")
        else:
            print("Conta não encontrada para o CPF informado. Verifique o CPF ou crie um usuário/conta.")

    elif opcao == "2": 
        cpf = input("Informe o CPF desejado para saque: ")
        cpf_limpo = ''.join(filter(str.isdigit, cpf))
        conta_alvo = encontrar_conta_por_cpf(cpf_limpo, contas)
        
        if conta_alvo:
            try:
                valor_saque = float(input("Digite o valor do saque: "))
                conta_alvo.sacar(valor_saque)
                ultimo_cpf_interagido = cpf_limpo 
            except ValueError:
                print("Operação falhou! Valor inválido. Por favor, digite um número.")
        else:
            print("Conta não encontrada para o CPF informado. Verifique o CPF ou crie um usuário/conta.")
 
    elif opcao == "3":
        cpf = input("Informe o CPF do cliente para extrato: ")
        cpf_limpo = ''.join(filter(str.isdigit, cpf))
        conta_alvo = encontrar_conta_por_cpf(cpf_limpo, contas)
        
        if conta_alvo: 
            conta_alvo.exibir_extrato()
            ultimo_cpf_interagido = cpf_limpo 
        else:
            print("Conta não encontrada para o CPF informado. Verifique o CPF ou crie um usuário/conta.")
            
    elif opcao == "4": 
        
        novo_cliente = criar_usuario(clientes) 
        if novo_cliente:
           
            numero_nova_conta = len(contas) + 1 
            
            
            nova_conta = ContaCorrente(numero=numero_nova_conta, agencia="0001", cliente=novo_cliente)
            contas.append(nova_conta)
            print(f"Conta Corrente {nova_conta.numero} criada para {novo_cliente.nome}.")
            ultimo_cpf_interagido = novo_cliente.cpf 
           
    elif opcao == "5": 
        cpf = input("Informe o CPF do cliente para criar uma nova conta: ")
        cpf_limpo = ''.join(filter(str.isdigit, cpf))
        cliente_para_conta = filtrar_usuario(cpf_limpo, clientes)
        
        if cliente_para_conta:
           
            conta_existente = encontrar_conta_por_cpf(cpf_limpo, contas) 
            if conta_existente:
                print(f"Ops! Cliente '{cliente_para_conta.nome}' já possui uma conta (Número: {conta_existente.numero}).")
            else:
                numero_nova_conta = len(contas) + 1
               
                nova_conta = ContaCorrente(numero=numero_nova_conta, agencia="0001", cliente=cliente_para_conta)
                contas.append(nova_conta)
                print(f"Conta Bancária {nova_conta.numero} criada para {cliente_para_conta.nome}.")
                ultimo_cpf_interagido = cpf_limpo 
        else:
            print("Cliente não encontrado. Crie um cadastro primeiro (opção 4).")
            
    elif opcao == "6": 
        nome_para_despedida = obter_nome_cliente_para_despedida(ultimo_cpf_interagido, clientes)
        print(f"Até logo, {nome_para_despedida}! Agradecemos por usar nosso sistema bancário. Saindo...")
        break
        
    else:
        print("Operação inválida! Por favor, selecione uma opção válida.")