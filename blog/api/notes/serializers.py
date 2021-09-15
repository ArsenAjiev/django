from rest_framework import serializers

from notes.models import Notes


class NotesSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    created_at = serializers.DateTimeField(read_only=True)


class NoteModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notes
        fields = ["title", "created_at"]

