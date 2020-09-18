from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from sadmin.models import Contact,Category,Comment,Article,Author
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import pdb;

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


def user_profile(request):
    author_obj = get_object_or_404(Author, username=request.session['author_username'])
    context ={
        'author_obj': author_obj
    }
    return render(request, 'user_templates/profile.html', context)


def profile_edit(request, user_id):
    author_obj = get_object_or_404(Author, id=user_id)
    if request.method == "POST":
        author_obj.first_name = request.POST.get('first_name')
        author_obj.last_name = request.POST.get('last_name')
        author_obj.username = request.POST.get('username')
        author_obj.email = request.POST.get('email')
        author_obj.phone = request.POST.get('phone')
        author_obj.password = request.POST.get('password')
        author_obj.country = request.POST.get('country')
        author_obj.division = request.POST.get('division')
        author_obj.present_address = request.POST.get('present_address')
        author_obj.permanent_address = request.POST.get('permanent_address')
        author_obj.designation = request.POST.get('designation')
        author_obj.save()
        messages.success(request, 'User Profile Update Successfully')
    context = {
        'author_obj': author_obj
    }
    return render(request, 'user_templates/update_profile.html', context)


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
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        second_body_title = request.POST.get('second_body_title')
        second_body = request.POST.get('second_body')
        article_pic = request.POST.get('article_pic')
        category = request.POST.get('category')
        article_author = request.POST.get('article_author')
        blog_obj = Article(title=title, body=body, second_body_title=second_body_title,
                           second_body=second_body,article_pic=article_pic, category=category,
                           article_author=article_author)
        blog_obj.save()
        messages.success(request, 'New Article Create Successfully !!')
    return render(request, 'user_templates/create_blog.html')


def blog_remove(request, id):
    article_obj = Article.objects.get(id=id)
    article_obj.delete()
    return HttpResponseRedirect('/')


def blog_list(request, user_id):
    author_obj = get_object_or_404(Author, id=user_id)
    article_obj = Article.objects.filter(article_author=author_obj.id)
    context = {
        'article': article_obj
    }
    return render(request, 'user_templates/blog_list.html', context)


def about(request):
    return render(request, 'user_templates/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact_obj = Contact(name=name, email=email, message=message)
        contact_obj.save()
        messages.success(request, 'Your Message send to Admin !!')
    return render(request, 'user_templates/contact.html')

