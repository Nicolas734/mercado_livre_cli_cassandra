from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

from usuario.insert import inserir_usuario
from usuario.select import buscar_usuarios
from usuario.deletar import excluir_usuario

from produto.insert import inserir_produto
from produto.select import buscar_produtos
from produto.deletar import excluir_produto

from vendedor.select import buscar_vendedores
from vendedor.insert import insert_vendedor
from vendedor.deletar import excluir_vendedor

cloud_config= {
        'secure_connect_bundle': 'secure-connect-cassandra.zip'
}
auth_provider = PlainTextAuthProvider('DAZzJreSkmXuryLkOQoCAFhM', 'nbPqijNx1AZ.Mr470ZR2AoBdS,Yk6i8YEI2d8rlG,m_9L26UMPmZ4,rXRtNMKOGGe9ywN3.Uv4x8l0lURZudDiURInuZaPX3y3ZelC4xiebZY,bhpv1rhTPTwqAy7,TH')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('mercado_livre')

row = session.execute("select release_version from system.local").one()

if row:
    print("Conexão bem sucedida...")
    execucao = True
    
    while execucao:
        
        print('''
            [1] inserir usuario
            [2] buscar usuarios
            [3] excluir usuario
            [4] inserir produto
            [5] buscar produtos
            [6] excluir produto
            [7] buscar vendedores
            [8] inserir vendedore
            [9] excluir vendedor
            [0] sair
            
            ''')
        
        opcao = input(str('Escolha uma das opções a cima: '))
        match (int(opcao)):
            case 1:
                inserir_usuario(session)
            case 2:
                buscar_usuarios(session)
            case 3:
                excluir_usuario(session)
            case 4:
                inserir_produto(session)
            case 5:
                buscar_produtos(session)
            case 6:
                excluir_produto(session)
            case 7:
                buscar_vendedores(session)
            case 8:
                insert_vendedor(session)
            case 9:
                excluir_vendedor(session)
            case 0:
                print('Até mais...')
                execucao = False

else:
    print("Ocorreu um erro.")