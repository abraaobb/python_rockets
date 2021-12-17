# Python Básico

Curso de Python Básico oferecido pela Rockets FPF Tech

------

## Instalação

### Utilizando o choco:

entrar no link e seguir os comandos de instalação:
http://chocolatey.org/install

depois que o choco estiver instalado executar o comando no terminal:
```choco install python```

### Utilizando o instalador:

para instalar normalmente é só acessar o link e seguir os passos de instalações
https://www.python.org/

**OBS:** No Windows ativar o path durante a instalação

após instalar para verificar versão digite o comando no terminal
```python --version```

## Usando o pip

o pip é o gerenciador de pacotesdo python, podemos ver os pacotes disponíveis através do site https://pypi.org/



## Usando o terminal

para usar o terminal inteligente do python abra o terminal e digite
```python```

## Usando o VSCode

Extensão Python
	

Atualizar o pip
	pip install --upgrade pip

Instalar o virtual enviroment
	pip install virtualenv


Criar uma virtual enviroment
	lembrar sempre de setar o diretório
	python -m venv C:\envs\projetoa\


Ativar a virutal enviroment
	acessar o arquivo activate.bat dentro do diretório
	c:\envs\projetoa\Scripts\activate.bat


Requirements
	exportar o requirements
		pip freeze > requirements.txt
	instalar o requirements
		pip install -r requirements.txt
		

Pacotes para pesquisar
	psycopg2
	pip install psycopg2-binary
	django
	pip install Django
	ipython
	pip install ipython
