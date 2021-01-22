from .models import Toy
from .forms import ToyForm
from django.shortcuts import get_object_or_404, render, redirect


def index(request):
    if request.method == 'GET':
        toys = Toy.objects.all()
        return render(request, 'toys/toys.html', {'toys': toys})


def toy(request, pk):
    toy = Toy.objects.get(pk=pk)
    return render(request, 'toys/toy.html', {'toy': toy})


def toy_create(request):
    if request.method == 'POST':
        form = ToyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ToyForm()

    return render(request, 'toys/new_toy.html', {'form': form})


def about(request):
    return render(request, 'toys/about.html')
