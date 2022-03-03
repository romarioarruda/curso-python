from db import nova_conexao


with nova_conexao() as conexao:
    cursor = conexao.cursor()

    cursor.execute('SHOW DATABASES')

    for i, database in enumerate(cursor, start=1):
        print(f'Banco de dados {i}: {database[0]}')
        