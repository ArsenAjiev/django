from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


from post.models import Post


def index(request):
    title = request.GET.get("title")
    post_list = Post.objects.filter(title__contains=title)
    post_ids = [post.id for post in post_list]
    return HttpResponse(", ".join(post_ids))



# def index(request):
#    return HttpResponse("Posts index view- Hello world")
