from django.shortcuts import render, redirect
from .forms import CatequeseInfantilForm


def catequese_infantil(request):
    if request.method == 'POST':
        form = CatequeseInfantilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:procure_secretaria')
    else:
        form = CatequeseInfantilForm()
    return render(request, 'catequese_infantil.html', {'form': form})

def procure_secretaria(request):
    return render(request, 'procure_secretaria.html')