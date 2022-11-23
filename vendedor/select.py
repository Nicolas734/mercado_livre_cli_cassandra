def buscar_vendedores(session):

    print('Listagem dos vendedores...\n')

    for usuario in session.execute('select * from vendedores'):
        print('|')
        print(f'| id: {usuario.id}')
        print(f'| nome: {usuario.nome}')
        print(f'| email: {usuario.email}')
        print(f'| cnpj: {usuario.cnpj}')
        print(f'| telefone: {usuario.telefone}')
        print('|')