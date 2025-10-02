# deploy_sqlserver.py
import os

def setup_sqlserver():
    print("🚀 Configurando ambiente para SQL Server...")
    
    # Configurar variáveis de ambiente para SQL Server
    os.environ.setdefault('DB_ENGINE', 'sqlserver')
    os.environ.setdefault('DB_NAME', 'CambioMoeda')
    os.environ.setdefault('DB_USER', 'candidato')
    os.environ.setdefault('DB_PASSWORD', 'candidato123')
    os.environ.setdefault('DB_HOST', 'VMEXAME24\\SQLEXPRESS')
    
    # A senha será pedida separadamente por segurança
    password = input("🔐 Digite a senha do SQL Server (usuário 'candidato'): ")
    os.environ.setdefault('DB_PASSWORD', password)
    
    print("✅ Variáveis de ambiente configuradas para SQL Server")
    print("📊 Configuração:")
    print(f"   Database: {os.environ.get('DB_NAME')}")
    print(f"   Host: {os.environ.get('DB_HOST')}")
    print(f"   User: {os.environ.get('DB_USER')}")
    print("")
    print("🎯 Agora execute:")
    print("   python manage.py migrate --fake")
    print("   python manage.py runserver")

if __name__ == "__main__":
    setup_sqlserver()