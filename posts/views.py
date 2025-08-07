from django.shortcuts import render

# Create your views here.
blog_posts = [
    {
        'id': 1,
        'title': 'test post 1',
        'content': 'test content1 hello world'
    },
    {
        'id': 2,
        'title': 'Django is best Framework',
        'content': 'test content2 hello world'
    },
    {
        'id': 3,
        'title': 'Python is best programmin language',
        'content': 'test content3 hello world'
    },
]


def post_list(request):
    return render(request, 'posts/post_list.html', {'posts': blog_posts})

