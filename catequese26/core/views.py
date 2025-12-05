from django.http import FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CatequeseInfantilForm, CrismaForm
from .models import CatequeseInfantilModel, CrismaModel
from .services import gerar_ficha_catequese, gerar_ficha_crisma

def catequese_infantil(request):
    if request.method == 'POST':
        form = CatequeseInfantilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:procure_secretaria')
    else:
        form = CatequeseInfantilForm()
    return render(request, 'catequese_infantil.html', {'form': form})

def crisma(request):
    if request.method == 'POST':
        form = CrismaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:procure_secretaria')
    else:
        form = CrismaForm()
    return render(request, 'crisma.html', {'form': form})

def procure_secretaria(request):
    return render(request, 'procure_secretaria.html')

def listar_fichas(request):
    fichas = CatequeseInfantilModel.objects.filter(ficha_impressa=False).order_by('nome')
    fichasCrisma = CrismaModel.objects.filter(ficha_impressa=False).order_by('nome')
    mensagem = 'Fichas Pendentes de Impressão'
    contexto = {'fichas': fichas,'fichasCrisma': fichasCrisma, 
                'mensagem': mensagem}
    return render(request, 'listar_fichas.html', contexto)

def listar_todas_fichas(request):
    fichas = CatequeseInfantilModel.objects.all().order_by('nome')
    fichasCrisma = CrismaModel.objects.all().order_by('nome')
    mensagem = 'Todas as Fichas de Inscrição'
    contexto = {'fichas': fichas,'fichasCrisma': fichasCrisma, 
                'mensagem': mensagem}
    return render(request, 'listar_fichas.html', contexto)

def imprimir_ficha(request):
    if request.method == 'POST':
        ficha_id = request.POST.get('ficha_id')
        ficha = get_object_or_404(CatequeseInfantilModel, id=ficha_id)
        ficha.ficha_impressa = True
        ficha.save()
        pdf_path = gerar_ficha_catequese(ficha)
        return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    return redirect('core:listar_fichas')

def imprimir_ficha_crisma(request):
    if request.method == 'POST':
        ficha_id = request.POST.get('ficha_id')
        ficha = get_object_or_404(CrismaModel, id=ficha_id)
        ficha.ficha_impressa = True
        ficha.save()
        pdf_path = gerar_ficha_crisma(ficha)
        return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    return redirect('core:listar_fichas')