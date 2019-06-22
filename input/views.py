from django.shortcuts import render
from .forms import InputForm, outputData

# Create your views here.


def index(request):
	form = InputForm()
	return render(request, 'input/index.html', {'form': form})


def output(request):
	form = InputForm()
	output = outputData()
	if request.method == 'POST':
		print(request.POST)
		form = InputForm(request.POST)
		if form.is_valid():
			#Call the python function
			return render(request, 'input/output.html', {'data': output})
		else:
			print(form.errors)
	return render(request, 'input/output.html')
