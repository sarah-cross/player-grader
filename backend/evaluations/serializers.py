from rest_framework import serializers
from .models import Player, Evaluation, Weight

# SERIALIZERS HANDLE CONVERSION BETWEEN MODELS AND JSON

class PlayerSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = '__all__'

    def get_image(self, obj):
        print("Image URL:", obj.image.url)  
        request = self.context.get('request')
        if obj.image and request:
            # Ensure you are using `obj.image.url` and not manually appending MEDIA_URL
            return request.build_absolute_uri(obj.image.url)
        return None



class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'

class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = '__all__'
