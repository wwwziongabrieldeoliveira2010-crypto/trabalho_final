from arquivo_utilitario import *
from arquivo_listar import *



def editar_nota():

    usuario = autenticar("professor")

    if not usuario:
        return

    listar_notas()

    id_nota = input("ID da nota: ")

    if not validar_inteiro(id_nota):
        print("ID inválido.")
        return

    nova_nota = input("Nova nota: ")

    if not validar_nota(nova_nota):
        print("Nota inválida.")
        return

    novo_bimestre = input("Novo bimestre: ")

    if not validar_bimestre(novo_bimestre):
        print("Bimestre inválido.")
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

        if cursor.rowcount == 0:
            print("Nota não encontrada.")
        else:

            registrarlogs(
                usuario,
                f"EDITOU NOTA ID {id_nota}"
            )

            print("Nota atualizada com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro: {err}")

    finally:
        cursor.close()
        db.close()


def lancar_nota():


    usuario = autenticar("professor")

    if not usuario:
        return

    listar_alunos()
    mostrar_materias()

    id_aluno = input("ID do aluno: ")
    id_materia = input("ID da matéria: ")
    nota = input("Nota: ")
    bimestre = input("Bimestre: ")

    if not validar_inteiro(id_aluno):
        print("ID do aluno inválido.")
        return

    if not validar_inteiro(id_materia):
        print("ID da matéria inválido.")
        return

    if not validar_nota(nota):
        print("Nota inválida.")
        return

    if not validar_bimestre(bimestre):
        print("Bimestre inválido.")
        return

    db = conectar()
    cursor = db.cursor()

try:

        cursor.execute(
            "SELECT id_aluno FROM alunos WHERE id_aluno = %s",
            (int(id_aluno),)
        )

        if not cursor.fetchone():
            print("Aluno não encontrado.")
            return

        cursor.execute(
            "SELECT id_materia FROM materias WHERE id_materia = %s",
            (int(id_materia),)
        )

        if not cursor.fetchone():
            print("Matéria não encontrada.")
            return

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
        f"LANÇOU NOTA PARA ALUNO {id_aluno}"
    )

    print("Nota lançada com sucesso!")

except mysql.connector.Error as err:
        print(f"Erro: {err}")

finally:
        cursor.close()
        db.close()

