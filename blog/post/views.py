import logging

from django.http import HttpResponse
from django.shortcuts import render, redirect

from post.models import Post

from post.forms import RegistrationForm, AddPostForm

logger = logging.getLogger(__name__)


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


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            logger.info(form.cleaned_data)
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {"form": form})


# added function for templates - add.post.html
def add_post(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            #  logger.info(form.cleaned_data)
            # unpacking the dictionary and assigning values from the received data to the model
            # author=request.user - will be added automatically
            Post.objects.create(**form.cleaned_data, author=request.user)
            return redirect('post_index')

    else:
        form = AddPostForm()
    return render(request, 'add_post.html', {"form": form})












# def register_user(request):
#     if request.method == "POST":
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             # Process validated data
#             # form.cleaned_data["email"]
#             # form.cleaned_data["password"]
#             return redirect("/thanks/")
#     else:
#         form = RegisterForm()
#     return render(request, "register.html", {"form": form})

# def register(request):
#     form = RegistrationForm()
#     logger.info(request.POST)
#
#
#
#     return render(request, "register.html", {"form": form})




# def index(request):
#    return HttpResponse("Posts index view- Hello world")
