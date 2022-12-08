def buscar_vendedores(session):

    vendedores = session.execute('select * from vendedores')

    if vendedores:

        print('Listagem dos vendedores...\n')

        for vendedor in vendedores:
            print('|')
            print(f'| id: {vendedor.id}')
            print(f'| nome: {vendedor.nome}')
            print(f'| email: {vendedor.email}')
            print(f'| cnpj: {vendedor.cnpj}')
            print(f'| telefone: {vendedor.telefone}')
            print('|')

    else:

        print("Nenhum vendedor encontrado...")


def buscar_vendedor_id(session):

    lista_vendedores = session.execute('select * from vendedores')

    if lista_vendedores:

        for vendedor in lista_vendedores:

            print("\nLista dos vendedores cadastrados no sistema...")
            print(f'| id: {vendedor.id}')
            print(f'| nome: {vendedor.nome}')
            print(f'| email: {vendedor.email}')

        print('\n')
        id_vendedor = input(str("Digite o id do vendedor: "))
        vendedor = session.execute(f"select * from vendedores where id = '{id_vendedor}'")

        if vendedor:

            for v in vendedor:
                print('\n')
                print(f'| id: {v.id}')
                print(f'| nome: {v.nome}')
                print(f'| email: {v.email}')
                print(f'| cnpj: {v.cnpj}')
                print(f'| telefone: {v.telefone}')
                print('\n')

        else:

            print("vendedor não encontrado...")

    else:

        print("Nenhum vendedor encontrado...")