from rest_framework.serializers import ModelSerializer
from anketa.models import Candidate


class CandidateSerializer(ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('year', 'address', 'married')


class CandidateDetailModelSerializer(ModelSerializer):
    class Meta:
        model = Candidate
        fields = (
            'year', 'address', 'nation', 'height', 'weight', 'health', 'married', 'prayed', 'desires', 'created_at',
            'view_count')
