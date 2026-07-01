

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

##  Regras de Negócios
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

## Tecnologias Utilizadas

- Python
- MySQL
- mysql-connector-python
- A nossa mente genial
## Como executar
## 1. Clonar o repositório

```bash
git clone https://github.com/wwwziongabrieldeoliveira2010-crypto/trabalho_final.git
```

## 2. Acessar a pasta do projeto

```bash
cd trabalho_final
```

## 3. Instalar as dependências

Caso utilize o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Ou instale manualmente:

```bash
pip install mysql-connector-python
```

## 4. Configurar o banco de dados

1. Certifique-se de que o MySQL esteja instalado e em execução.
2. Abra o arquivo principal do projeto.
3. Altere as informações de conexão, caso necessário:

```python
host="localhost"
user="root"
password="SUA_SENHA"
```

4. Execute o programa pela primeira vez para criar automaticamente o banco de dados e as tabelas.

## 5. Executar o sistema

No terminal:

```bash
python main.py
```

(Substitua `main.py` pelo nome correto do seu arquivo principal.)

## 6. Login

Ao iniciar o sistema, escolha uma das opções disponíveis no menu e faça login com um usuário cadastrado.

## 7. Funcionalidades

- Cadastro de alunos;
- Cadastro de professores;
- Cadastro de disciplinas;
- Cadastro de turmas;
- Matrícula de alunos;
- Consulta de informações;
- Alteração de dados;
- Exclusão de registros;
- Controle de notas;
- Controle de frequência.

## 8. Encerrando

Para sair do sistema, selecione a opção **Sair** no menu principal.

## ⚠️ Observações

- É necessário possuir o MySQL instalado.
- O banco é criado automaticamente na primeira execução (caso essa funcionalidade esteja implementada).
- Caso ocorra erro de conexão, verifique o usuário, senha e se o serviço do MySQL está ativo.
### 1. Instale as dependências

```bash
pip install mysql-connector-python 

