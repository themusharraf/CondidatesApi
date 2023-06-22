from django.urls import path, include
from rest_framework.routers import DefaultRouter

from anketa.views import CandidateModelViewSet

router = DefaultRouter()
router.register('ankeata', CandidateModelViewSet)

urlpatterns = [
    path('', include(router.urls), )
]
