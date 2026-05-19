import mysql.connector
from datetime import datetime


def conectar():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Senac2026",
        database="boletim"
    )

db = conectar()

cursor = db.cursor()



cursor.execute("CREATE DATABASE IF NOT EXISTS boletim")




cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (

    id_usuario INT AUTO_INCREMENT PRIMARY KEY,

    login VARCHAR(50) UNIQUE NOT NULL,

    senha VARCHAR(255) NOT NULL,

    cargo VARCHAR(20) NOT NULL
)
""")



cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (

    id_aluno INT AUTO_INCREMENT PRIMARY KEY,

    nome VARCHAR(100) NOT NULL,

    idade INT NOT NULL,

    cpf CHAR(11) UNIQUE NOT NULL
)
""")



cursor.execute("""
CREATE TABLE IF NOT EXISTS materias (

    id_materia INT AUTO_INCREMENT PRIMARY KEY,

    nome_materia VARCHAR(100) UNIQUE NOT NULL
)
""")



materias = [
    ('Matemática',),
    ('Português',),
    ('História',),
    ('Geografia',),
    ('Ciências',),
    ('Inglês',)
]

cursor.executemany("""
INSERT IGNORE INTO materias (nome_materia)
VALUES (%s)
""", materias)



cursor.execute("""
CREATE TABLE IF NOT EXISTS notas (

    id_nota INT AUTO_INCREMENT PRIMARY KEY,

    nota FLOAT NOT NULL,

    bimestre INT NOT NULL,

    fk_id_aluno INT NOT NULL,

    fk_id_materia INT NOT NULL,

    FOREIGN KEY (fk_id_aluno)
    REFERENCES alunos(id_aluno)
    ON DELETE CASCADE,

    FOREIGN KEY (fk_id_materia)
    REFERENCES materias(id_materia)
    ON DELETE CASCADE
)
""")



cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (

    id_log INT AUTO_INCREMENT PRIMARY KEY,

    usuario VARCHAR(100) NOT NULL,

    acao VARCHAR(255) NOT NULL,

    data_hora DATETIME NOT NULL
)
""")



cursor.execute("""
CREATE OR REPLACE VIEW vw_boletim AS

SELECT

    a.nome AS aluno,

    m.nome_materia AS materia,

    AVG(n.nota) AS media

FROM notas n

JOIN alunos a
ON n.fk_id_aluno = a.id_aluno

JOIN materias m
ON n.fk_id_materia = m.id_materia

GROUP BY
a.nome,
m.nome_materia
""")

# Salvar alterações
db.commit()

print("Banco de dados 'boletim' criado com sucesso!")

# Fechar conexão
cursor.close()
db.close()



def conectar():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Senac2026",
        database="boletim"
    )


def validar_texto(texto):

    if texto.strip() == "":
        return False

    if any(char.isdigit() for char in texto):
        return False

    return True
def validaçao_numero(numero):
    if numero.strip() == "":
        return False

    if not numero.isdigit():
        return False
    
    return True

def validarcpf(cpf):
    if cpf.strip() == "":
        return False
    if not cpf.isdigit():
        return False
    
    return True

def registrarlogs(usuario,acão):


    db = conectar()

    cursor = db.conectar()

    cursor.execute()

query = """
INSERT INTO logs
(usuario, ação, data_hora)
VALUES (%s, %s,%s)
"""

cursor.close()
def autenticar(cargo_necessario=None):

    tentativas = 5

    while tentativas > 0:

        login_usuario = input("login: ")
        senha = input("senha: ")

        db = conectar()
        cursor = db.cursor()

        query = """
        SELECT senha cargo
        FROM usuarios
        WHERE login = %s
        """

        cursor.execute(query(login_usuario,))
        
        resultado = cursor.fetchone  

        cursor.close()
        db.close()

        if resultado:
 
            senha_banco = resultado[0]
            cargo_usuario = resultado[1]
 
            if senha == senha_banco:
 
                if (
                    cargo_necessario
                    and cargo_usuario != cargo_necessario
                ):
 
                    print(
                        f"Acesso negado. "
                        f"Apenas {cargo_necessario}."
)
 
                    return None
 
                registrarlogs(
                    login_usuario,
                    "LOGIN REALIZADO"
                )
 
                return login_usuario
        
        tentativas -= 1
 
        print(
            f"Login inválido. "
            f"Tentativas restantes: {tentativas}"
        )
 
    print("Usuário bloqueado.")
    return None

def cadastrar_usuario():

    login = input("Novo login: ")
 
    if login.strip() == "":
        print("Login vazio.")
        return
 
    senha = input("Senha: ")
 
    if senha.strip() == "":
        print("Senha vazia.")
        return
 
    print("\nCARGOS:")
    print("1 - admin")
    print("2 - professor")
 
    opcao = input("Escolha: ")
 
    if opcao == "1":
        cargo = "admin"
 
    elif opcao == "2":
        cargo = "professor"
 
    else:
        print("Cargo inválido.")
        return
 
    db = conectar()
    cursor = db.conectar()

    query = """
    INSERT INTO usuarios
    (login, senha, cargo)
    VALUES (%s, %s, %s)
    """

    try:
 
        cursor.execute(
            query,
            (
                login,
                senha,
                cargo
            )
        )
 
        db.commit()
 
        print("Usuário cadastrado!")
 
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
 
    finally:
        cursor.close()
        db.close()

def cadastrar_aluno():

    usuario = autenticar()

    if not usuario:
        return

    nome = input("Nome: ")
    
    if not validar_texto(nome):
        print("Nome inválido.")
        return

    idade = input("Idade: ")

    if not validaçao_numero(idade):
        print("Idade inválida.")
        return
    
    cpf = input("CPF: ")

    if not validarcpf(cpf):
        print("CPF inválido.")
        return

    db = conectar()
    cursor = db.cursor()

    query = """
    INSERT INTO alunos
    (nome, idade, cpf)
    VALUES (%s, %s, %s)
    """

    try:

        cursor.execute(
            query,
            (
                nome,
                int(idade),
                cpf
            )
        )

        db.commit()

        registrarlogs(
            usuario,
            f"CADASTROU ALUNO {nome}"
        )

        print("Aluno cadastrado!")

    except mysql.connector.Error as err:
        print(f"Erro: {err}")

    finally:
        cursor.close()
        db.close()


def listar_alunos():

    db = conectar()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM alunos")

    alunos = cursor.fetchall()

    print("\n===== ALUNOS =====")

    for aluno in alunos:

        print(
            f"ID: {aluno[0]} | "
            f"Nome: {aluno[1]} | "
            f"Idade: {aluno[2]} | "
            f"CPF: {aluno[3]}"
        )

    cursor.close()
    db.close()

def mostrar_materia(): 

    db = conectar()
    cursor = db.cursor()

    cursor.execute("""
    SELECT id_materia, nome_materia
    FROM materias
    """)

    materias = cursor.fetchall()

    print("\n======MATERIAS======")

    for materia in materias:

        print(
                      f"ID: {materia[0]} | "
            f"Nome: {materia[1]}"
        )

    cursor.close()
    db.close()


def lancar_nota():

    usuario = autenticar()

    if not usuario:
        return
    
    listar_alunos()
    mostrar_materia()


    id_aluno = input("\nID do aluno: ")
    id_materia = input("ID da matéria: ")
    nota = input("Nota: ")
    bimestre = input("Bimestre: ")


    if not validaçao_numero(id_aluno):
        print("ID do aluno inválido.")
        return

    if not validaçao_numero(id_materia):
        print("ID da matéria inválido.")
        return

    if not validaçao_numero(nota):
        print("Nota inválida.")
        return

    if not validaçao_numero(bimestre):
        print("Bimestre inválido.")
        return
    
    db = conectar()
    cursor = db.cursor()

    query = """
    INSERT INTO notas
    (
        fk_id_aluno,
        fk_id_materia,
        nota,
        bimestre
    )
    VALUES (%s, %s, %s, %s)
    """
    try:

        cursor.execute(
            query,
            (
                int(id_aluno),
                int(id_materia),
                float(nota),
                int(bimestre)
            )
        )

        db.commit()

        registrarlogs(
            usuario,
            f"NOTA LANÇADA PARA ALUNO {id_aluno}"
        )

        print("Nota lançada!")

        
    except mysql.connector.Error as err:
        print(f"Erro: {err}")

    finally:
        cursor.close()
        db.close()

def listar_notas():

    db = conectar()
    cursor = db.cursor()

    query = """
    SELECT
        n.id_nota,
        a.nome,
        m.nome_materia,
        n.nota,
        n.bimestre
    FROM notas n

    JOIN alunos a
        ON n.fk_id_aluno = a.id_aluno

    JOIN materias m
        ON n.fk_id_materia = m.id_materia
    """

    cursor.execute(query)

    notas = cursor.fetchall()

    print("\n======NOTAS======")

    for nota in notas:

        print(
            f"ID Nota: {nota[0]} | "
            f"Aluno: {nota[1]} | "
            f"Matéria: {nota[2]} | "
            f"Nota: {nota[3]} | "
            f"Bimestre: {nota[4]}"
        )

    cursor.close()
    db.close()


def editarnota():
    usuario = autenticar()
    if not usuario:
        return
    listar_notas()

    id_nota = input("digite o ID  de sua nota: ")

    if not validaçao_numero(id_nota):
        print("ID invalido")
        return
    
    nova_nota = input("digite sua nova nota: ")


    if not validaçao_numero(nova_nota):
        print("nota invalida")


    novo_bimestre = input("digite um novo bimestre: ")

    if not validaçao_numero(novo_bimestre):
        print("nota invalida")
        return
    
    db = conectar()
    cursor = db.cursor()

    query = """
    UPDATE notas
    SET
        nota = %s,
        bimestre = %s
    WHERE id_nota = %s
    """

    try:

        cursor.execute(
            query,
            (   
                float(nova_nota),
                int(novo_bimestre),
                int(id_nota)
            )

        )

        db.commit()

        registrarlogs(
            usuario,
            f"EDITOU NOTA ID{id_nota}"
        )

        print("nota atualizada!")

    except mysql.connector.Error as err:
        print(f"o erro foi {err}")

    finally:
        cursor.close()
        db.close()


    
    
def remover_nota():

    usuario = autenticar("admin")

    if not usuario:
        return
    
    listar_notas()

    id_nota = input("digite o ID da nota que você que remover: ")
    if not validaçao_numero(id_nota):
        print("id invalida")
        return
    db = conectar()
    cursor = db.cursor()
    try:

        cursor.execute(
            "DELETE FROM notas WHERE id_nota = %s",
            (int(id_nota),)
        )

        db.commit()

        registrarlogs(
            usuario,
            f"REMOVEU NOTA ID {id_nota}"
        )

        print("nota removida")

    except mysql.connector.Error as err:
        print(f"o erro {err}")

    finally:
        cursor.close()
        db.close

def ver_boletim():
 
    db = conectar()
    cursor = db.cursor()
 
    cursor.execute("""
    SELECT *
    FROM vw_boletim
    """)
 
    resultados = cursor.fetchall()

    print("\n===== BOLETIM =====")

    for aluno, materia, media in resultados:

        situacao = "APROVADO"

        if media < 6:
            situacao = "REPROVADO"

        print(
            f"Alunos: {aluno} | "
            f"Matéria: {materia} | "
            f"Média: {media:.2f} | "
            f"Situação: {situacao}"
        )

    cursor.close()
    db.close()
     
def remover_usuario():
    
    usuario = autenticar("admin")

    if not usuario:
        return 

    idusuario = input("digite o id do usuario: ")

   
    
    db = conectar()
    cursor = db.cursor()

    try:

        cursor.execute(
            "DELETE FROM usuarios WHERE id_usuario = %s",
            (int(idusuario),)
            
        )
    
        db.commit()

        registrar_log(
            usuario,
            f"REMOVEU USUARIO ID {idusuario}"
        )

        print("usuario removido!")

    except mysql.connector.Error as err:
        print(f"Erro: {err}")

    finally:
        cursor.close()
        db.close()


def menu():
 
    while True:
 
        print("\n===== SISTEMA ESCOLAR =====")
        print("1 - Cadastrar usuário")
        print("2 - Cadastrar aluno")
        print("3 - Listar alunos")
        print("4 - Mostrar matérias")
        print("5 - Lançar nota")
        print("6 - Ver boletim")
        print("7 - Listar notas")
        print("8 - Editar nota")
        print("9 - Remover nota")
        print("10 - Remover usuario")
        print("0 - Sair")
 
        opcao = input("Escolha: ")
 
        if opcao == "1":
            cadastrar_usuario()
 
        elif opcao == "2":
            cadastrar_aluno()
 
        elif opcao == "3":
            listar_alunos()
 
        elif opcao == "4":
            mostrar_materia()
 
        elif opcao == "5":
            lancar_nota()
 
        elif opcao == "6":
            ver_boletim()
 
        elif opcao == "7":
            listar_notas()
 
        elif opcao == "8":
            editarnota()
 
        elif opcao == "9":
            remover_nota()
 
        elif opcao == "10":
            remover_usuario()
        
        elif opcao == "0":
 
            print("Sistema encerrado.")
            break
 
        else:
            print("Opção inválida.")
 

if __name__ == "__main__":
    menu()
 
