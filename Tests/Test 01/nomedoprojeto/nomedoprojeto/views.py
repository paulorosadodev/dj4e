from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.base import View
import html

def checkGuess(guess):
    nivel = False
    if guess:
        try:
            xp = int(guess)
            nivel = 1
            xp_maximo = 100
            while xp >= xp_maximo:
                xp -= xp_maximo
                nivel += 1
                xp_maximo *= 2
        except:
            nivel = 'Bad format for guess:' + html.escape(guess)
    return nivel

def calcular_xp_maximo(guess):
        xp = int(guess)
        nivel = 1
        xp_maximo = 100
        while xp >= xp_maximo:
            xp -= xp_maximo
            nivel += 1
            xp_maximo *= 2
        return xp_maximo*2

class ClassyView(View):
    def get(self, request):
        return render(request, 'nomedoprojeto/guess.html')
    
    def post(self, request):
        guess = request.POST.get('guess')
        msg = checkGuess(guess)
        xp = calcular_xp_maximo(guess)
        return render(request, 'nomedoprojeto/guess2.html', {'message': msg, 'xp': xp, 'atual': guess})