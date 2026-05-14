import mysql.connector
from datetime import datetime


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
def validadação_numero(numero):
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


    cn = conectar()

    cursor = cn.conectar()

query = """
    INSERT INTO logs
    (usuario, ação)


"""