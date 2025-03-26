from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Declaring a class BlogPost with two attributes: title and content
class BlogPost:
    def __init__(self, title, content):
        self.title = title
        self.content = content

#Creating a list of BlogPost objects
blog_posts = [
    BlogPost('First Post', 'This is my first blog post.'),
    BlogPost('Second Post', 'This is my second blog post.'),
    BlogPost('Third Post', 'This is my third blog post.'),
]

#Creating a function index that returns the index.html template
def index(request):
    return render(request, 'blog/index.html', {'blog_posts': blog_posts})
        

def blog_detail(request, slug):
    return render(request,'blog/blog_post.html',{'blog_title':slug})

