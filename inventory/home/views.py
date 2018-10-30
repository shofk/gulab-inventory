from django.shortcuts import render
from chemical.models import ChemicalItem
from itertools import chain

# Create your views here.
def index(request):
    query = request.GET.get('q')
    if query:
        # get all the relevant searches
        chemical_match = ChemicalItem.objects.filter(chemical_name__icontains=query)
        company_match= ChemicalItem.objects.filter(company_name__icontains=query)

        # chain them together
        result = chain(chemical_match, company_match)
        # possibly give them orders as below
        # result = sorted(chain(chemical_match, company_match),
        #                 key=lambda instance: instance.expiration_date)

        # render the results
        return render(request, 'home/search_result.html', {'result': result})
    else:
        return render(request, 'home/home.html', {})
