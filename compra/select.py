import json

def buscar_compras(session):

    compras = session.execute("select * from compras")

    if compras:

        print("Listagem das compras...\n")

        for compra in compras:
            cliente = json.loads(compra.cliente.replace("\'", "\""))
            produto = json.loads(compra.produto.replace("\'","\""))
            vendedor = json.loads(compra.vendedor.replace("\'","\""))
            print("|")
            print("| informações da compra")
            print(f"| id: {compra.id}")
            print("| produto:{nome}, preco: {preco}".format(
                nome = produto['nome'], preco = produto['preco']
            ))
            print(f"| data da compra: {compra.data_compra}")
            print("| Informações do vendedor: {nome}, email: {email}, cnpj: {cnpj}".format(nome = vendedor['nome'], email = vendedor['email'], cnpj = vendedor['cnpj']))
            print("| Informações do cliente: {nome}, email: {email}".format(nome = cliente['nome'], email = cliente['email']))
            print("|")

    else:

        print("Nenhuma compra encontrada...")


def buscar_compra_id(session):

    lista_compras = session.execute("select * from compras")

    if lista_compras:

        for compra in lista_compras:
            produto = json.loads(compra.produto.replace("\'","\""))

            print("\nListagem das compras registradas no sistema...\n")
            print("|")
            print(f"| id: {compra.id}")
            print("| produto:{nome}, preco: {preco}".format(
                nome = produto['nome'], preco = produto['preco']
            ))
            print(f"| data da compra: {compra.data_compra}")
            print("|")

        print('\n')
        id_compra = input(str("Digite o id da compra: "))
        compra = session.execute(f"select * from compras where id = '{id_compra}'")

        if compra: 

            for c in compra:

                cliente = json.loads(c.cliente.replace("\'", "\""))
                produto = json.loads(c.produto.replace("\'","\""))
                vendedor = json.loads(c.vendedor.replace("\'","\""))
                print('\n')
                print("| informações da compra")
                print(f"| id: {c.id}")
                print("| produto:{nome}, preco: {preco}".format(
                    nome = produto['nome'], preco = produto['preco']
                ))
                print(f"| data da compra: {c.data_compra}")
                print("| Informações do vendedor: {nome}, email: {email}, cnpj: {cnpj}".format(nome = vendedor['nome'], email = vendedor['email'], cnpj = vendedor['cnpj']))
                print("| Informações do cliente: {nome}, email: {email}".format(nome = cliente['nome'], email = cliente['email']))
                print('\n')

        else:

            print("compra não encontrada...")




    else:

        print("Nenhuma compra encontrada...")