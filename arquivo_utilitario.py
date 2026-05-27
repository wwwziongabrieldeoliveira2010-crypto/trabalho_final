import mysql.connector
from datetime import datetime



# CONEXÃO
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Senac2026"
)

cursor = db.cursor()

# CRIAR BANCO
cursor.execute("CREATE DATABASE IF NOT EXISTS boletim")

# USAR BANCO
cursor.execute("USE boletim")

# =========================
# TABELA USUÁRIOS
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (

    id_usuario INT AUTO_INCREMENT PRIMARY KEY,

    login VARCHAR(50) UNIQUE NOT NULL,

    senha VARCHAR(255) NOT NULL,

    cargo VARCHAR(20) NOT NULL
)
""")

# =========================
# TABELA ALUNOS
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (

    id_aluno INT AUTO_INCREMENT PRIMARY KEY,

    nome VARCHAR(100) NOT NULL,

    idade INT NOT NULL,

    cpf CHAR(11) UNIQUE NOT NULL
)
""")

# =========================
# TABELA MATÉRIAS
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS materias (

    id_materia INT AUTO_INCREMENT PRIMARY KEY,

    nome_materia VARCHAR(100) UNIQUE NOT NULL
)
""")

# INSERIR MATÉRIAS
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

# =========================
# TABELA NOTAS
# =========================
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

# =========================
# TABELA LOGS
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (

    id_log INT AUTO_INCREMENT PRIMARY KEY,

    usuario VARCHAR(100) NOT NULL,

    acao VARCHAR(255) NOT NULL,

    data_hora DATETIME NOT NULL
)
""")

# =========================
# VIEW BOLETIM
# =========================
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

# =========================
# INSERIR ALUNO
# =========================
cursor.execute("""
INSERT INTO alunos (nome, idade, cpf)
VALUES (%s, %s, %s)
""", ("João", 16, "12345678901"))

# PEGAR ID DO ALUNO
id_aluno = cursor.lastrowid

# =========================
# INSERIR NOTA
# =========================
cursor.execute("""
INSERT INTO notas (nota, bimestre, fk_id_aluno, fk_id_materia)
VALUES (%s, %s, %s, %s)
""", (8.5, 1, id_aluno, 1))

# SALVAR ALTERAÇÕES
db.commit()

print("Banco de dados criado com sucesso!")
print("Aluno e nota cadastrados!")

# FECHAR CONEXÃO
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


def validar_numero(numero):

    if numero.strip() == "":
        return False

    try:
        float(numero)
        return True

    except:
        return False


def validarcpf(cpf):

    if not cpf.isdigit():
        return False

    if len(cpf) != 11:
        return False

    return True

def registrarlogs(usuario, acao):

    db = conectar()
    cursor = db.cursor()

    query = """
    INSERT INTO logs
    (usuario, acao, data_hora)
    VALUES (%s, %s, %s)
    """

    cursor.execute(
        query,
        (
            usuario,
            acao,
            datetime.now()
        )
    )

    db.commit()

    cursor.close()
    db.close()



def autenticar(cargo_necessario=None):

    tentativas = 5

    while tentativas > 0:

        login_usuario = input("Login: ")
        senha = input("Senha: ")

        db = conectar()
        cursor = db.cursor()

        query = """
        SELECT senha, cargo
        FROM usuarios
        WHERE login = %s
        """

        cursor.execute(query, (login_usuario,))

        resultado = cursor.fetchone()

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

                    print(f"Apenas {cargo_necessario}.")
                    return None

                registrarlogs(
                    login_usuario,
                    "LOGIN REALIZADO"
                )

                print("Login realizado!")

                return login_usuario

        tentativas -= 1

        print(f"Tentativas restantes: {tentativas}")

    print("Usuário bloqueado.")
    return None
