from django.urls import path
from .views import (
    GlosaForLessDocumentationListView,
    GlosaForLessDocumentationDetailView,
    GlosaForLessDocumentationCreateView,
    GlosaForLessDocumentationUpdateView,
    GlosaForLessDocumentationDeleteView,
    GlosaForErrorOFfactoringListView,
    GlosaForErrorOFfactoringDetailView,
    GlosaForErrorOFfactoringCreateView,
    GlosaForErrorOFfactoringUpdateView,
    GlosaForErrorOFfactoringDeleteView,
)

urlpatterns = [
    # URLs for GlosaForLessDocumentation
    path('glosas/less_documentation/', GlosaForLessDocumentationListView.as_view(), name='glosasForLessDocumentationListApi'),
    path('glosas/less_documentation/<int:pk>/', GlosaForLessDocumentationDetailView.as_view(), name='glosasForLessDocumentationDetailApi'),
    path('glosas/less_documentation/add/', GlosaForLessDocumentationCreateView.as_view(), name='glosasForLessDocumentationCreateApi'),
    path('glosas/less_documentation/<int:pk>/update/', GlosaForLessDocumentationUpdateView.as_view(), name='glosasForLessDocumentationUpdateApi'),
    path('glosas/less_documentation/<int:pk>/delete/', GlosaForLessDocumentationDeleteView.as_view(), name='glosasForLessDocumentationDeleteApi'),

    # URLs for GlosaForErrorOFfactoring
    path('glosas/error_factoring/', GlosaForErrorOFfactoringListView.as_view(), name='glosasForErrorOFfactoringListApi'),
    path('glosas/error_factoring/<int:pk>/', GlosaForErrorOFfactoringDetailView.as_view(), name='glosasForErrorOFfactoringDetailApi'),
    path('glosas/error_factoring/add/', GlosaForErrorOFfactoringCreateView.as_view(), name='glosasForErrorOFfactoringCreateApi'),
    path('glosas/error_factoring/<int:pk>/update/', GlosaForErrorOFfactoringUpdateView.as_view(), name='glosasForErrorOFfactoringUpdateApi'),
    path('glosas/error_factoring/<int:pk>/delete/', GlosaForErrorOFfactoringDeleteView.as_view(), name='glosasForErrorOFfactoringDeleteApi'),
]
