# api/urls.py

from django.urls import include, path
from rest_framework import routers
from api.posts.views import PostViewSet
from api.notes.views import NotesViewSet
from api.products.views import ProductViewSet
from api.users.views import RegisterView




app_name = "api"

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"notes", NotesViewSet)
router.register(r"products", ProductViewSet)
router.register(r"register", RegisterView, basename='register')



urlpatterns = [
    path("", include(router.urls)),

]
