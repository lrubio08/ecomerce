from django.shortcuts import render

# Vista para el index global
def index(request):
    return render(request, 'index.html')
