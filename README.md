## Agenda Django

Este é um projeto de agenda desenvolvido com Django.

### Descrição
Uma aplicação web para gerenciar contatos, permitindo cadastro, edição, exclusão e visualização de contatos.

### Estrutura do Projeto
- `contact/`: App principal para gerenciamento de contatos
- `base_templates/` e `base_static/`: Templates e arquivos estáticos globais
- `db.sqlite3`: Banco de dados SQLite padrão do Django

### Requisitos
- Python 3.11+
- Django 4.x

### Instalação
1. Crie e ative um ambiente virtual:
	```bash
	python -m venv .venv
	source .venv/bin/activate
	```
2. Instale as dependências:
	```bash
	pip install django
	```
3. Execute as migrações:
	```bash
	python manage.py migrate
	```
4. Inicie o servidor de desenvolvimento:
	```bash
	python manage.py runserver
	```

### Uso
Acesse `http://127.0.0.1:8000/` no navegador para utilizar a aplicação.

---
Desenvolvido para fins de estudo.
