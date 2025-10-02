# compras/views.py
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.http import JsonResponse
from datetime import datetime
from .forms import CompraForm
from .models import Compra
from .services import BCBService
from decimal import Decimal
from datetime import date, timedelta

def home(request):
    compras = Compra.objects.all().order_by('-data_compra')
    
    # Totais
    total_usd = compras.aggregate(Sum('quantidade_usd'))['quantidade_usd__sum'] or 0
    total_brl = compras.aggregate(Sum('valor_total_brl'))['valor_total_brl__sum'] or 0
    
    # Custo médio ponderado
    custo_medio = 0
    if total_usd > 0:
        custo_medio = total_brl / total_usd
    
    # Última cotação - pega da compra mais recente
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
        # Verificar se é uma requisição AJAX para buscar cotação
        if 'ajax_cotacao' in request.POST:
            try:
                data_compra_str = request.POST.get('data_compra')
                data_compra = datetime.strptime(data_compra_str, '%Y-%m-%d').date()
                
                # Validar se a data é válida (pelo menos 2 dias antes de hoje)
                hoje = date.today()
                data_minima = hoje - timedelta(days=2)
                if data_compra > data_minima:
                    return JsonResponse({
                        'error': 'A data da compra deve ser pelo menos 2 dias antes da data atual (D-1).'
                    }, status=400)
                
                bcb_service = BCBService()
                cotacao_data = bcb_service.get_dollar_quote(data_compra)
                
                if cotacao_data:
                    return JsonResponse({
                        'cotacao': float(cotacao_data['cotacaoCompra']),
                        'data_cotacao': cotacao_data['dataHoraCotacao']
                    })
                else:
                    return JsonResponse({
                        'error': 'Não foi possível obter a cotação para esta data. Verifique se é um dia útil.'
                    }, status=400)
                    
            except ValueError as e:
                return JsonResponse({
                    'error': 'Data inválida. Use o formato correto.'
                }, status=400)
            except Exception as e:
                return JsonResponse({
                    'error': f'Erro interno: {str(e)}'
                }, status=500)
        
        # Processamento normal do formulário de compra
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