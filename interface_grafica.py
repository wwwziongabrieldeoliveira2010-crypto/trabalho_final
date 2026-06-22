
import time
import os 



def interface():
    print("\n|======================================================|"
                    "\n|-------------------SISTEMA ESCOLAR--------------------|"
                    "\n|======================================================|\n")

    print("              ===========================")
    print("              |  [1] -  Cadastrar usuário|")
    print("              |  [2] -  Cadastrar aluno  |")
    print("              |========================= |")
    print("              |  [3] -  Listar alunos    |")
    print("              |  [4] -  Mostrar matérias |")
    print("              |  [5] -  Lançar nota      |")
    print("              |  [6] -  Ver boletim      |")
    print("              |  [7] -  Listar notas     |")
    print("              |  [8] -  eitar nota       |")
    print("              |  [9] -  Listar usuarios  |") 
    print("              |========================= |")
    print("              |  [10] - Remover nota     |")
    print("              |  [11] - Remover usuario  |")
    print("              |  [12] - Remover aluno    |")
    print("              |  [0] -  Sair             |")
    print("              ============================")


def loading():
      for i in range(12):

        os.system('cls' if os.name == 'nt' else 'clear')

        print("=" * 30)
        print("   INICIANDO CADASTRO")
        print("=" * 30)

        barra = "🟦" * i + "⬛" * (12 - i)

        porcentagem = int((i / 11) * 100)

        print(f"\n[{barra}]")
        print(f"\nCarregando... {porcentagem}%")

        time.sleep(0.2)

        os.system('cls' if os.name == 'nt' else 'clear')
        ("Cadastro iniciado com sucesso!")


        
