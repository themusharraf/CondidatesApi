from django.urls import path

from .import views


urlpatterns = [
    path('condidate-list/', views.CondidanteListView.as_view()),
    path('condidate/', views.CondidateView.as_view())
]
