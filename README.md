# Desafio Django - Sistema de Câmbio

## Descrição
Sistema para cadastro de compras de dólares e cálculo de custo médio da carteira, integrado com a API do Banco Central do Brasil.

## Funcionalidades
- ✅ Cadastro de compras de dólares
- ✅ Integração com API do BCB para cotações
- ✅ Cálculo automático do custo médio ponderado
- ✅ Visualização da carteira com totais
- ✅ Validação de datas úteis

## Tecnologias
- Django 5.2.6
- MySQL
- Python 3.11
- Bootstrap 5
# Desafio Django - Sistema de Câmbio

## Deploy no SQL Server

1. **Use a branch sqlserver-deploy**
```bash
git checkout sqlserver-deploy

## Instalação Rápida

1. **Clone o repositório**
```bash
git clone https://github.com/renanteste/Desafio-Django.git
cd Desafio-Django
Configure o ambiente Python

bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# OU
venv\Scripts\activate     # Windows
Instale as dependências

bash
pip install -r requirements.txt
Configure as variáveis de ambiente (opcional)

bash
# No Windows (PowerShell)
$env:DB_NAME = "CambioMoeda"
$env:DB_USER = "seu_usuario"
$env:DB_PASSWORD = "sua_senha"
$env:DB_HOST = "localhost"

# No Linux/Mac
export DB_NAME="CambioMoeda"
export DB_USER="seu_usuario"
export DB_PASSWORD="sua_senha"
export DB_HOST="localhost"
Execute o servidor

bash
python manage.py runserver
Acesse: http://localhost:8000

text

## 6. Commitar essas mudanças finais

```bash
PS C:\Users\gpnet\Documents\Desafio-django\cambiodolar> git add .
PS C:\Users\gpnet\Documents\Desafio-django\cambiodolar> git commit -m "feat: add deployment setup files"
PS C:\Users\gpnet\Documents\Desafio-django\cambiodolar> git push origin main