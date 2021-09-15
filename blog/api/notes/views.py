from rest_framework import viewsets


from api.notes.serializers import NotesSerializer

from notes.models import Notes


class NotesViewSet(viewsets.ModelViewSet):
   """
   API endpoint that allows posts to be viewed.
   """

   queryset =Notes.objects.all().order_by("-created_at")
   serializer_class = NotesSerializer
   permission_classes = []

















# class Notes(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     created_at = models.DateTimeField(
#         auto_now_add=True, db_index=True