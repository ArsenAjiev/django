from django.http import HttpResponse

from post.models import Post


def index(request):
    slug = request.GET.get("slug")

    if request.user.is_authenticated:
          post_list = Post.objects.filter(author=request.user)
    else:
        post_list = Post.objects.all()

    if slug is not None:
        post_list = post_list.filter(slug__contains=slug)

    post_titles = [post.slug for post in post_list]
    return HttpResponse(", ".join(post_titles))



# def index(request):
#    return HttpResponse("Posts index view- Hello world")
