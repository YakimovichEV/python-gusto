from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>', dish_info),
    path('add/category', category_add)
]
