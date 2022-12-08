import json

def buscar_produtos(session):

    produtos = session.execute("select * from produtos")

    if produtos:

        print("Listagem dos produtos...\n")

        for produto in produtos:
            vendedor = json.loads(produto.vendedor.replace("\'", "\""))
            print("|")
            print(f'| id: {produto.id}')
            print(f'| Nome: {produto.nome}')
            print(f'| Descricao: {produto.descricao}')
            print(f'| Preço: {produto.preco}')
            print(f'| Quantidade de produtos em estoque: {produto.quantidade}')
            print(f'| Data de postagem do produto: {produto.data_postagem}')
            print("| Informações do vendedor: {nome}, email: {email}, cnpj: {cnpj}".format(
                nome = vendedor['nome'], email = vendedor['email'], cnpj = vendedor['cnpj']
            ))

    else:

        print("Nenhum produto encontrado...")


def buscar_produto_id(session):

    lista_produtos = session.execute("select * from produtos")

    if lista_produtos:

        for produto in lista_produtos:

            print("\nListagem dos produtos cadastrados no sistema...\n")
            print(f'| id: {produto.id}')
            print(f'| Nome: {produto.nome}')
            print(f'| Preço: {produto.preco}')

        print('\n')
        id_produto = input(str("Digite o id do produto: "))
        produto = session.execute(f"select * from produtos where id = '{id_produto}'")

        if produto:

            for p in produto:
                vendedor = json.loads(p.vendedor.replace("\'", "\""))
                print('\n')
                print(f'| id: {p.id}')
                print(f'| Nome: {p.nome}')
                print(f'| Descricao: {p.descricao}')
                print(f'| Preço: {p.preco}')
                print(f'| Quantidade de produtos em estoque: {p.quantidade}')
                print(f'| Data de postagem do produto: {p.data_postagem}')
                print("| Informações do vendedor: {nome}, email: {email}, cnpj: {cnpj}".format(
                    nome = vendedor['nome'], email = vendedor['email'], cnpj = vendedor['cnpj']
                ))
                print('\n')

        else:

            print("Produto não encontrado...")

    else:
        print("Nenhum produto encontrado...")