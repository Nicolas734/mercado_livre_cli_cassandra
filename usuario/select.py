def buscar_usuarios(session):

    usuarios = session.execute('select * from usuarios')

    if usuarios:

        print('Listagem dos usuarios...\n')

        for usuario in usuarios:
            print('|')
            print(f'| id: {usuario.id}')
            print(f'| nome: {usuario.nome}')
            print(f'| email: {usuario.email}')
            print(f'| cpf: {usuario.cpf}')
            print(f'| rg: {usuario.rg}')
            print(f'| data de nascimento: {usuario.data_nascimento}')
            print(f'| telefone: {usuario.telefone}')
            print(f'| endereco: {usuario.endereco}')
            print('|')

    else:

        print("Nenhum usuario encontrado...")


def buscar_usuario_id(session):

    lista_usuarios = session.execute('select * from usuarios')

    if lista_usuarios:

        for usuario in lista_usuarios:

            print('\nListagem dos usuarios cadastrados no sistema...\n')
            print(f'| id: {usuario.id}')
            print(f'| nome: {usuario.nome}')
            print(f'| email: {usuario.email}')

        print('\n')
        id_usuario = input(str("Digite o id do usuario: "))
        usuario = session.execute(f"select * from usuarios where id = '{id_usuario}'")

        if usuario:

            for user in usuario:
                print('\n')
                print(f'| id: {user.id}')
                print(f'| nome: {user.nome}')
                print(f'| email: {user.email}')
                print(f'| cpf: {user.cpf}')
                print(f'| rg: {user.rg}')
                print(f'| data de nascimento: {user.data_nascimento}')
                print(f'| telefone: {user.telefone}')
                print(f'| endereco: {user.endereco}')
                print('\n')
            
        else:

            print("Usuario encontrado...")

    else:

        print("Nenhum usuario encontrado...")