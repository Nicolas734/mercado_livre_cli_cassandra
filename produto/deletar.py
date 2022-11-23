from produto.select import buscar_produtos

def excluir_produto(session):
    buscar_produtos(session)

    produto_id = input(str('Digite o id do produto que deseja excluir: '))

    session.execute(f"delete from produtos where id='{produto_id}'")
    print(f'\nproduto de id {produto_id} excluido com sucesso...\n')