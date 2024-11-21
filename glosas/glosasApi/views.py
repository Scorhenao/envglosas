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
    def get_object(self, pk):
        try:
            return GlosaForLessDocumentation.objects.get(pk=pk)
        except GlosaForLessDocumentation.DoesNotExist:
            raise NotFound(detail="GlosaForLessDocumentation not found")

    def get(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = GlosaForLessDocumentationSerializer(instance)
        return Response({
            "status": "200",
            "data": serializer.data,
            "message": "Glosa retrieved successfully"
        }, status=status.HTTP_200_OK)


class GlosaForLessDocumentationCreateView(generics.CreateAPIView):
    queryset = GlosaForLessDocumentation.objects.all()
    serializer_class = GlosaForLessDocumentationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "status": "201",
            "data": serializer.data,
            "message": "Glosa created successfully"
        }, status=status.HTTP_201_CREATED)


class GlosaForLessDocumentationUpdateView(generics.UpdateAPIView):
    queryset = GlosaForLessDocumentation.objects.all()
    serializer_class = GlosaForLessDocumentationSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "status": "200",
            "data": serializer.data,
            "message": "Glosa updated successfully"
        }, status=status.HTTP_200_OK)


class GlosaForLessDocumentationDeleteView(generics.DestroyAPIView):
    queryset = GlosaForLessDocumentation.objects.all()
    serializer_class = GlosaForLessDocumentationSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "status": "204",
            "message": "Glosa deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)
        
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