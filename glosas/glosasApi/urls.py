from django.urls import path
from . import views

urlpatterns = [
    # URLs for GlosaForLessDocumentation
    path('less_documentation/', views.glosa_less_docs_list, name='glosasForLessDocumentationList'),
    path('less_documentation/<int:pk>/', views.glosa_less_docs_detail, name='glosasForLessDocumentationDetail'),
    path('less_documentation/add/', views.glosa_less_docs_create, name='glosasForLessDocumentationCreate'),
    path('less_documentation/<int:pk>/update/', views.glosa_less_docs_update, name='glosasForLessDocumentationUpdate'),
    path('less_documentation/<int:pk>/delete/', views.glosa_less_docs_delete, name='glosasForLessDocumentationDelete'),

    # URLs for GlosaForErrorOFfactoring
    path('error_factoring/', views.glosa_error_factoring_list, name='glosasForErrorOFfactoringList'),
    path('error_factoring/<int:pk>/', views.glosa_error_factoring_detail, name='glosaForErrorOFfactoringDetail'),
    path('error_factoring/add/', views.glosa_error_factoring_create, name='glosaForErrorOFfactoringAdd'),
    path('error_factoring/<int:pk>/update/', views.glosa_error_factoring_update, name='glosaForErrorOFfactoringUpdate'),
    path('error_factoring/<int:pk>/delete/', views.glosa_error_factoring_delete, name='glosaForErrorOFfactoringDelete'),
]