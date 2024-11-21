from django.urls import path

from . views import GlosaForLessDocumentationListView, GlosaForErrorOFfactoringListView, GlosaForLessDocumentationDetailView


urlpatterns = [
    # URLs for GlosaForLessDocumentation
    path('glosas/less_documentation/', GlosaForLessDocumentationListView.as_view(), name='glosasForLessDocumentationListApi'),
    path('glosas/less_documentation/<int:pk>/', GlosaForLessDocumentationDetailView.as_view(), name='glosasForLessDocumentationDetailApi'),
    # path('less_documentation/add/', views.glosa_less_docs_create, name='glosasForLessDocumentationCreate'),
    # path('less_documentation/<int:pk>/update/', views.glosa_less_docs_update, name='glosasForLessDocumentationUpdate'),
    # path('less_documentation/<int:pk>/delete/', views.glosa_less_docs_delete, name='glosasForLessDocumentationDelete'),

    # URLs for GlosaForErrorOFfactoring
    path('glosas/error_factoring/', GlosaForErrorOFfactoringListView.as_view(), name='glosasForErrorOFfactoringListApi'),
    # path('error_factoring/<int:pk>/', views.glosa_error_factoring_detail, name='glosaForErrorOFfactoringDetail'),
    # path('error_factoring/add/', views.glosa_error_factoring_create, name='glosaForErrorOFfactoringCreate'),
    # path('error_factoring/<int:pk>/update/', views.glosa_error_factoring_update, name='glosaForErrorOFfactoringUpdate'),
    # path('error_factoring/<int:pk>/delete/', views.glosa_error_factoring_delete, name='glosaForErrorOFfactoringDelete'),
]