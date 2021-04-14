from django.urls import path
from .views import *

urlpatterns = [
    path('view/', messages_view),

]
