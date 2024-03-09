from django.shortcuts import render, HttpResponse
from app.forms import *
# Create your views here.
def djform(request):
    SFO = StudentForm()
    d = {'SFO':SFO}
    return render(request, 'djform.html', d)