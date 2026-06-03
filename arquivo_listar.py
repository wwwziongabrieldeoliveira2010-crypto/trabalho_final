from arquivo_utilitario import *

def listar_alunos():

    db = conectar()
    cursor = db.cursor()

    cursor.execute("""SELECT * FROM alunos ORDER BY nome ASC""")

    alunos = cursor.fetchall()

    print("\n===== ALUNOS =====")

    for aluno in alunos:

        print(
            f"ID: {aluno[0]} | "
            f"Nome: {aluno[1]} | "
            f"Idade: {aluno[2]} | "
            f"CPF: {aluno[3]}"
        )

    cursor.close()
    db.close()

def mostrar_materias():

    db = conectar()
    cursor = db.cursor()

    cursor.execute("""
    SELECT id_materia, nome_materia
    FROM materias ORDER BY id_materia, nome_materia ASC
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


def listar_notas():

    db = conectar()
    cursor = db.cursor()

    query = """
    SELECT
        n.id_nota,
        a.nome,
        m.nome_materia,
        n.nota,
        n.bimestre
    FROM notas n

    JOIN alunos a
        ON n.fk_id_aluno = a.id_aluno

    JOIN materias m
        ON n.fk_id_materia = m.id_materia

    """

    cursor.execute(query)

    notas = cursor.fetchall()

    print("\n===== NOTAS =====")

    for nota in notas:

        print(
            f"ID: {nota[0]} | "
            f"Aluno: {nota[1]} | "
            f"Matéria: {nota[2]} | "
            f"Nota: {nota[3]} | "
            f"Bimestre: {nota[4]}"
        )

    cursor.close()
    db.close()


def ver_boletim():

    db = conectar()
    cursor = db.cursor()

    cursor.execute("""
    SELECT *
    FROM vw_boletim 
    ORDER BY aluno ASC
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



def listar_usuarios():

    usuario = autenticar("admin")

    if not usuario:
        return

    db = conectar()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM usuarios")

    usuario = cursor.fetchall()

    print("\n===== usuarios =====")

    for usuario in usuario:

        print(
            f"ID: {usuario[0]} | "
            f"Nome: {usuario[1]} | "
            f"Senha: {usuario[2]} | "
            f"Cargo: {usuario[3]}"
        )

    cursor.close()
    db.close()