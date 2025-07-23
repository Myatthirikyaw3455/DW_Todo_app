from django.shortcuts import render
from .models import TodoModel
# Create your views here.

def TodoList(request):
    todo = TodoModel.objects.all()
    context = {
        'todo' : todo
    }
    return render(request, 'index.html',context)
    


#data pya ml so view mhr pya ml
#variable ko small nae pl kyay nyar 