import logging
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    query = request.GET.get("query")

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        logger.info(first_name)

        last_name = request.POST.get("last_name")
        logger.info(last_name)

    return HttpResponse(f"Querry: {query}")