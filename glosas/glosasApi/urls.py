from django.urls import path

from .views import (
    GlosaForErrorOFfactoringListView,
    GlosaForLessDocumentationListView,
    GlosaForLessDocumentationDetailView,
    GlosaForLessDocumentationCreateView,
    GlosaForLessDocumentationUpdateView,
    GlosaForLessDocumentationDeleteView
)
urlpatterns = [
    # Listar y Detalles
    path('glosas/less_documentation/', GlosaForLessDocumentationListView.as_view(), name='glosasForLessDocumentationListApi'),
    path('glosas/less_documentation/<int:pk>/', GlosaForLessDocumentationDetailView.as_view(), name='glosasForLessDocumentationDetailApi'),

    # Crear
    path('glosas/less_documentation/add/', GlosaForLessDocumentationCreateView.as_view(), name='glosasForLessDocumentationCreateApi'),

    # Actualizar
    path('glosas/less_documentation/<int:pk>/update/', GlosaForLessDocumentationUpdateView.as_view(), name='glosasForLessDocumentationUpdateApi'),

    # Eliminar
    path('glosas/less_documentation/<int:pk>/delete/', GlosaForLessDocumentationDeleteView.as_view(), name='glosasForLessDocumentationDeleteApi'),
    # URLs for GlosaForErrorOFfactoring
    path('glosas/error_factoring/', GlosaForErrorOFfactoringListView.as_view(), name='glosasForErrorOFfactoringListApi'),
    # path('error_factoring/<int:pk>/', views.glosa_error_factoring_detail, name='glosaForErrorOFfactoringDetail'),
    # path('error_factoring/add/', views.glosa_error_factoring_create, name='glosaForErrorOFfactoringCreate'),
    # path('error_factoring/<int:pk>/update/', views.glosa_error_factoring_update, name='glosaForErrorOFfactoringUpdate'),
    # path('error_factoring/<int:pk>/delete/', views.glosa_error_factoring_delete, name='glosaForErrorOFfactoringDelete'),
]