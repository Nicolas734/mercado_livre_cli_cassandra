from usuario.select import buscar_usuarios

def excluir_usuario(session):
    buscar_usuarios(session)
    
    usuario_id = input(str('Digite o id do usuario que deseja excluir: '))
    
    session.execute(f"delete from usuarios where id='{usuario_id}'")
    print(f'\nusuario de id {usuario_id} excluido com sucesso...\n')