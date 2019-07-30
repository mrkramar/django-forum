from django.shortcuts import render

def index(request):

    topics = [
        {
            'title': 'Cars',
            'description': 'Discuss about your favorite cars here.'
        },
        {
            'title': 'Design',
            'description': 'Post your ideas.'
        }
    ]

    context = {
        'topics': topics
    }

    return render(request, 'forum/index.html', context)
