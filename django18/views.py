from django.shortcuts import render

def home(request):
	return render(request, 'apps/about.html', {})

def about(request):
	return render(request, 'apps/about.html', {})

def contact(request):
	return render(request, 'apps/contact.html', {})