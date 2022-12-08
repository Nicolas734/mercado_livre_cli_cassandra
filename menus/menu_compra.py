from compra.select import buscar_compras, buscar_compra_id
from compra.insert import inserir_compra
from compra.deletar import excluir_compra

def menu_compra(session):
    execucao = True

    while execucao:

        print('''
Opções:
[1] Buscar todas as compras
[2] Buscar uma compra por id
[3] Cadastrar uma nova compra
[4] Atualizar informações de uma compra
[5] Excluir uma compra
[0] Voltar
        ''')

        opcao = input(str("Escolha uma opção: "))

        match int(opcao):
            case 1:
                buscar_compras(session)
            case 2:
                buscar_compra_id(session)
            case 3:
                inserir_compra(session)
            case 4:
                print("Não criado...")
            case 5:
                excluir_compra(session)
            case 0:
                execucao = False
                return
            case _:
                print("Operação não entendida...")