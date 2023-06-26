from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView


from .import serializers
from .models import Condidate, SavedCondidate


class CondidanteListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Condidate.objects.all()
    serializer_class = serializers.CondidateSerializers


class CondidateView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.CondidateSerializers

    def post(self, request, *args, **kwargs):
        user = self.request.user
        serializer = serializers.CondidateSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                "success": False,
                "message": "malumotlar to'ldirilmagan"
            }, status=403
            )
        if Condidate.objects.filter(condidate_user=user).exists():
            return Response({
                "success": False,
                "message": "Condidate already"
            })

        Condidate.objects.create(**serializer.data, condidate_user=user)
        return Response({"success": True})


class SavedView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.SavedCondidateSerializer

    def get_queryset(self):
        user = self.request.user
        return SavedCondidate.objects.filter(user=user)


class SavedDetailView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = SavedCondidate.objects.all()
    serializer_class = serializers.SavedCondidateSerializer


class RemoweFromSaveView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.SavedCondidateSerializer

    def get_queryset(self):
        user = self.request.user
        return SavedCondidate.objects.filter(user=user)
            