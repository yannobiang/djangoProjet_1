
from http.client import HTTPResponse

#from django.http import 
from datetime import datetime
from django.shortcuts import render

def index(request):
    """ les filtres utilisables sur django docs.djangoproject.com 
        (django template filter)
    """

    date = datetime.today()
    print(date)
    return render(request, "DocBlog/index.html", context={"prenom":"patrick","date":date})