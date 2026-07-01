

# Sistema Escolar em Python

Projeto desenvolvido por Zion , Davi Martins, Emanoel, Samuel Rocca. utilizando Python e MySQL para gerenciamento escolar.

## Funcionalidades

- Cadastro de usuários
- Cadastro de alunos
- Lançamento de notas
- Edição de notas
- Remoção de alunos
- Remoção de usuários
- Visualização de boletim
- Sistema de autenticação
- Registro de logs

## Tecnologias Utilizadas

- Python
- MySQL
- mysql-connector-python
- A nossa mente genial
## Como executar

### 1. Instale as dependências

```bash
pip install mysql-connector-python 

Regras de Negócio
- Apenas usuários autenticados poderão acessar o sistema.
- Apenas usuários com permissão de administrador poderão cadastrar e remover usuários.
- Apenas usuários autorizados poderão cadastrar, editar ou remover alunos.
- Cada aluno deverá possuir um CPF único, não sendo permitido cadastro duplicado.
- As notas dos alunos deverão estar entre 0 e 10.
- O bimestre informado deverá ser um valor entre 1 e 4.
- Não será permitido lançar notas para alunos ou disciplinas que não estejam cadastrados.
- A média dos alunos será calculada automaticamente pelo sistema com base nas notas lançadas.
- O boletim deverá exibir a média final e a situação do aluno (Aprovado ou Reprovado).
    Toda ação importante realizada pelos usuários (como login, cadastro, edição e remoção) deverá ser registrada em um histórico de logs.
