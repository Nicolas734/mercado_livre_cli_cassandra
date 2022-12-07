from produto.insert import inserir_produto
from produto.select import buscar_produtos
from produto.update import atualizar_produto
from produto.deletar import excluir_produto

def menu_produto(session):
    execucao = True

    while execucao:

        print('''
Opções:
[1] Buscar todos os produtos
[2] Buscar um produto por id
[3] Cadastrar um novo produto
[4] Atualizar informações de um produto
[5] Excluir um produto
[0] Voltar
        ''')

        opcao = input(str("Escolha uma opção: "))

        match int(opcao):
            case 1:
                buscar_produtos(session)
            case 2:
                print("Não criado...")
            case 3:
                inserir_produto(session)
            case 4:
                atualizar_produto(session)
            case 5:
                excluir_produto(session)
            case 0:
                execucao = False
                return
            case _:
                print("Operação não entendida...")