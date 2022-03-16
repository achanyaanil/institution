from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.home),
    path('registration/',views.registration),
]

