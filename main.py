from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from usuario.insert import inserir_usuario
from usuario.select import buscar_usuarios
from usuario.deletar import excluir_usuario

cloud_config= {
        'secure_connect_bundle': 'secure-connect-cassandra.zip'
}
auth_provider = PlainTextAuthProvider('DAZzJreSkmXuryLkOQoCAFhM', 'nbPqijNx1AZ.Mr470ZR2AoBdS,Yk6i8YEI2d8rlG,m_9L26UMPmZ4,rXRtNMKOGGe9ywN3.Uv4x8l0lURZudDiURInuZaPX3y3ZelC4xiebZY,bhpv1rhTPTwqAy7,TH')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('mercado_livre')

row = session.execute("select release_version from system.local").one()

if row:
    print("Conexão bem sucedida...")
    print(session.execute("select * from usuarios").all())
    execucao = True
    
    while execucao:
        
        print('''
            [1] inserir usuario
            [2] buscar usuarios
            [3] excluir usuario
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
            case 0:
                print('Até mais...')
                execucao = False

else:
    print("Ocorreu um erro.")