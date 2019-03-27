from django.shortcuts import render
from .forms import InputForm

# Create your views here.


def index(request):
    return render(request, 'input/index.html')


def output(request):
    form = InputForm()
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            #Call the python function
            return render(request, 'input/output.html', {'form': form})
    return render(request, 'input/output.html')
