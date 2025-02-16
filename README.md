# FastAPI

Exemplo de implementação utilizando FastAPI com conceitos de DDD.

## Criando Ambiente

Acesse a pasta do projeto e cria uma Virtualenv:

```
$ python -m venv venv
```

Após isso, inicie a Virtualenv criada anteriormente:

* Para Sistemas baseados em Unix
```
$ source venv/bin/active
```
* Para Windows
```
$ venv/Scripts/activate
```

## Dependências do Projeto

### Instalação dos Pacotes

Se preferir instalar todas as dependências do projeto, execute os comandos abaixo:

```
$ pip install "fastapi[standard]"
$ pip install PyJWT
$ pip install passlib
$ pip install bcrypt
$ pip install sqlalchemy
```

### Instação por Requirements

Entre dentro da pasta raiz e execute o seguinte comando, e com isso todas as dependências do projeto serão instaladas:

```
$ pip install -r requirements.txt
```

## Configurações .env

Dentro da pasta src/api, crie um arquivo ".env", assim como o padrão da classe [Config.py](https://github.com/charlesluizmendes/Fast/blob/main/src/api/config.py):

* Exemplo de conteúdo do arquivo
```
DATABASE_URL=sqlite:///database.db
SECRET_KEY=65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Executando o projeto

Acesse a pasta raiz e execute o seguinte comando:

```
$ python run.py
```
