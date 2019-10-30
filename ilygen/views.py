from django.shortcuts import render
from django.http import HttpResponse
from .models import Gen
import random

def random_ily():
    ily = ['Я тебя люблю', 'I love you', '我爱你', 'seni seviyorum', "je t'aime", 'Te amo', 'انا احبك']
    print(random.choice(ily))
    return random.choice(ily)

def index(request):
    gen = Gen.objects.all()
    return render(request, 'index.html',
                  {'gen': [random_ily,]})
