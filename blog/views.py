from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Raja',
        'title':'Ponniyin Selvan',
        'content': 'First content',
        'date_posted':'May 23  2021'
    },
    {
        'author': 'Tinku',
        'title':'AAthichudi',
        'content': 'Second content',
        'date_posted':'May 24 2021'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request,'blog/home.html', context)
def about(request):
    return render(request,'blog/about.html', {'title':'About'})
