from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

from menu.menu_usuario import menu_usuario
from menu.menu_produto import menu_produto
from menu.menu_vendedor import menu_vendedor
from menu.menu_compra import menu_compra

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
Opções:
[1] Menu do usuario
[2] Menu do produto
[3] Menu do vendedor
[4] Menu da compra
[0] sair
        ''')
        
        opcao = input(str('Escolha uma das opções a cima: '))
        match (int(opcao)):
            case 1:
                menu_usuario(session)
            case 2:
                menu_produto(session)
            case 3:
                menu_vendedor(session)
            case 4:
                menu_compra(session)
            case 0:
                print('Até mais...')
                execucao = False
            case _:
                print("Operação não entendida...")

else:
    print("Ocorreu um erro.")