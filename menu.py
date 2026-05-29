from interface_grafica import *
from arquivo_listar import *
from arquivo_de_remocao import *
from arquivo_cadastros import *
from arquivo_utilitario import *
from arquivo__de_adicionar_e_editar import *
def menu():
     while True:
          interface()
     
          op = input("Escolha uma opção: ")
          

          if op == "1":
               cadastrar_usuario()
               
          elif op == "2":
               cadastrar_aluno()

          elif op == "3":
               listar_alunos()

          elif op == "4":
               mostrar_materias()

          elif op == "5":
               lancar_nota()

          elif op == "6":
               ver_boletim()

          elif op == "7":
               listar_notas()

          elif op == "8":
               editar_nota()

          elif op == "9":
               remover_nota()

          elif op == "10":
               remover_usuario()

          elif op == "11":
               remover_aluno()

          elif op == "0":
               print("Até a proxima, Fique com o suns...")
               print("░░░░░▄▄▀▀▀▀▀▀▀▀▀▄▄░░░░░")
               print("░░░░█░░░░░░░░░░░░░█░░░░")
               print("░░░█░░░░░░░░░░▄▄▄░░█░░░")
               print("░░░█░░▄▄▄░░▄░░███░░█░░░")
               print("░░░▄█░▄░░░▀▀▀░░░▄░█▄░░░")
               print("░░░█░░▀█▀█▀█▀█▀█▀░░█░░░")
               print("░░░▄██▄▄▀▀▀▀▀▀▀▄▄██▄░░░")
               print("░▄█░█▀▀█▀▀▀█▀▀▀█▀▀█░█▄░")
               break

          else:
               print("opção invalida")