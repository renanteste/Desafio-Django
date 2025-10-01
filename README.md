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

## Configuração
1. Clone o repositório
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente: `.\venv\Scripts\activate`
4. Instale dependências: `pip install django mysqlclient requests python-dateutil`
5. Configure o banco MySQL no `settings.py`
6. Execute: `python manage.py runserver`

## Estrutura do Banco
```sql
CREATE DATABASE CambioMoeda;
USE CambioMoeda;

CREATE TABLE Compra (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    data_compra DATE NOT NULL,
    quantidade_usd DECIMAL(15,2) NOT NULL,
    cotacao_usd_brl DECIMAL(10,4) NOT NULL,
    valor_total_brl DECIMAL(15,2) NOT NULL,
    datahora_cotacao DATETIME NOT NULL,
    criado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
