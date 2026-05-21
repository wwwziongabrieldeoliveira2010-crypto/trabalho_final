from arquivo_utilitario import *
from arquivo_listar import *




def editar_nota():

    usuario = autenticar()

    if not usuario:
        return

    listar_notas()

    id_nota = input("ID da nota: ")

    if not validar_numero(id_nota):
        print("ID inválido.")
        return

    nova_nota = input("Nova nota: ")

    if not validar_numero(nova_nota):
        print("Nota inválida.")
        return

    novo_bimestre = input("Novo bimestre: ")

    if not validar_numero(novo_bimestre):
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
                int(float(novo_bimestre)),
                int(float(id_nota))
            )
        )

        db.commit()

        registrarlogs(
            usuario,
            f"EDITOU NOTA ID {id_nota}"
        )

        print("Nota atualizada!")

    except mysql.connector.Error as err:
        print(f"Erro: {err}")

    finally:
        cursor.close()
        db.close()




def lancar_nota():

    usuario = autenticar()

    if not usuario:
        return

    listar_alunos()
    mostrar_materias()

    id_aluno = input("ID do aluno: ")
    id_materia = input("ID da matéria: ")
    nota = input("Nota: ")
    bimestre = input("Bimestre: ")

    if not validar_numero(id_aluno):
        print("ID inválido.")
        return

    if not validar_numero(id_materia):
        print("ID inválido.")
        return

    if not validar_numero(nota):
        print("Nota inválida.")
        return

    if not validar_numero(bimestre):
        print("Bimestre inválido.")
        return

    db = conectar()
    cursor = db.cursor()

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

    try:

        cursor.execute(
            query,
            (
                int(float(id_aluno)),
                int(float(id_materia)),
                float(nota),
                int(float(bimestre))
            )
        )

        db.commit()

        registrarlogs(
            usuario,
            f"LANÇOU NOTA PARA ALUNO {id_aluno}"
        )

        print("Nota lançada!")

    except mysql.connector.Error as err:
        print(f"Erro: {err}")

    finally:
        cursor.close()
        db.close()
