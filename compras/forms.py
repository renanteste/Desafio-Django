# compras/forms.py
from django import forms
from datetime import date, timedelta
from .services import BCBService

class CompraForm(forms.Form):
    data_compra = forms.DateField(
        label='Data da Compra',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    )
    quantidade_usd = forms.DecimalField(
        label='Quantidade de Dólares',
        max_digits=15,
        decimal_places=2,
        min_value=0.01,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})
    )
    
    def clean_data_compra(self):
        data_compra = self.cleaned_data['data_compra']
        hoje = date.today()
        
        # Verifica se a data é HOJE ou no FUTURO
        if data_compra >= hoje:
            raise forms.ValidationError("A data da compra deve ser anterior ao dia atual.")
        
        # Verifica se é pelo menos D-1 (2 dias antes)
        data_minima = hoje - timedelta(days=2)
        if data_compra > data_minima:
            raise forms.ValidationError("A data da compra deve ser pelo menos 2 dias antes da data atual (D-1).")
        
        # Verifica se é dia útil
        bcb_service = BCBService()
        if bcb_service.is_weekend(data_compra) or bcb_service.is_holiday(data_compra):
            raise forms.ValidationError("A data da compra deve ser um dia útil.")
        
        return data_compra