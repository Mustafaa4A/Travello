from django.shortcuts import render
from .models import Destnation

# Create your views here.


def index(request):
    dests = Destnation.objects.all()
    return render(request, 'index.html', {'dests': dests})
