from usuario.select import buscar_usuarios, buscar_usuario_id
from usuario.insert import inserir_usuario
from usuario.update import atualizar_usuario
from usuario.deletar import excluir_usuario

def menu_usuario(session):
    execucao = True

    while execucao:

        print('''
Opções:
[1] Buscar todos os usuarios
[2] Buscar um usuario por id
[3] Cadastrar um novo usuario
[4] Atualizar informações de um usuario
[5] Excluir um usuario
[0] Voltar
        ''')

        opcao = input(str("Escolha uma opção: "))

        match int(opcao):
            case 1:
                buscar_usuarios(session)
            case 2:
                buscar_usuario_id(session)
            case 3:
                inserir_usuario(session)
            case 4:
                atualizar_usuario(session)
            case 5:
                excluir_usuario(session)
            case 0:
                execucao = False
                return
            case _:
                print("Operação não entendida...")