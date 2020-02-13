from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_money/<str:location>', views.process_money, name="process_money"),
    path('reset', views.reset),
]