# deploy_sqlserver.py
import os
import django
from django.core.management import execute_from_command_line

def setup_sqlserver():
    # Configurar variáveis de ambiente para SQL Server
    os.environ.setdefault('DB_ENGINE', 'sqlserver')
    os.environ.setdefault('DB_NAME', 'CambioMoeda')
    os.environ.setdefault('DB_USER', 'sa')
    os.environ.setdefault('DB_HOST', 'VMEXAME2A\\SQLEXPRESS')
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cambiodolar.settings')
    django.setup()
    
    print("✅ Configurado para SQL Server")
    print("Execute: python manage.py runserver")

if __name__ == "__main__":
    setup_sqlserver()