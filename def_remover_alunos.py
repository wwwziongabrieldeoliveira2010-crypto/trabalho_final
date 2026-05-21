from def_conectar import conectar
from def_autenticar import autenticar
from def_listar_alunos import listar_alunos 
from def_registrarlogs import registrarlogs

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
