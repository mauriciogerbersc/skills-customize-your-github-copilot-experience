# 📘 Assignment: Construindo APIs REST com framework FastAPI

## 🎯 Objective

Aprender a criar APIs REST utilizando o framework FastAPI, cobrindo conceitos como rotas, métodos HTTP e validação de dados.

## 📝 Tasks

### 🛠️ Criar uma API básica

#### Description
Crie uma API básica com FastAPI que tenha pelo menos duas rotas: uma rota GET que retorna uma mensagem de boas-vindas e uma rota POST que aceita dados JSON e retorna uma resposta formatada.

#### Requirements
Completed program should:

- Ter uma rota GET em `/` que retorna uma mensagem de boas-vindas.
- Ter uma rota POST em `/data` que aceita um JSON com um campo `name` e retorna uma mensagem personalizada.
- Utilizar validação de dados com Pydantic.

### 🛠️ Adicionar documentação automática

#### Description
Utilize os recursos nativos do FastAPI para gerar documentação automática para a API.

#### Requirements
Completed program should:

- A documentação deve estar acessível em `/docs`.
- A API deve incluir descrições e exemplos para cada rota.
- Utilizar o Swagger UI gerado pelo FastAPI.