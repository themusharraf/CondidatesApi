from rest_framework import serializers

from .models import User, Condidate


class CondidateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Condidate
        fields = (
            # 'condidate_user',
            'condidate_name', 
            'condidate_age', 
            'condidate_height', 
            'condidate_weight', 
            'condidate_health',
            'condidate_address',
            'condidate_profession',
            'condidate_nation',
            'condidate_married',
            'condidate_prayed',
            'condidate_desires'
        )
    
    def create(self, validated_data):
        condidate = Condidate.objects.create(**validated_data,condidate_user_id=1)
        return condidate