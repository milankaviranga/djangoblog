from django.shortcuts import render
from post.models import Catagory,Post
from post.forms import VisiterEmail
from django.views import View
from django.utils import timezone
# Create your views here.

# this is a catagory section

def index(request):
    webpage_post = Post.objects.order_by('date').reverse()[0:]
    my_post = {'all_post':webpage_post}
    return render(request,'allpost/post.html',context = my_post)

def java(request):
    webpage_post = Post.objects.order_by('date').reverse()[0:]
    my_post = {'java_post':webpage_post}
    return render(request,'catpost/javaonly/javaonly.html',context = my_post)

def pythons(request):
    webpage_post = Post.objects.order_by('date').reverse()[0:]
    my_post = {'python_post':webpage_post}
    return render(request,'catpost/pythononly/python.html',context = my_post)

def tests(request):
    webpage_post = Post.objects.order_by('date').reverse()[0:]
    my_post = {'test_post':webpage_post}
    return render(request,'allpost/test.html',context = my_post)

# this is a form section


def formes(request):
    form = VisiterEmail()
    if request.method == 'POST':
        form = VisiterEmail(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('this is a wrong')
    return render(request,'userform/visiterform.html',context={'form':form})

# social media section



# this is a full form section

