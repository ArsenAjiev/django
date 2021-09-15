from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import logging

from django.http import HttpResponse
from django.shortcuts import render, redirect

from notes.models import Notes

from post.forms import RegistrationForm, AddPostForm


def index2(request):
    title = Notes.objects.all()
    post_titles = [notes.title for notes in title]
    return HttpResponse(", ".join(post_titles))





