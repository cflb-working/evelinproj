from django.db import models

# Create your models here.
class PadraoCor(models.Model):
    """
    Padrão de cor da amostra de qualidade.
    """
    sem_cor_percent = models.IntegerField("Sem cor (%)", default=0)
    a_25_percent = models.IntegerField("0 a 25% (%)", default=0)
    de_25_a_50_percent = models.IntegerField("25 a 50% (%)", default=0)
    a_50_percent = models.IntegerField("50 a 75% (%)", default=0) # Correção no nome do campo para corresponder à tabela
    a_75_percent = models.IntegerField("75 a 100% (%)", default=0) # Correção no nome do campo para corresponder à tabela

    def __str__(self):
        return f"Padrão de Cor da Amostra - ID: {self.id}"

class Maturacao(models.Model):
    """
    Maturação da amostra de qualidade.
    """
    ponto_1_0_percent = models.IntegerField("1.0 (%)", default=0)
    ponto_1_5_percent = models.IntegerField("1.5 (%)", default=0)
    ponto_2_0_percent = models.IntegerField("2.0 (%)", default=0)
    ponto_2_5_percent = models.IntegerField("2.5 (%)", default=0)

    def __str__(self):
        return f"Maturação da Amostra - ID: {self.id}"
    

class CalibresAmostra(models.Model):
    """
    Calibres da amostra de qualidade.
    """
    p_10_12_percent = models.IntegerField("P (10 a 12) (%)", default=30) # Valor default baseado na planilha
    m_8_9_percent = models.IntegerField("M (8 a 9) (%)", default=20) # Valor default baseado na planilha
    g_6_7_percent = models.IntegerField("G (6 a 7) (%)", default=30) # Valor default baseado na planilha

    def __str__(self):
        return f"Calibres da Amostra - ID: {self.id}"

class Calibre(models.Model):
    """
    Representa um calibre de manga.
    """
    calibre = models.CharField("Calibre", max_length=10)
    legenda_calibre = models.CharField("Legenda Calibre", max_length=20)
    descricao = models.CharField("Descrição", max_length=50)

    def __str__(self):
        return f"Calibre {self.legenda_calibre} ({self.calibre}) - {self.descricao}"

class DanosDetectados(models.Model):
    """
    Danos detectados na amostra de qualidade.
    """
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


class Amostra(models.Model):
    """
    Avaliação da qualidade de uma amostra de mangas de um lote.
    """
    #lote = models.ForeignKey(Lote, on_delete=models.CASCADE, related_name="amostras_qualidade")
    data_avaliacao = models.DateField("Data da Avaliação")
    quantidade_frutos = models.IntegerField("Amostra - Quantidade de Frutos")
    padrao_cor = models.ForeignKey(PadraoCor, on_delete=models.CASCADE)
    maturacao = models.ForeignKey(Maturacao, on_delete=models.CASCADE)
    calibres_amostra = models.ForeignKey(CalibresAmostra, on_delete=models.CASCADE)
    danos_detectados = models.ForeignKey(DanosDetectados, on_delete=models.CASCADE)

    def __str__(self):
        return f"Amostra de Qualidade do Lote - ID: {self.id}"

