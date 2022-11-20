contatos = [["-- Contatos --"]]
keys = ["Nome:","Telefone:","Cidade:","Estado:","Status:"]

def incluir(): #menu - opção 1
    nome = str(input("Digite o nome: "))
    tel = str(input("Digite o telefone: "))
    cidade = str(input("Digite a cidade: "))
    estado = str(input("Digite o estado: "))
    status = str(input('Status - Digite "P" p/ Pessoal ou "C" p/ Comercial: '))
    contatos.append([nome,tel,cidade,estado,status])
    print(f"\nCadastro do(a) {nome} efetuado com sucesso!")

def alterar(): #menu - opção 2
    nome_altera = input("Digite o nome que deseja alterar: ")
    for i in range (len(contatos)):
        for j in range (i):
            if nome_altera in contatos[i][j]:
                print(f"\n{nome_altera} encontrado(a) na posição/índice {i},{j}.")
                nome_altera = input("\nDigite o novo nome: ")
                telefone_altera = input(str("Digite o novo telefone: "))
                cidade_altera = input(str("Digite a nova cidade: "))
                estado_altera = input(str("Digite o novo estado: "))
                status_altera = input(str("Digite o novo status\n'P' -> Pessoal | 'C' -> Comercial: "))
                confirma = input(f"\nConfirma alteração de {nome_altera}? S - Sim, N - Não: ")
                if confirma == "S" or confirma == "s":
                    contatos[i] = nome_altera, telefone_altera, cidade_altera, estado_altera, status_altera
                    print(f"\nRegistro alterado com sucesso!")
                    break
                else:
                    print("\nAlteração cancelada!")
            break
        else:
            print(f'\n{nome_altera} não foi encontrado!')

def listar(): #menu - opção 3
    print("\n3.AGENDA COMPLETA")
    for cadastros in contatos:
        print("- *** -")
        for i in cadastros:
            print(i)

def procurar(): #menu - opção 4
    nome_busca = str(input("Digite o nome: "))
    for i in range (len(contatos)):
        for j in range (i):
            if nome_busca in contatos[i][j]:
                print(f"\n{nome_busca} encontrado(a) na posição/índice {i},{j}.")
                break
            else:
                print(f"\n{nome_busca} não encontrado!")

def excluir(): #menu - opção 5
    nome_exclui = input("Digite o nome que deseja exluir: ")
    for i in range (len(contatos)):
        for j in range (i):
            if nome_exclui in contatos[i][j]:
                print(f"\n{nome_exclui} encontrado(a) na posição/índice {i},{j}.")
                confirma = input(f"Confirma exclusão de {nome_exclui}? S - Sim, N - Não: ")
                if confirma == "S" or confirma == "s":
                    contatos.pop(i)
                    print(f"\nRegistro de {nome_exclui} excluído com sucesso!")
                    menu()
                else:
                    print("\nOperação cancelada!")
                    menu()
            else:
                print(f"\n{nome_exclui} não foi encontrado!")
                menu()

def menu():
    Tela = """
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
            incluir()
            menu()
            opc = str(input("-> ESCOLHA A OPÇÃO: "))

        elif opc == "2":
            alterar()
            menu()
            opc = str(input("-> ESCOLHA A OPÇÃO: "))

        elif opc == "3":
            listar()
            menu()
            opc = str(input("-> ESCOLHA A OPÇÃO: "))

        elif opc == "4":
            print("\n4.PROCURAR")
            procurar()
            print()
            menu()         
            opc = str(input("-> ESCOLHA A OPÇÃO: "))

        elif opc == "5":
            print("\n5.EXCLUSÃO DE REGISTRO")
            print()
            excluir()
            print()
            opc = str(input("-> ESCOLHA A OPÇÃO: "))

        elif opc == "6":
            print("\nObrigado por utilizar o sistema.\n\nAté breve!\n")
            break
        else:
            print("\nDigite uma opção válida\n")
            menu()
            opc = str(input("-> ESCOLHA A OPÇÃO: "))