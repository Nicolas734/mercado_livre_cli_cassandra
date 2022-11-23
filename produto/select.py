def buscar_produtos(session):

    print("Listagem dos produtos...\n")

    for produto in session.execute("select * from produtos"):
        print("|")
        print(f'| id: {produto.id}')
        print(f'| Nome: {produto.nome}')
        print(f'| Descricao: {produto.descricao}')
        print(f'| Preço: {produto.preco}')
        print(f'| Quantidade de produtos em estoque: {produto.quantidade}')
        print(f'| Data de postagem do produto: {produto.data_postagem}')
        print("|")