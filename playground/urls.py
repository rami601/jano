from django.urls import path
from .  import views

urlpatterns = [
    path("",views.say_hi,name='home'),
    path("<str:years>/<str:month>",views.year,name='home'),
    path("contect",views.test,name="test")
    

]