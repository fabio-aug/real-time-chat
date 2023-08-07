# Real Time Chat
Chat em tempo real construído em python utilizando o Flet e implementação de testes automatizados através do Selenium.

## Dependências do projeto

- flet
- selenium
- typing (padrão do python)
- unittest (padrão do python)
- subprocess (padrão do python)

### Instalação

```
pip install flet selenium
```

## Execução

Na pasta raiz do projeto (`path\real-time-chat`), execute o comando no terminal:

```
python main.py
```

## Testes

Na pasta raiz do projeto (`path\real-time-chat`), execute o comando no terminal:

```
python -m unittest discover -s .\tests\ -p "*_tests.py"
```