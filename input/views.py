from django.shortcuts import render
from .forms import InputForm

# Create your views here.


def index(request):
	form = InputForm()
	return render(request, 'input/index.html', {'form': form})


def output(request):
	form = InputForm()
	if request.method == 'POST':
		print(request.POST)
		form = InputForm(request.POST)
		if form.is_valid():
			#Call the python function
			return render(request, 'input/output.html', {'form': form})
		else:
			print(form.errors)
	return render(request, 'input/output.html')
