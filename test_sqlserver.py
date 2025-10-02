# test_sqlserver.py
import pyodbc

def test_connection():
    servers = [
        "VMEXAME24\\SQLEXPRESS",
        "localhost\\SQLEXPRESS", 
        ".\\SQLEXPRESS",
        "VMEXAME24",
        "localhost"
    ]
    
    for server in servers:
        try:
            print(f"🔧 Tentando conectar em: {server}")
            conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE=CambioMoeda;UID=candidato;PWD=candidato123'
            conn = pyodbc.connect(conn_str, timeout=5)
            print(f"✅ Conectado com sucesso em: {server}")
            conn.close()
            return server
        except Exception as e:
            print(f"❌ Falha em {server}: {e}")
    
    return None

print("🧪 Testando conexões SQL Server...")
working_server = test_connection()

if working_server:
    print(f"🎯 Servidor funcionando: {working_server}")
else:
    print("💥 Nenhum servidor funcionou. Verifique:")
    print("   1. SQL Server está instalado?")
    print("   2. Serviço SQL Server está rodando?")
    print("   3. Instância SQLEXPRESS existe?")