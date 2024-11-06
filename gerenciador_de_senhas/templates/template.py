import sys
import os

sys.path.append(os.path.abspath(os.curdir))

from projetos_praticos.gerenciador_de_senhas.model import password
from projetos_praticos.gerenciador_de_senhas.views.password_views import FernetHasher



action = input('Digite 1 para salvar uma nova senha ou 2 para ver uma senha')

if action == '1':
    if len (Password.get()) == 0:
        key, path = FernetHasher.create_key(archive=True)
        print('Sua chave foi criada com sucesso, salve-a com cuidado!')
        print(f'Chave: {key.decode("utf-8")}')
        if path:
            print('Chave salva no arquivo, lembre-se de remover o arquivo após o transferir de local')
            print(f'Caminho: {path}')
    else:
        key = input('Digite sua chave usada para criptografia, use sempre a mesma chave: ')

    domain = input('Dominio: ')
    password = input('Senha: ')
    fernet_user = FernetHasher(key)
    p1 = Password(domain=domain, password=fernet_user.encrypt(password).decode('utf-8'))
    p1.save()

elif action == '2':
    domain = input('Dominio: ')
    key = input('Key: ')
    fernet_user = FernetHasher(key)
    data = Password.get()

    for i in data:
        if domain in i['domain']:
            password = fernet_user.decrypt(i['password'])
        if password:
            print(f'Sua senha: {password}')
        else:
            print('Nenhuma senha foi encontrada para o domínio')