from django.shortcuts import render
from .models import Topic

"""
Index view.
"""
def index(request):

    context = {
        'topics': Topic.objects.all()
    }

    return render(request, 'forum/index.html', context)

def login(request):
    return render(request, 'forum/login.html')