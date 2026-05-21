from def_conectar import conectar
from def_autenticar import autenticar
from def_listar_notas import listar_notas 
from def_registrarlogs import registrarlogs
from def_vaçidar_numero import validar_numero

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
