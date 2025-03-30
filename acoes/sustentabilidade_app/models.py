from django.db import models
from django.utils import timezone 

class UsuarioSustentavel(models.Model):
    nome = models.CharField(max_length=100)
    consumo_energia = models.FloatField(help_text="Consumo de energia em kWh/dia")
    consumo_agua = models.FloatField(help_text="Consumo de água em L/dia")
    residuos = models.FloatField(help_text="Resíduos não recicláveis em kg/dia")
    uso_transporte = models.FloatField(help_text="Distância percorrida em km/dia")
    nota_sustentabilidade = models.FloatField(null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
        
    def calcular_sustentabilidade(self):
        """Calcula a nota com base nos dados diários inseridos."""
        peso_energia = max(0, 10 - self.consumo_energia / (50/30)) 
        peso_agua = max(0, 10 - self.consumo_agua / (100/30))  
        
        peso_residuos = max(0, 10 - self.residuos / (2/7))  
        peso_transporte = max(0, 10 - self.uso_transporte / (20/7))  
        media = (peso_energia + peso_agua + peso_residuos + peso_transporte) / 4
        return round(min(5, media / 2), 1)  
    
    def save(self, *args, **kwargs):
        self.nota_sustentabilidade = self.calcular_sustentabilidade()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} - Nota: {self.nota_sustentabilidade}"
