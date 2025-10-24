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
            filmes = cursor.fetchall()
            if filmes:
                for filme in filmes:
                    id, titulo, genero, ano, nota = filme
                    print(f"ID: {id} | Filme: {titulo} | Gênero: {genero} | Ano: {ano} | Nota: {nota}")
            else:
                print("Nenhum filme cadastrado ainda")        
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
            print(f"Erro ao tentar atualizar aluno: {erro}")
        finally:
            cursor.close()
            conexao.close()
