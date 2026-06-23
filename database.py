from datetime import datetime
import mysql.connector
from getpass import getpass
import sys

# =========================
# CONEXÃO MYSQL
# =========================

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Senac2026"
)

cursor = db.cursor()

# =========================
# CRIAR BANCO
# =========================

cursor.execute("CREATE DATABASE IF NOT EXISTS boletim")

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

# =========================
# INSERIR MATÉRIAS
# =========================

materias = [
    ("Matemática",),
    ("Português",),
    ("História",),
    ("Geografia",),
    ("Ciências",),
    ("Inglês",)
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
# FINALIZAR
# =========================

db.commit()

print("Banco de dados criado com sucesso!")

cursor.close()
db.close()
 

def conectar():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Senac2026",
        database="boletim"
    )

