from rest_framework import serializers
from shop.models import STATUS_CHOICES
from shop.models import Product


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    image = serializers.ImageField()
    cost = serializers.IntegerField()
    status = serializers.ChoiceField(
         choices=STATUS_CHOICES )


class ProductModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ["title", "image", "cost", "status"]