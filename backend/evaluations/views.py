from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Player, Evaluation, Weight
from .serializers import PlayerSerializer, EvaluationSerializer, WeightSerializer

# VIEWS DEFINE LOGIC FOR HANDLING HTTP REQUESTS (WHAT HAPPENS WHEN YOU GET, POST, DELETE DATA)
# VIEWSETS ARE A HIGHER-LEVEL ABSTRACTION OF VIEWS
# MODELVIEWSET AUTOMATICALLY LINKS THE DB MODELS WITH THE SERIALIZERS

class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def get_serializer_context(self):
        return {'request': self.request}

class EvaluationViewSet(ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

class WeightViewSet(ModelViewSet):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer

