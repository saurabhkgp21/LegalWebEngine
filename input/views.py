from django.shortcuts import render
from .forms import DataCreate
from .models import Data

# Create your views here.


def index(request):
    obj = Data.objects.all()
    appis = 0
    if request.method == 'POST':
        appis = 1
        form = DataCreate(request.POST)
        if form.is_valid():
            form.save()

            return render(request, 'input/index.html', {'form': form, 'appis': appis, 'ob': obj})
    else:
        form = DataCreate()

    return render(request, 'input/index.html', {'form': form, 'appis': appis, 'ob': obj})
