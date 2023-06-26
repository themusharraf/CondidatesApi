from django.urls import path, include
from rest_framework.routers import DefaultRouter

from anketa.views import CandidateModelViewSet, SavedCandidatesView

router = DefaultRouter()
router.register('ankeata', CandidateModelViewSet)

urlpatterns = [
    path('', include(router.urls), ),
    path('saved/', SavedCandidatesView.as_view(), name='saved'),
]
