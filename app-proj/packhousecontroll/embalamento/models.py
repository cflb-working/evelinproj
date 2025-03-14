from django.db import models

# Create your models here.
class Lote(models.Model):
    """
    Representa um lote de mangas - Dados do Cliente do Packing House.
    """
    codigo_cliente_embalado = models.CharField("MTF Código", max_length=20, unique=True)
    inicio_embalamento = models.DateField("Início Embalamento")
    fim_embalamento = models.DateField("Fim Embalamento")
    quantidade_pallets = models.CharField("Quantidade de Pallets", max_length=50, blank=True, null=True) # Pode ser IntegerField ou CharField dependendo da necessidade
    destino_cliente = models.CharField("Destino/Cliente", max_length=100)
    calibres_lote = models.CharField("Calibres do Lote", max_length=50)
    marca_caixa = models.CharField("Marca da Caixa", max_length=100, blank=True, null=True)
    embalamento_observacoes = models.CharField("Embalamento Observações", max_length=200, blank=True, null=True)
    variedade = models.CharField("Variedade", max_length=50)

    # Campos de Aproveitamento da Fruta (mantidos aqui, ou podem ser movidos para outro modelo se necessário)
    #entrada_processado = models.IntegerField("Entrada Processado", default=0)
    #refugo_kg = models.DecimalField("Refugo (kg)", max_digits=10, decimal_places=2, default=0.00)
    #embalado_total = models.DecimalField("Embalado Total (kg)", max_digits=10, decimal_places=2, default=0.00)
    #cont_refligo = models.IntegerField("Cont Reflugo", default=0)
    #comentarios_gerais = models.TextField("Comentários Gerais", blank=True, null=True)

    def __str__(self):
        return self.codigo_cliente_embalado

    #@property
    #def aproveitamento_percentual(self):
    #    """Calcula o percentual de aproveitamento da fruta."""
    #    if self.entrada_processado > 0:
    #        return (self.embalado_total / self.entrada_processado) * 100
    #    return 0.00
    

class TipoCaixa(models.Model):
    """
        Representa um tipo de caixa.
    """
    padrao_caixa = models.CharField("Tipo da Caixa", max_length=50)
    descricao = models.CharField("Descrição", max_length=50)

    def __str__(self):
        return f"{self.padrao_caixa} - {self.descricao}"

class Pallet(models.Model):
    """
    Representa um pallet embalado.
    """

    numero_pallet = models.IntegerField("Número do Pallet")
    calibres = models.ManyToManyField("Calibre")
    data_embalamento = models.DateField("Data do Embalamento")
    total_caixas = models.IntegerField("Total de Caixas")
    tipo_caixa = models.ForeignKey("TipoCaixa", on_delete=models.CASCADE)
    
    pertence_lote = models.ForeignKey(Lote, on_delete=models.CASCADE, related_name='pallets')

    def __str__(self):
        return f"Pallet {self.numero_pallet} - Calibre {self.calibres.get().legenda_calibre} ({self.calibres.get().calibre})"
    

class DanosDetectados(models.Model):
    """
    Danos detectados na amostra de qualidade.
    """
    amostra_qualidade = models.ForeignKey(AmostraQualidade, on_delete=models.CASCADE, related_name="danos_detectados")
    trips_percent = models.IntegerField("Trips (%)", default=40) # Valor default baseado na planilha
    escoramento_percent = models.IntegerField("Escoramento (%)", default=20) # Valor default baseado na planilha
    cochonilha_percent = models.IntegerField("Cochonilha (%)", default=20) # Valor default baseado na planilha
    fisicu_percent = models.IntegerField("Físico (%)", default=50) # Valor default baseado na planilha
    acaro_percent = models.IntegerField("Acaro (%)", default=0) # Valor default baseado na planilha
    mosca_percent = models.IntegerField("Mosca (%)", default=0) # Valor default baseado na planilha
    lenticela_percent = models.IntegerField("Lenticela (%)", default=20) # Valor default baseado na planilha
    mecanico_percent = models.IntegerField("Mecânico (%)", default=20) # Valor default baseado na planilha
    colapso_percent = models.IntegerField("Colapso (%)", default=0) # Valor default baseado na planilha
    latex_percent = models.IntegerField("Latex (%)", default=20) # Valor default baseado na planilha
    golpe_sol_percent = models.IntegerField("Golpe Sol (%)", default=0) # Valor default baseado na planilha
    furo_corte_percent = models.IntegerField("Furo/Corte (%)", default=20) # Valor default baseado na planilha
    dano_polna_percent = models.IntegerField("Dano Polar (%)", default=30) # Valor default baseado na planilha
    mancha_cal_percent = models.IntegerField("Mancha de Cal (%)", default=20) # Valor default baseado na planilha


    def __str__(self):
        return f"Danos Detectados da Amostra: {self.amostra_qualidade}"        