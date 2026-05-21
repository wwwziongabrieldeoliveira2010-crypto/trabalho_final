from def_conectar import conectar
from def_autenticar import autenticar
from def_listar_usuarios import listar_usuarios 
from def_registrarlogs import registrarlogs
from def_validar_numero import validar_numero

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
