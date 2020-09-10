from django.shortcuts import render,redirect,get_object_or_404
from sadmin.models import Contact,Category,Comment,Article,Author
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('user-home')
    else:
        if request.method == "POST":
            username = request.POST.get('user')
            password = request.POST.get('pass')
            auth = Author.objects.filter(username=username, password=password).exists()
            print('login auth', auth)
            if auth:
                statuscheck = Author.objects.filter(username=username, status=1).exists()
                if statuscheck:
                    request.session['author_username'] = username
                    return redirect('user-home')
                else:
                    messages.add_message(request, messages.INFO, 'Your account is not active! Contact Admin!')
            else:
                messages.add_message(request, messages.INFO, 'Username or password missmatch !!')
    return render(request, 'user_templates/login.html')

def user_logout(request):
    logout(request)
    return redirect('user_login')


def home(request):
    article_obj = Article.objects.all()
    category_obj = Category.objects.all()
    context={
        'article_obj': article_obj,
        'category_obj': category_obj
    }
    return render(request, 'user_templates/index.html', context)


def user_profile(request, username):

    return render(request, 'user_templates/profile.html')


def user_contact(request):

    return render(request, 'user_templates/contact.html')


def all_blog(request):

    return render(request, 'user_templates/all_blog')


def single_blog(request, id):
    single_article_obj = get_object_or_404(Article, id=id)
    context={
        'single_article_obj':single_article_obj
    }
    return render(request, 'user_templates/single_blog.html', context)


def single_category(request, name):
    return render(request, 'user_templates/single_category.html')


def create_blog(request):
    category_obj = Category.objects.all()
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        second_body_title = request.POST.get('second_body_title')
        second_body = request.POST.get('second_body')
        article_pic = request.POST.get('article_pic')
        category = request.POST.get('category')

        blog_obj = Article(title=title, body=body, second_body_title=second_body_title,
                           second_body=second_body, article_pic=article_pic, category=category)

        blog_obj.save()
        messages.success(request, 'New Article Create Successfully !!')
    context = {
        'category_obj': category_obj
    }
    return render(request, 'user_templates/create_blog.html', context)


def blog_list(request):
    return render(request, 'user_templates/blog_list.html')


def about(request):
    return render(request, 'user_templates/about.html')


def contact(request):
    return render(request, 'user_templates/contact.html')
