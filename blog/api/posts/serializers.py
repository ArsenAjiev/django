from rest_framework import serializers

from post.models import Post


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    image = serializers.ImageField()
    text = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)


class PostModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "image", "text", "created_at"]