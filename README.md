
  ![Title png](https://github.com/user-attachments/assets/2500d2d1-a9db-4036-ab93-cb824e131810)


Este é o backend de um sistema de gestão de alunos desenvolvido em um Projeto Integrador da Univesp, feito com Django e Django Rest Framework (DRF). O projeto utiliza MariaDB como banco de dados e oferece uma API para gerenciar informações de usuários, alunos, professores e outros elementos relacionados ao sistema.

## Requisitos

- Python 3.9 ou superior
- Django 4.x
- Django Rest Framework (DRF)
- MariaDB
- Git
- pip (gerenciador de pacotes Python)

## Instalação

### 1. Clonar o repositório

Clone o repositório do projeto para sua máquina local:


### 1. Clone o repositório
```bash
git clone https://github.com/emanueljn/backend_sistema_de_gestao_de_alunos.git
cd sistema-de-gestao-de-alunos-backend
```

### 2. Instalar as dependências
```bash
Com o ambiente virtual ativo, instale as dependências necessárias:
```

### 3. Intalar depedencias
```bash
pip install -r requirements.txt
```

### 4. Crie banco de dados MariaDB
```bash
CREATE DATABASE sga;
CREATE USER 'usuario'@'localhost' IDENTIFIED BY 'senha';
GRANT ALL PRIVILEGES ON sga.* TO 'usuario'@'localhost';
FLUSH PRIVILEGES;
```

### 5. Aplicar as migrações
Após configurar o banco de dados, aplique as migrações para criar as tabelas necessárias:

```bash
python manage.py migrate
```
### 6. Criar um superusuário
Para acessar o painel administrativo do Django, crie um superusuário:

```bash
python manage.py createsuperuser
```
### 7. Rodar o servidor de desenvolvimento
Execute o servidor de desenvolvimento do Django para iniciar a aplicação:

```bash
python manage.py runserver
```

### A aplicação estará disponível em http://127.0.0.1:8000/.

### 8. Rodar o servidor de desenvolvimento
Execute o servidor de desenvolvimento do Django para iniciar a aplicação:


## Autores

Emanuel de Jesus Nardes, Eduardo Vinicius de Araujo, Kauã Franchini Lima, Lucas Jonatas Dionísio, Marcos Alexandre Yoshiwara, Rafael de Oliveira Claro Pedroso, Silvio Jose Batista, Vitório Felício do Santos
