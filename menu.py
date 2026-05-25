from interface_grafica import *
from arquivo_listar import *
from arquivo_de_remocao import *
from arquivo_cadastros import *
from arquivo_utilitario import *

while True:
     interface()
    
     op = input("Escolha um numero de 0 a 11")
     validar_numero(op)

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
          print("Saindo...")
          break
