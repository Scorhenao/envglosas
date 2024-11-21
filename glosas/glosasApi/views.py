from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import GlosaForLessDocumentation, GlosaForErrorOFfactoring
from .serializers import GlosaForLessDocumentationSerializer,GlosaForErrorOFfactoringSerializer
from .errror_handlers import (
    validation_error_response,
    exception_response,
    method_not_allowed_response,
    object_not_found_response
)
from rest_framework.parsers import JSONParser
from django.http import JsonResponse


# CRUD for GlosaForLessDocumentation

class GlosaForLessDocumentationListView(generics.ListAPIView):
    queryset = GlosaForLessDocumentation.objects.all()
    serializer_class = GlosaForLessDocumentationSerializer
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "status": "200",
            "data": serializer.data, 
            "message": "List retrieved successfully"
        }, status=status.HTTP_200_OK)

class GlosaForLessDocumentationDetailView(APIView):
    def get(self, request, pk=None):
        try:
            # Buscar el objeto por su ID (pk)
            instance = GlosaForLessDocumentation.objects.get(pk=pk)
            serializer = GlosaForLessDocumentationSerializer(instance)
            return Response({
                "status": "200",
                "data": serializer.data,
                "message": "Glosa retrieved successfully"
            }, status=status.HTTP_200_OK)
        except GlosaForLessDocumentation.DoesNotExist:
            # Devolver respuesta de objeto no encontrado
            return Response({
                "status": "error",
                "message": "GlosaForLessDocumentation not found"
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Manejar errores genéricos
            return exception_response(e)

    

def glosa_less_docs_create(request):
    if request.method == 'POST':
        form = GlosaForLessDocumentationForm(request.POST)
        if form.is_valid():
            glosa = form.save()
            # Respuesta JSON si es necesario
            if request.headers.get('Accept') == 'application/json':
                response = {
                    "status": "201",
                    "data": {
                        "id": glosa.pk,
                        "code_glosa": glosa.code_glosa,
                        "description": glosa.description,
                        "rejected_amount": glosa.rejected_amount,
                        "missed_documents": glosa.missed_documents
                    },
                    "message": "Glosa created successfully."
                }
                return JsonResponse(response)
            # Redirección para usuarios normales
            return redirect('glosasForLessDocumentationList')
        else:
            # Manejo de errores para un formulario inválido
            return render(request, 'glosas/less_documentation_create.html', {'form': form})
    else:
        # Renderizar formulario vacío en método GET
        form = GlosaForLessDocumentationForm()
        return render(request, 'glosas/less_documentation_form.html', {'form': form})
def glosa_less_docs_update(request, pk):
    glosa = get_object_or_404(GlosaForLessDocumentation, pk=pk)
    if request.method == 'POST':
        form = GlosaForLessDocumentationForm(request.POST, instance=glosa)
        if form.is_valid():
            form.save()
            response = {
                "status": "success",
                "data": {
                    "id": glosa.pk,
                    "code_glosa": glosa.code_glosa,
                    "description": glosa.description,
                },
                "message": "Glosa updated successfully."
            }
            return JsonResponse(response, status=200)
        else:
            response = {
                "status": "error",
                "data": {},
                "message": "Failed to update glosa. Invalid data."
            }
            return JsonResponse(response, status=400)
    else:
        response = {
            "status": "error",
            "data": {},
            "message": "GET method not allowed for update."
        }
        return JsonResponse(response, status=405)

def glosa_less_docs_delete(request, pk):
    glosa = get_object_or_404(GlosaForLessDocumentation, pk=pk)
    if request.method == 'POST':
        glosa.delete()
        response = {
            "status": "success",
            "data": {},
            "message": "Glosa deleted successfully."
        }
        return JsonResponse(response, status=204)
    else:
        response = {
            "status": "error",
            "data": {},
            "message": "GET method not allowed for deletion."
        }
        return JsonResponse(response, status=405)

# CRUD for GlosaForErrorOFfactoring

class GlosaForErrorOFfactoringListView(generics.ListAPIView):
    queryset = GlosaForErrorOFfactoring.objects.all()
    serializer_class = GlosaForErrorOFfactoringSerializer
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "status": "200",
            "data": serializer.data, 
            "message": "List retrieved successfully"
        }, status=status.HTTP_200_OK)

def glosa_error_factoring_detail(request, pk):
    glosa = get_object_or_404(GlosaForErrorOFfactoring, pk=pk)
    return render(request, 'glosas/error_factoring_detail.html', {'glosa': glosa})

def glosa_error_factoring_create(request):
    if request.method == 'POST':
        form = GlosaForErrorOFfactoringForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('glosasForErrorOFfactoringList')
    else:
        form = GlosaForErrorOFfactoringForm()
        return render(request, 'glosas/error_factoring_form.html', {'form': form})

def glosa_error_factoring_update(request, pk):
    glosa = get_object_or_404(GlosaForErrorOFfactoring, pk=pk)
    if request.method == 'POST':
        form = GlosaForErrorOFfactoringForm(request.POST, instance=glosa)
        if form.is_valid():
            form.save()
            return redirect('glosasForErrorOFfactoringList')
    else:
        form = GlosaForErrorOFfactoringForm(instance=glosa)
    return render(request, 'glosas/error_factoring_form.html', {'form': form})

def glosa_error_factoring_delete(request, pk):
    glosa = get_object_or_404(GlosaForErrorOFfactoring, pk=pk)
    if request.method == 'POST':
        glosa.delete()
        return redirect('glosasForErrorOFfactoringList')
    return render(request, 'glosas/error_factoring_confirm_delete.html', {'glosa': glosa})