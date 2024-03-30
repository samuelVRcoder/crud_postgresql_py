import psycopg2

DB_HOST = "CHANGE_ME"
DB_PORT = 5432
DB_NAME = "CHANGE_ME"
DB_USER = "CHANGE_ME"
DB_PASSWORD = "CHANGE_ME"
table = "CHANGE_ME"

conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
    )
        
try:
    cursor = conn.cursor()
    nome = "Samuel"
    idade = 33
            
    cursor.execute(f"INSERT INTO {table} (nome, idade) VALUES (%s, %s)", (nome, idade))
    conn.commit()
    print("Registro inserido com sucesso!")
except Exception as e:
    print(f"Erro ao inserir registro: {e}")


try:
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    registros = cursor.fetchall()
    for registro in registros:
        print(f"ID: {registro[0]}, Nome: {registro[1]}, Idade: {registro[2]}")
except Exception as e:
    print(f"Erro ao listar registros: {e}")


try:
    cursor = conn.cursor()
    nome = "Jose"
    idade = 20
    _id = 1

    cursor.execute(f"update {table} set nome = %s, idade = %s where id = %s", (nome, idade, _id))
            
    
    conn.commit()
    print("Registro atualizado com sucesso!")
except Exception as e:
    print(f"Erro ao atualizar registro: {e}")


try:
    cursor = conn.cursor()
    
    _id = 1
            
    cursor.execute(f"delete from {table} where id = %s", (_id,))
    conn.commit()
    print("Registro deletado com sucesso!")
except Exception as e:
    print(f"Erro ao deletar registro: {e}")

conn.close()



