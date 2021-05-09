from django.shortcuts import render
import random

def home(request):
    return render(request, 'partnerapp/home.html')

def result(request):
    list = ('다연','연우','서영','소은','유진','은성','경나','도윤','혜준','주연','현주','예림','정인','민정','연수','한빛','수현','원아','진영','서경','정운','윤서','수화')
    person = random.sample(list, 2)
    return render(request, 'partnerapp/result.html', {'person' : person})