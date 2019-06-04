from django.shortcuts import render
from heirarchical_data_mptt.models import Filer
from heirarchical_data_mptt.forms import NewFileForm
from django.http import HttpResponseRedirect

def main_view(request):
    html = 'main.html'
    data = Filer.objects.all()
    return render(request, html, {"data": data})

def add_file(request):
    html = 'newfile.html'
    if request.method == 'POST':
        form = NewFileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Filer.objects.create(
                name=data['name'],
                parent=data['parent']
            )
    form = NewFileForm()
    return render(request, html, {'form': form})