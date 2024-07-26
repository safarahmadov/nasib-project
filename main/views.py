from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm

# Create your views here.
def about(request):
    return render(request, 'about.html')

def BlogSingle(request):
    return render(request, 'blog-single.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Comment

def CourseSingle(request, id):
    post = get_object_or_404(Course, id=id)
    new_comment = None

    if request.method == "POST":
        message_text = request.POST.get("message")
        name_text = request.POST.get("name")
        email_text = request.POST.get("email")
        
        if message_text and name_text and email_text:
            new_comment = Comment(blog=post, message=message_text, name=name_text, email=email_text)
            new_comment.save()
            return redirect("course-single", id=id)
    return render(request, 'course-single.html', {
        "post": post,
        "new_comments": post.comments.all() })


#category , course, blog
def index(request):
    category = Category.objects.all()
    course = Course.objects.all()
    blog = Blog.objects.all()
    context={
        "category":category,
        "course":course,
        "blog":blog
    }
    return render(request, 'index.html', context=context)

def course(request):
    return render(request, 'course.html')


def SearchNone(request):
    return render(request, 'search-none.html')

def SearchPage(request):
    return render(request, 'search-page.html')


    
    