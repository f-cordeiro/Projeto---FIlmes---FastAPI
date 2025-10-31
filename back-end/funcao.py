from conexao import conectar

def criar_table():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS filmes(
                id INT AUTO_INCREMENT PRIMARY KEY,
                titulo TEXT NOT NULL,
                genero TEXT NOT NULL,
                ano INT NOT NULL,
                nota FLOAT
                )               
            """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar a tabela {erro}")
        finally:
            cursor.close()
            conexao.commit()


def cadastrar_filme(titulo, genero, ano, nota):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO filmes (titulo, genero, ano, nota) VALUES (%s, %s, %s, %s)",
                (titulo, genero, ano, nota)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao cadastrar o filme: {erro}")
        finally:
            cursor.close()
            conexao.close()

def listar_filme():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM filmes ORDER BY ID"
            )
            return cursor.fetchall()      
        except Exception as erro:
            print(f"Erro ao tentar exbir filme: {erro}")
            return []
        finally:
            cursor.close()
            conexao.close()

def atualizar_filme(id, nova_nota):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "UPDATE filmes SET nota = %s WHERE id = %s",
                (nova_nota, id)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao tentar atualizar filme: {erro}")
        finally:
            cursor.close()
            conexao.close()


def deletar_filme(id_filme):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "DELETE FROM filmes WHERE id = %s",
                (id_filme,)
            )
            conexao.commit()
            if cursor.rowcount > 0:
                print("Filme removido com sucesso!")
            else:
                print("Nenhum Filme foi encontrado com o ID fornecido.")
        except Exception as erro:
            print(f"Erro ao tentar inserir filmes: {erro}")
        finally:
            cursor.close()
            conexao.close()

def buscar_filme(id_filme):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM filmes WHERE id = %s",
                (id_filme,)
            )
            return cursor.fetchone()
        except Exception as erro:
            print(f"Erro ao buscar o filme: {erro}")
        finally:
            cursor.close()
            conexao.close()