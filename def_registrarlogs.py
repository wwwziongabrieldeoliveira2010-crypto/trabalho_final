from def_conectar import conectar
import datetime from datetime

def registrar_log(usuario, acao):

    db = conectar()
    cursor = db.cursor()

    query = """
    INSERT INTO logs
    (usuario, acao, data_hora)
    VALUES (%s, %s, %s)
    """

    cursor.execute(
        query,
        (
            usuario,
            acao,
            datetime.now()
        )
    )

    db.commit()

    cursor.close()
    db.close()
