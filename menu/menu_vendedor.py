from vendedor.select import buscar_vendedores
from vendedor.insert import insert_vendedor
from vendedor.update import atualizar_vendedor
from vendedor.deletar import excluir_vendedor

def menu_vendedor(session):
    execucao =True

    while execucao:

        print('''
Opções:
[1] Buscar todos os vendedores
[2] Buscar um vendedor por id
[3] Cadastrar um novo vendedor
[4] Atualizar informações de um vendedor
[5] Excluir um vendedor
[0] Voltar
        ''')

        opcao = input(str("Escolha uma opção: "))

        match int(opcao):
            case 1:
                buscar_vendedores(session)
            case 2:
                print("Não criado...")
            case 3:
                insert_vendedor(session)
            case 4:
                atualizar_vendedor(session)
            case 5:
                excluir_vendedor(session)
            case 0:
                execucao = False
                return
            case _:
                print("Operação não entendida...")