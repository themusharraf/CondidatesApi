from django.urls import path

from .import views


urlpatterns = [
    path('condidate-list/', views.CondidanteListView.as_view()),
    path('condidate-form/', views.CondidateView.as_view()),
    path('condidate-save-list/', views.SavedView.as_view()),
    path('condidate-detail/<int:pk>/', views.SavedDetailView.as_view()),
    path('condidate-remove/<int:pk>/', views.RemoweFromSaveView.as_view()),
]
