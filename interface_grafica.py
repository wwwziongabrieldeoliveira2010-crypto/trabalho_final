from arquivo_cadastros import *
from arquivo_de_remocao import *
from arquivo_listar import *
import time
import random 
import os 
delay = random.randint(1, 4)


def interface():
    print("\n|=====================================================|"
                "\n|-------------------SISTEMA ESCOLAR-------------------|"
                "\n|=====================================================|\n")

    print("1 - |Cadastrar usuário|")
    print("2 - |Cadastrar aluno|")
    print("3 - |Listar alunos|")
    print("4 - |Mostrar matérias|")
    print("5 - |Lançar nota|")
    print("6 - |Ver boletim|")
    print("7 - |Listar notas|")
    print("8 - |Editar nota|")
    print("9 - |Remover nota|")
    print("10- |Remover usuario|")
    print("11- |Remover aluno|")
    print("0 - |Sair|")


def loading():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("iniciando cadastro")
        time.sleep(delay)
        print("⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
        time.sleep(delay)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("iniciando cadastro")
        print("🟦🟦⬛⬛⬛⬛⬛⬛⬛⬛⬛")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("iniciando cadastro")
        print("🟦🟦🟦⬛⬛⬛⬛⬛⬛⬛⬛")
        time.sleep(delay)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("iniciando cadastro")
        print("🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛")
        time.sleep(delay)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("iniciando cadastro")
        print("🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛")
        time.sleep(delay)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("iniciando cadastro")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("iniciando cadastro")
        print("🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦")
        time.sleep(2)
        
loading()