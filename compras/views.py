# compras/views.py
from django.shortcuts import render, redirect
from django.db.models import Sum
from datetime import datetime
from .forms import CompraForm
from .models import Compra
from .services import BCBService
from decimal import Decimal

def home(request):
    compras = Compra.objects.all().order_by('-data_compra')
    
    # Totais
    total_usd = compras.aggregate(Sum('quantidade_usd'))['quantidade_usd__sum'] or 0
    total_brl = compras.aggregate(Sum('valor_total_brl'))['valor_total_brl__sum'] or 0
    
    # Custo médio ponderado
    custo_medio = 0
    if total_usd > 0:
        custo_medio = total_brl / total_usd
    
    # Última cotação
    ultima_cotacao = None
    if compras.exists():
        ultima_compra = compras.first()
        ultima_cotacao = ultima_compra.datahora_cotacao
    
    context = {
        'compras': compras,
        'total_usd': total_usd,
        'total_brl': total_brl,
        'custo_medio': custo_medio,
        'ultima_cotacao': ultima_cotacao,
    }
    
    return render(request, 'compras/home.html', context)

def cadastrar_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            data_compra = form.cleaned_data['data_compra']
            quantidade_usd = form.cleaned_data['quantidade_usd']
            
            # Buscar cotação
            bcb_service = BCBService()
            cotacao_data = bcb_service.get_dollar_quote(data_compra)
            
            if cotacao_data:
                cotacao = Decimal(str(cotacao_data['cotacaoCompra']))
                valor_total_brl = quantidade_usd * cotacao
                
                # Criar compra
                compra = Compra(
                    data_compra=data_compra,
                    quantidade_usd=quantidade_usd,
                    cotacao_usd_brl=cotacao,
                    valor_total_brl=valor_total_brl,
                    datahora_cotacao=cotacao_data['dataHoraCotacao']
                )
                compra.save()
                
                return redirect('home')
            else:
                form.add_error(None, 'Não foi possível obter a cotação para esta data.')
    else:
        form = CompraForm()
    
    return render(request, 'compras/cadastrar_compra.html', {'form': form})