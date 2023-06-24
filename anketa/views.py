from django.db.models import F
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from anketa.models import Candidate, Saved
from anketa.permissions import IsAuthorOrReadOnly
from anketa.serializers import CandidateDetailModelSerializer, CandidateSerializer
from rest_framework import generics


class CandidateModelViewSet(ModelViewSet):
    queryset = Candidate.objects.all()
    permission_classes = IsAuthorOrReadOnly,
    serializer_class = CandidateSerializer

    def retrieve(self, request, *args, **kwargs):
        self.get_queryset()
        instance = self.get_object()
        instance.view_count += 1
        instance.save()
        serializer = CandidateDetailModelSerializer(instance)
        return Response(serializer.data)
    # def get_queryset(self):
    #     query = super().get_queryset()
    #     query.update(view_count=F('view_count') + 1)
    #     return query
