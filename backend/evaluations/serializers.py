from rest_framework import serializers
from .models import Player, Evaluation, Weight

# SERIALIZERS HANDLE CONVERSION BETWEEN MODELS AND JSON

class PlayerSerializer(serializers.ModelSerializer):
   # image = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = '__all__'



class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'

class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = '__all__'
