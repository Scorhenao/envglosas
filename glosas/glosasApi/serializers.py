from rest_framework import serializers
from .models import GlosaForLessDocumentation, GlosaForErrorOFfactoring

class GlosaForLessDocumentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlosaForLessDocumentation
        fields = ['code_glosa', 'description', 'rejected_amount', 'missed_documents']

class GlosaForErrorOFfactoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlosaForErrorOFfactoring
        fields = ['code_glosa', 'description', 'rejected_amount', 'type_error']