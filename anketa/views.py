from django.db.models import F
from rest_framework.viewsets import ModelViewSet

from anketa.models import Candidate
from anketa.permissions import IsAuthorOrReadOnly
from anketa.serializers import CandidateSerializer, CandidateDetailModelSerializer


class CandidateModelViewSet(ModelViewSet):
    queryset = Candidate.objects.all()
    permission_classes = IsAuthorOrReadOnly,
    serializer_class = CandidateDetailModelSerializer

    def get_queryset(self):
        query = super().get_queryset()
        query.update(view_count=F('view_count') + 1)
        return query
