## 1. Objetivo
Criar uma API REST com FastAPI para inserir, recuperar e remover registros em um banco de dados.

## 2. Tecnologias
**FastAPI**  
**Pydantic**
**SQLAlchemy**  
**PostgreSQL**  
**Alembic**  

## 3. Endpoints
- **Criar item** (`POST /users/`): Adiciona um novo registro.
- **Recuperar item** (`GET /users/{user_id}`): Recupera um novo registro.
- **Deletar item** (`DELETE /users/{user_id}`): Remove um registro pelo ID.

## 4. Estrutura do Projeto
```
project/
|-- app/
|   |-- main.py               # Aplicação FastApi
|   |-- database.py           # Configurar banco de dados e a conexão
|   |-- models.py             # Criar modelo SQLAlchemy
|   |-- schemas.py            # Definir schemas Pydantic
|   |-- db_ops.py             # operações do banco de dados
|   |-- endpoints.py          # Implementar endpoints
|-- alembic/                  # Configurar e rodar migrações com Alembic 
|-- .env                      # Credenciais do projeto
|-- pyproject.toml            # Configuração e dependencias do projeto
|-- poetry.lock               # Lock das dependencias
|-- README.md                 # Passos para a execução do projeto
```  

## 5. Estrutura da Tabela
A tabela deve conter os seguintes campos:

- `id` (uuid): Id do usuário
- `name` (string): Nome do usuário.
- `last_name` (string): Sobrenome do usuário.
- `college_course` (string): Curso universitário do usuário.

## 5. Adicione exemplos a raiz do projeto com `Postman Collections` ou no README com `curl`

