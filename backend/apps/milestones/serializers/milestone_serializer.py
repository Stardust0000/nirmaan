from rest_framework import serializers
from apps.milestones.models import Milestone

class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = ['id','title','description','start_date','end_date']
        read_only_fields = ['id']

    def validate(self,attrs):
        if attrs['start_date'] > attrs['end_date']:
            raise serializers.ValidationError("End Date must be after Start Date.")
        return attrs
    
    def validate_title(self, title):
        if not title or not title.strip():
            raise serializers.ValidationError("Title cannot be empty")
        return title.strip()