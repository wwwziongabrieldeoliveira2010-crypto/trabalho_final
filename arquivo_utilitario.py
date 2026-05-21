import mysql.connector
from datetime import datetime


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Senac2026"
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS boletim")

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
