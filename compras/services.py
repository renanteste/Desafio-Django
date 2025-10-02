# compras/services.py
import requests
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import holidays

class BCBService:
    BASE_URL = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata"
    
    def __init__(self):
        self.br_holidays = holidays.Brazil()
    
    def is_weekend(self, date):
        return date.weekday() >= 5
    
    def is_holiday(self, date):
        return date in self.br_holidays
    
    def get_previous_business_day(self, date):
        previous_day = date - timedelta(days=1)
        while self.is_weekend(previous_day) or self.is_holiday(previous_day):
            previous_day -= timedelta(days=1)
        return previous_day
    
    def format_date_for_api(self, date):
        return date.strftime("%m-%d-%Y")
    
    def get_dollar_quote(self, date):
        try:
            # Encontra o dia útil anterior à data informada
            business_day = self.get_previous_business_day(date)
            formatted_date = self.format_date_for_api(business_day)
            
            print(f"🔍 Buscando cotação para: {date}")
            print(f"📅 Dia útil anterior: {business_day}")
            print(f"🌐 Data na API: {formatted_date}")
            
            url = f"{self.BASE_URL}/CotacaoDolarDia(dataCotacao=@dataCotacao)"
            params = {
                '@dataCotacao': f"'{formatted_date}'",
                '$top': '100',
                '$format': 'json',
                '$select': 'cotacaoCompra,cotacaoVenda,dataHoraCotacao'
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            if 'value' in data and len(data['value']) > 0:
                quote_data = data['value'][0]
                return {
                    'cotacaoCompra': float(quote_data['cotacaoCompra']),
                    'cotacaoVenda': float(quote_data['cotacaoVenda']),
                    'dataHoraCotacao': quote_data['dataHoraCotacao'],
                    'data_cotacao': business_day
                }
            else:
                return None
                
        except requests.RequestException as e:
            print(f"Erro na requisição: {e}")
            return None
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return None