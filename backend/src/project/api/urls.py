from django.urls import path 

from .views import Question1ListView, Question1DetailView

urlpatterns = [
    path('',Question1ListView.as_view()),
    path('<pk>', Question1DetailView.as_view())
]