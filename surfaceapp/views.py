from django.shortcuts import render

# Create your views here.

def home(request):
	context={}
	return render(request, 'home.html', context)

def about(request):
	context={}
	return render(request, 'about.html', context)

def contactus(request):
	context={}
	return render(request, 'contactus.html', context)

def partners(request):
	context={}
	return render(request, 'partners.html', context)

def projects(request):
	context={}
	return render(request, 'projects.html', context)

def partners(request):
	context={}
	return render(request, 'partners.html', context)

def architecture(request):
	context={}
	return render(request, 'architecture.html', context)

def masterplanning(request):
	context={}
	return render(request, 'masterplanning.html', context)

def interiordesign(request):
	context={}
	return render(request, 'interiordesign.html', context)

def landscape(request):
	context={}
	return render(request, 'landscape.html', context)

def competition(request):
	context={}
	return render(request, 'competition.html', context)
