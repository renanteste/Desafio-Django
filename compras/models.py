# compras/models.py
from django.db import models

class Compra(models.Model):
    data_compra = models.DateField()
    quantidade_usd = models.DecimalField(max_digits=15, decimal_places=2)
    cotacao_usd_brl = models.DecimalField(max_digits=10, decimal_places=4)
    valor_total_brl = models.DecimalField(max_digits=15, decimal_places=2)
    datahora_cotacao = models.DateTimeField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Compra'
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

    def __str__(self):
        return f"Compra de ${self.quantidade_usd} em {self.data_compra}"