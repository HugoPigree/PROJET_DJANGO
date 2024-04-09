from django.shortcuts import render
from .models import Train
import random # On importe random pour choisir au hasard un train.

def index(request) :
    return render(request, "index.html",{})

def show(request, train_id):
    train = Train.objects.get(id=train_id)
    return render(request, "show.html", {'train': train}) # 'train': train permet de donner accès à la variable train dans show (d'ou la possibilité de faire train.destination etc)

def random_train(request):
    random_train = random.choice(Train.objects.all())
    return render(request, "show.html", {'train': random_train}) #même chose ici mais cette fois avec l'utilisation de random, on va mettre l'url de la views (random_train) dans notre nav bar index.html

