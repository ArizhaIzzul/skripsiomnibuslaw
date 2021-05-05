from django.urls import path
from .views import index #views dari folder app 

urlpatterns = [
    path ("", index),
]