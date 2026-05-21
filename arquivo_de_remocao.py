from arquivo_utilitario import *
from arquivo_listar import *

def remover_aluno():

    usuario = autenticar("admin")

    if not usuario:
        return

    listar_alunos()

    idaluno = input("Digite o ID do aluno: ")

    if not validar_numero(idaluno):
        print("ID inválido.")
        return

    db = conectar()
    cursor = db.cursor()

    try:

        cursor.execute(
            "DELETE FROM alunos WHERE id_aluno = %s",
            (int(float(idaluno)),)
        )

        db.commit()

        registrarlogs(
            usuario,
            f"REMOVEU ALUNO ID {idaluno}"
        )

        print("Aluno removido!")

    except mysql.connector.Error as err:
        print(f"Erro: {err}")

    finally:
        cursor.close()
        db.close()


def remover_nota():

    usuario = autenticar("admin")

    if not usuario:
        return

    listar_notas()

    id_nota = input("ID da nota: ")

    if not validar_numero(id_nota):
        print("ID inválido.")
        return

    db = conectar()
    cursor = db.cursor()

    try:

        cursor.execute(
            "DELETE FROM notas WHERE id_nota = %s",
            (int(float(id_nota)),)
        )

        db.commit()

        registrarlogs(
            usuario,
            f"REMOVEU NOTA ID {id_nota}"
        )

        print("Nota removida!")

    except mysql.connector.Error as err:
        print(f"Erro: {err}")

    finally:
        cursor.close()
        db.close()




def remover_usuario():

    usuario = autenticar("admin")

    if not usuario:
        return

    idusuario = input("Digite o ID do usuário: ")

    if not validar_numero(idusuario):
        print("ID inválido.")
        return

    db = conectar()
    cursor = db.cursor()

    try:

        cursor.execute(
            "DELETE FROM usuarios WHERE id_usuario = %s",
            (int(float(idusuario)),)
        )

        db.commit()

        registrarlogs(
            usuario,
            f"REMOVEU USUARIO ID {idusuario}"
        )

        print("Usuário removido!")

    except mysql.connector.Error as err:
        print(f"Erro: {err}")

    finally:
        cursor.close()
        db.close()