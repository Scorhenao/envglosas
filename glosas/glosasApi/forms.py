from django import forms
from .models import GlosaForLessDocumentation, GlosaForErrorOFfactoring

class GlosaForLessDocumentationForm(forms.ModelForm):
    class Meta:
        model = GlosaForLessDocumentation
        fields = ['code_glosa', 'description', 'rejected_amount', 'missed_documents']
        
class GlosaForErrorOFfactoringForm(forms.ModelForm):
    class Meta:
        model = GlosaForErrorOFfactoring
        fields = ['code_glosa', 'description', 'rejected_amount', 'type_error']