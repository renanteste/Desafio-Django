# corrigir_datas_sql.py
import os
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cambiodolar.settings')
django.setup()

from django.db import connection

def corrigir_datas_sql():
    print("🔧 Corrigindo datas diretamente no banco...")
    
    with connection.cursor() as cursor:
        # Corrigir data_compra (inverter dia e mês)
        cursor.execute("""
            UPDATE Compra 
            SET data_compra = CONCAT(
                YEAR(data_compra), '-', 
                RIGHT('0' + CAST(DAY(data_compra) AS VARCHAR(2)), 2), '-',
                RIGHT('0' + CAST(MONTH(data_compra) AS VARCHAR(2)), 2
            )
            WHERE id = 1
        """)
        
        # Corrigir datahora_cotacao (inverter dia e mês)
        cursor.execute("""
            UPDATE Compra 
            SET datahora_cotacao = CONCAT(
                YEAR(datahora_cotacao), '-', 
                RIGHT('0' + CAST(DAY(datahora_cotacao) AS VARCHAR(2)), 2), '-',
                RIGHT('0' + CAST(MONTH(datahora_cotacao) AS VARCHAR(2)), 2),
                ' ', 
                CONVERT(VARCHAR(8), datahora_cotacao, 108)
            )
            WHERE id = 1
        """)
        
        print("✅ Datas corrigidas com sucesso!")
        
        # Mostrar resultado
        cursor.execute("SELECT id, data_compra, datahora_cotacao FROM Compra WHERE id = 1")
        row = cursor.fetchone()
        print(f"📅 Resultado:")
        print(f"   ID: {row[0]}")
        print(f"   data_compra: {row[1]}")
        print(f"   datahora_cotacao: {row[2]}")

if __name__ == "__main__":
    corrigir_datas_sql()