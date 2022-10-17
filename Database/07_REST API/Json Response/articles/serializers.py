from rest_framework import serializers
from .models import Article

# serialize 과정
class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
