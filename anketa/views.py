from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import Response, APIView
from rest_framework import status
from anketa.serializers import SavedCandidateSerializer
from anketa.models import Candidate, Saved
from anketa.permissions import IsAuthorOrReadOnly
from anketa.serializers import CandidateDetailModelSerializer, CandidateSerializer


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


class SavedCandidatesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, req, *args, **kwargs):
        saved = Saved.objects.filter(author=req.user)
        serializer = SavedCandidateSerializer(saved, many=True)

        return Response(serializer.data)

    def post(self, req, *args, **kwargs):
        req.data.pop('id', None)

        saved = Saved.objects.filter(**req.data)
        if saved:
            saved.delete()

            return Response({'detail': 'deleted'}, status=status.HTTP_204_NO_CONTENT)

        serializer = SavedCandidateSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
