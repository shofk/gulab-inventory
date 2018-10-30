from django.shortcuts import render

from .models import ChemicalItem

# Create your views here.
def index(request):
    chemical_list = ChemicalItem.objects.order_by('-expiration_date')

    return render(request, 'chemical/index.html', {'chemical_list':chemical_list})
