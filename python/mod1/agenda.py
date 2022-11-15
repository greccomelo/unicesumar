agenda = []

def cadastro(): #menu item 1
    nome = input(str("\nDigite o Nome: "))
    telefone = input(str("Digite o Telefone: "))
    cidade = input(str("Digite a Cidade: "))
    estado = input(str("Digite o Estado: "))
    status = input(str("Digite o Status\n'P' -> Pessoal | 'C' -> Comercial: "))
    agenda.append([nome,telefone,cidade,estado,status])

def lista(): #menu item 3
    print()
    print(agenda)

def procura(nome): #menu item 4
        ind_i = 0
        ind_j = 0
        for i in range (len(agenda)):
            for j in range (i):
                if nome in agenda[i][j]:
                    ind_i = i
                    ind_j = j
                    break
                break
        return (ind_i, ind_j)

def menu():
    Tela = """\n
    ---------------------------
    |                          |
    |   MENU PESSOA AGENDA     |
    |                          |
    |   1.Cadastrar na Agenda  |
    |   2.Alterar dados        |
    |   3.Listar Agenda        |
    |   4.Procurar na Agenda   | 
    |   5.Excluir da Agenda    |
    |                          |
    |   6.Sair do sistema      |
    |                          |
    ---------------------------
    """
    print(Tela)
    
menu()
opc = str(input("-> ESCOLHA A OPÇÃO: "))

opc1 = "0"
while opc1 != "6":
        if opc == "1":
            cadastro()
            print("\nCadastro feito com sucesso!\n")
            menu()
            opc = str(input("-> ESCOLHA A OPÇÃO: "))

        elif opc == "2":
            indice_altera = input("\nDigite o índice que deseja alterar: ")
            if (agenda.index(int(indice_altera)) in agenda):
                nome_altera = input("\nDigite o nome: ")
                telefone_altera = input(str("Digite o telefone: "))
                cidade_altera = input(str("Digite a Cidade: "))
                estado_altera = input(str("Digite o Estado: "))
                status_altera = input(str("Digite o Status\n'P' -> Pessoal | 'C' -> Comercial: "))
                agenda[int(indice_altera)] = nome_altera, telefone_altera, cidade_altera, estado_altera, status_altera
                print("\nRegistro alterado com sucesso!")
                menu()
                opc = str(input("-> ESCOLHA A OPÇÃO: "))                    
            else:
                print("\nÍndice não existe.")
                menu()
                opc = str(input("-> ESCOLHA A OPÇÃO: "))
                    
        elif opc == "3":
            lista()
            menu()
            opc = str(input("-> ESCOLHA A OPÇÃO: "))
        elif opc == "4":
            nome = input(str("\nDigite o nome que deseja procurar: "))
            achei = procura(nome)
            print()
            print("Índice",achei,"na Agenda.") # imprime índices
            print("Cadastro ->",agenda[achei[0]])
            menu()
            opc = str(input("-> ESCOLHA A OPÇÃO: "))
        elif opc == "5":
            print()
            indice = input("Digite o índice a ser excluido: ")
            agenda.pop(int(indice))
            print()
            print("\nÍndice",indice,"excluído com sucesso!")
            menu()
            opc = str(input("-> ESCOLHA A OPÇÃO: "))
        elif opc == "6":
            print("\nObrigado por utilizar o sistema.\nAté breve!\n")
            break
        else:
            print("\nDigite uma opção válida\n")
            menu()
            opc = str(input("-> ESCOLHA A OPÇÃO: "))