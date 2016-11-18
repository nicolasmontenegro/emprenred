from django.shortcuts import render

def home(request):
	return render(request, "site/base.html", {})

# Create your views here.
