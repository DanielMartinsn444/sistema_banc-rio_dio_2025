import json
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

def salvar_dados(clientes, contas, nome_arquivo_clientes='clientes.json', nome_arquivo_contas='contas.json'):
   
    clientes_para_json = [] 
    for cliente_obj in clientes: 
        dados_cliente = { 
            'nome': cliente_obj.nome,
            'cpf': cliente_obj.cpf,
            'endereco': cliente_obj.endereco,
            'data_nascimento': cliente_obj.data_nascimento,
        }
        clientes_para_json.append(dados_cliente) 
    
    
    try:
        with open(nome_arquivo_clientes, 'w', encoding='utf-8') as f_clientes:
            json.dump(clientes_para_json, f_clientes, indent=4) 
        print(f"Dados de clientes salvos em '{nome_arquivo_clientes}'")
    except Exception as e:
        print(f"Erro ao tentar salvar clientes: {e}")

    
    contas_para_json = [] 
    for conta_obj in contas:
        dados_conta = { 
            'numero': conta_obj.numero,
            'agencia': conta_obj.agencia,
            'cpf_cliente': conta_obj.cliente.cpf,
            'saldo': conta_obj.saldo,
            'historico': conta_obj.historico,
            'limite': conta_obj.limite,
            'limite_saques': conta_obj.limite_saques, 
            'numero_saque': conta_obj.numero_saque,   
        }
        contas_para_json.append(dados_conta) 

    
    try:
        with open(nome_arquivo_contas, 'w', encoding='utf-8') as f_contas:
            json.dump(contas_para_json, f_contas, indent=4)
        print(f"Dados de contas salvos em '{nome_arquivo_contas}'")
    except Exception as e:
        print(f"Erro ao tentar salvar contas: {e}")


def carregar_dados(nome_arquivo_clientes='clientes.json', nome_arquivo_contas='contas.json'):
    clientes_carregados=[]
    try:
        with open(nome_arquivo_clientes, 'r', encoding='utf-8') as f_clientes:
            dados_json_cliente= json.load(f_clientes)
            for dados_do_cliente_dict in dados_json_cliente:
                novo_cliente= Cliente(
                    nome= dados_do_cliente_dict['nome'],
                    data_nascimento=dados_do_cliente_dict['data_nascimento'],
                    cpf= dados_do_cliente_dict['cpf'],
                    endereco= dados_do_cliente_dict['endereco'],
                )
                clientes_carregados.append(novo_cliente)
    except FileNotFoundError:
        print('arquivos de clientes não encontrados, iniciando arquivos vazios...')
        return [], []
    
    contas_carregadas= []
    try:
        with open(nome_arquivo_contas, 'r', encoding='utf-8') as f_contas:
            dados_json_conta= json.load(f_contas)
            for dados_da_conta_dict in dados_json_conta:
                cliente_correspondente= filtrar_usuario(dados_da_conta_dict['cpf_cliente'], clientes_carregados)
                if cliente_correspondente:
                    nova_conta= ContaCorrente(
                    numero= dados_da_conta_dict['numero'],
                    agencia= dados_da_conta_dict['agencia'],
                    cliente= cliente_correspondente,
                    saldo=dados_da_conta_dict.get('saldo', 0.0),
                    historico= dados_da_conta_dict.get('historico', []),
                    limite=dados_da_conta_dict.get('limite',0.0),
                    limite_saques=dados_da_conta_dict.get('limite_saques', 3),
                    numero_saques=dados_da_conta_dict.get('numero_saque', 0)
                    )
                    contas_carregadas.append(nova_conta)
                else:
                    print(f"Aviso: cliente com cpf {dados_da_conta_dict['cpf_cliente']} não encontrado para a conta {dados_da_conta_dict['numero']}. Conta não será carregada.")
    except FileNotFoundError:
        print("Nenhum dado de conta salvo encontrado. \niniciando com lista vazia de contas.")
    except Exception as e:
        print(f'erro inesperado ao carregar contas: {e}')
        
    return clientes_carregados, contas_carregadas

menu= """
Bem vindo ao banco!        
[1] Depósito
[2] Saques
[3] Extrato
[4] Criar Usuário
[5] Criar Conta
[6] Sair
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
        
        salvar_dados(clientes,contas)
        break      
    else:
        print("Operação inválida! Por favor, selecione uma opção válida.")