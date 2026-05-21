def ver_boletim():

    db = conectar()
    cursor = db.cursor()

    cursor.execute("""
    SELECT *
    FROM vw_boletim
    """)

    resultados = cursor.fetchall()

    print("\n===== BOLETIM =====")

    for aluno, materia, media in resultados:

        situacao = "APROVADO"

        if media < 6:
            situacao = "REPROVADO"

        print(
            f"Aluno: {aluno} | "
            f"Matéria: {materia} | "
            f"Média: {media:.2f} | "
            f"Situação: {situacao}"
        )

    cursor.close()
    db.close()
