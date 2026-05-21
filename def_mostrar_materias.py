from def_conectar import conectar

def mostrar_materias():

    db = conectar()
    cursor = db.cursor()

    cursor.execute("""
    SELECT id_materia, nome_materia
    FROM materias
    """)

    materias = cursor.fetchall()

    print("\n===== MATÉRIAS =====")

    for materia in materias:

        print(
            f"ID: {materia[0]} | "
            f"Nome: {materia[1]}"
        )

    cursor.close()
    db.close()
