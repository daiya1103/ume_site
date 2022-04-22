from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from base.models import User

# Create your views here.

class Index(ListView):
    template_name = 'base/index.html'
    model = User

def login(request):
    context = {}
    return render(request, 'pages/login.html', context)