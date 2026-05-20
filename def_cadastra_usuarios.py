from def_conectar import conectar


import mysql.connector

def cadastrar_usuario():

    login = input("Novo login: ")

    if login.strip() == "":
        print("Login vazio.")
        return

    senha = input("Senha: ")

    if senha.strip() == "":
        print("Senha vazia.")
        return

    print("\n1 - admin")
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
    cursor = db.cursor()

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