from def_conectar import conectar

import mysql.connector

def cadastrar_aluno():

    usuario = autenticar()

    if not usuario:
        return

    nome = input("Nome: ")

    if not validar_texto(nome):
        print("Nome inválido.")
        return

    idade = input("Idade: ")

    if not validar_numero(idade):
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
                int(float(idade)),
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
