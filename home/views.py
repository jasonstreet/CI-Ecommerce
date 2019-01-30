from django.shortcuts import render

# Create your views here.
def index(request):
    """Display index page"""
    return render(request, "index.html")