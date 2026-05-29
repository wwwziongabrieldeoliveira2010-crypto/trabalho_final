from arquivo_utilitario import *
from interface_grafica import loading



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
        loading()
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