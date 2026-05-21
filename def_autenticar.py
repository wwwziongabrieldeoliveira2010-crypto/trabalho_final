from def_conectar import conectar
from def_registrarlogs import registrarlogs

def autenticar(cargo_necessario=None):

    tentativas = 5

    while tentativas > 0:

        login_usuario = input("Login: ")
        senha = input("Senha: ")

        db = conectar()
        cursor = db.cursor()

        query = """
        SELECT senha, cargo
        FROM usuarios
        WHERE login = %s
        """

        cursor.execute(query, (login_usuario,))

        resultado = cursor.fetchone()

        cursor.close()
        db.close()

        if resultado:

            senha_banco = resultado[0]
            cargo_usuario = resultado[1]

            if senha == senha_banco:

                if (
                    cargo_necessario
                    and cargo_usuario != cargo_necessario
                ):

                    print(f"Apenas {cargo_necessario}.")
                    return None

                registrarlogs(
                    login_usuario,
                    "LOGIN REALIZADO"
                )

                print("Login realizado!")

                return login_usuario

        tentativas -= 1

        print(f"Tentativas restantes: {tentativas}")

    print("Usuário bloqueado.")
    return None
