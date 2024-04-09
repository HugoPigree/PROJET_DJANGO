from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('show/<int:train_id>' , views.show, name="show"), #int pour eviter une erreur dico et forcer le typage
    path('random/', views.random_train, name="random_train"),
]