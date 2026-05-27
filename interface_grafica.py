
import time
import random 
import os 
delay = random.randint(1, 3)


def interface():
    print("\n|======================================================|"
                    "\n|-------------------SISTEMA ESCOLAR--------------------|"
                    "\n|======================================================|\n")

    print("              ===========================")
    print("              |  [1] - Cadastrar usuário|")
    print("              |  [2] - Cadastrar aluno  |")
    print("              |=========================|")
    print("              |  [3] - Listar alunos    |")
    print("              |  [4] - Mostrar matérias |")
    print("              |  [5] - Lançar nota      |")
    print("              |  [6] - Ver boletim      |")
    print("              |  [7] - Listar notas     |")
    print("              |  [8] - Editar nota      |")
    print("              |=========================|")
    print("              |  [9] - Remover nota     |")
    print("              |  [10] - Remover usuario |")
    print("              |  [11] - Remover aluno   |")
    print("              |  [0] - Sair             |")
    print("              ===========================")
def loading():
    for i in range(12):

        os.system('cls' if os.name == 'nt' else 'clear')

        print("Iniciando cadastro")

        barra = "🟦" * i + "⬛" * (11 - i)

        print(barra)

        time.sleep(delay)
        
