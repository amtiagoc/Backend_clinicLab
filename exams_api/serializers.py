from rest_framework import serializers
from crud_exams.models import Exams

class ExamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exams
        fields = ('id', 'title', 'username', 'notes', 'created_at')






