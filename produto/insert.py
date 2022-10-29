from datetime import date
import uuid

def inserir_produto(session):
    dataAtual = date.today()
    produtos = []
    execucao = True
    while execucao:

        nome = input(str("Digite o nome do produto: "))
        descricao = input(str("Digite a descrição do produto: "))
        preco = input(str("Digite o preço do produto: "))
        quantidade = input(str("Digite a quantidade de produto em estoque: "))
        data_postagem = dataAtual.strftime('%d/%m/%Y')

        produto = {'nome':nome, 'descricao':descricao, 'preco':preco, 'quantidade':quantidade, 'data_postagem':data_postagem }
        produtos.append(produto)

        opcao = input(str("Deseja cadastrar outro produto ? [SIM/NAO] "))

        if opcao.upper() != "SIM":
            execucao = False

    for produto in produtos:
        session.execute("""
                insert into produtos
                    (id, nome, descricao, preco, quantidade, data_postagem )
                values
                    (%s,%s,%s,%s,%s,%s)
        """,
        (str(uuid.uuid1()),nome, descricao, preco, quantidade, data_postagem)

        )
