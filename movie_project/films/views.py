from django.shortcuts import render, redirect
from .models import Films
from .forms import FilmsForm


def index(request):
    films = Films.objects.all()
    return render(request, 'films/index.html', {'films': films})

def add(request):
    error = ''
    if request.method == 'POST':
        form = FilmsForm(request.POST)  # Сюда сохранится информация от пользователя.
        if form.is_valid():
            form.save()
            return redirect('page1')
        else:
            error = "Данные были заполнены некорректно"
    form = FilmsForm()
    return render(request, 'films/add.html', {'form': form, 'error': error})
