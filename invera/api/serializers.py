from rest_framework import serializers
from task.models import InveraTask
import datetime


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = InveraTask
        fields = '__all__'

