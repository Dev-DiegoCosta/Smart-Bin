

usuarios = {}

def cadastrar_usuario(cpf):
    if cpf not in usuarios:
        usuarios[cpf] = 0
        return True
    return False

def adicionar_pontos(cpf, pontos):
    if cpf in usuarios:
        usuarios[cpf] += pontos

def get_pontos(cpf):
    return usuarios.get(cpf, 0)
