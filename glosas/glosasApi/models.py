from django.db import models

class Glosa(models.Model):
    code_glosa = models.CharField(max_length=10)
    description = models.TextField()
    rejected_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def show_info(self):
        return f"Código: {self.code_glosa}, Descripción: {self.description}, Monto rechazado: {self.rejected_amount}"

    def getCodigoGlosa(self):
        return self.code_glosa
    
    def getDescriptionGlosa(self):
        return self.description
    
    def getRejectedAmount(self):
        return self.rejected_amount

class GlosaForLessDocumentation(Glosa):
    missed_documents = models.TextField()
    
    def show_info(self):
        return super().show_info() + f", Documentos faltantes: {self.missed_documents}"

class GlosaForErrorOFfactoring(Glosa):
    type_error = models.CharField(max_length=100)
    
    def show_info(self):
        return super().show_info() + f", Tipo de error: {self.type_error}"