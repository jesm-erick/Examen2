#from django.shortcuts import render

# Create your views here.
#from django.shortcuts import render, redirect

# Create your views here.
#def index(request):
    return render(request, 'index.html', {})
    


#from django.shortcuts import render, redirect
#from gestionMaquinaria.models import Name

# Create your views here.
#def index(request):
    #names_from_db = Name.objects.all()
    #context_dict = {'names_from_context': names_from_db}
    #return render(request, 'index.html', context_dict)

from django.shortcuts import render, redirect
from myapp.models import Name
from myapp.forms import NameForm

# Create your views here.
def index(request):
    names_from_db = Name.objects.all()

    form = NameForm()

    context_dict = {'names_from_context': names_from_db, 'form': form}

    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'index.html', context_dict)
        else:
            print(form.errors)    

    return render(request, 'index.html', context_dict)