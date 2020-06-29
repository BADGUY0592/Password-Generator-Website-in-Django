from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def generate(request):
    if request.method == "GET":
        lchar=list('qwertyuiopasdfghjklzxcvbnm')
        length=int(request.GET.get('length'))
        if(request.GET.get('case1')):
            lchar.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
        if(request.GET.get('case2')):
            lchar.extend(list('1234567890'))
        if(request.GET.get('case3')):
            lchar.extend(list('~!@#$%^&*()_+=-[]:;"<>,.?/'))
        rand = ''
        for x in range(length):
            rand+=random.choice(lchar)
        return render(request, 'generator/rand.html',{'rand':rand})