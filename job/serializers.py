##transform models to json format

from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):

    class Meta:

        model = Job
        fields = '__all__'