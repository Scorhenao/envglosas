from django.shortcuts import render, get_object_or_404, redirect
from .models import GlosaForLessDocumentation, GlosaForErrorOFfactoring
from .forms import GlosaForLessDocumentationForm, GlosaForErrorOFfactoringForm
# CRUD for GlosaForLessDocumentation

def glosa_less_docs_list(request):
    glosas = GlosaForLessDocumentation.objects.all()
    return render(request, 'glosas/less_documentation_list.html', {'glosas':glosas})

def glosa_less_docs_detail(request, pk):
    glosas = get_object_or_404(GlosaForLessDocumentation, pk=pk)
    return render(request, 'glosas/less_documentation_detail.html', {'glosas':glosas})

def glosa_less_docs_create(request):
    if request.method == 'POST':
        form = GlosaForLessDocumentationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('glosasForLessDocumentationList')
    else:
        form = GlosaForLessDocumentationForm()
        return render(request, 'glosas/less_documentation_form.html', {'form':form})

def glosa_less_docs_update(request, pk):
    glosa = get_object_or_404(GlosaForLessDocumentation, pk=pk)
    if request.method == 'POST':
        form = GlosaForLessDocumentationForm(request.POST, instance=glosa)
        if form.is_valid():
            form.save()
            return redirect('glosasForLessDocumentationList')
    else:
        form = GlosaForLessDocumentationForm(instance=glosa)
    return render(request, 'glosas/less_documentation_form.html', {'form':form})

def glosa_less_docs_delete(request, pk):
    glosa = get_object_or_404(GlosaForLessDocumentation, pk=pk)
    if request.method == 'POST':
        glosa.delete()
        return redirect('glosasForLessDocumentationList')
    return render(request, 'glosas/less_documentation_confirm_delete.html', {'glosa':glosa})


# CRUD for GlosaForErrorOFfactoring

def glosa_error_factoring_list(request):
    glosas = GlosaForErrorOFfactoring.objects.all()
    return render(request, 'glosas/error_factoring_list.html', {'glosas': glosas})

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