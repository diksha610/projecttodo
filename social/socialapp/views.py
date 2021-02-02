from django.shortcuts import render, redirect
from .models import entry


# Create your views here.

def index(request):
    if request.method =='POST':
        element = request.POST['element']
        e = entry(element=element)
        e.save()
        print('data saved ..')
    d = entry.objects.all()
    return render(request, 'index.html', {'details': d})


def del_element(request, id):
    e = entry.objects.get(pk=id)
    e.delete()
    return redirect('/')
