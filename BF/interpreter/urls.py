from django.urls import path
from . import views

urlpatterns = [
    # path("interpreter/",views.functionName)
    path("",views.functionName),
    path("nav/",views.navTest)
]
