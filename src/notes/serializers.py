from rest_framework import serializers
from . import models


class NotesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Notes
        exclude = ['content', 'updated_at',]


class NotesDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Notes
        fields = '__all__'


class NotesCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Notes
        fields = '__all__'
