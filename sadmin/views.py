from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from.models import Author,Contact,Comment,Category,Article
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator


# Create your views here.

def getlogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(username=username, password=password)
            if auth is not None:
                login(request, auth)
                if request.user.is_superuser:
                    return redirect('home')
                else:
                    return redirect('user-home')
            else:
                messages.add_message(request, messages.INFO, 'Username or password missmatch !!')
    return render(request, 'sadmin_templates/login.html')


def getlogout(request):
    logout(request)
    return redirect('login')


def admin_home(request):
    author_obj = Author.objects.all().count()
    blog_obj = Article.objects.all().count()
    contact_obj = Contact.objects.all().count()
    article_obj = Article.objects.all()
    context={
        'article_obj':article_obj,
        'author_obj':author_obj,
        'blog_obj':blog_obj,
        'contact_obj':contact_obj
    }
    return render(request, 'sadmin_templates/index.html', context)


def add_users(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        country = request.POST.get('country')
        division = request.POST.get('division')
        present_adress = request.POST.get('present_adress')
        parmanent_adress = request.POST.get('parmanent_adress')
        designation = request.POST.get('designation')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        blog_user = Author(first_name=fname,last_name=lname,username=uname, email=email, phone=phone, password=password,
                             present_address=present_adress,country=country, permanent_address=parmanent_adress, designation=designation,
                             division=division)
        user = Author.objects.all().filter(username=uname)
        if user:
            messages.warning(request, "User is Already Exist")

        else:
            blog_user.save()

            messages.success(request, 'User Created successfully')
    context = {
        'isact_registersurveyor': 'active',

    }
    return render(request, 'sadmin_templates/user/register_user.html', context)

def user_list(request, filter):
    surveyor = None
    if filter == 'None':
        surveyor = Author.objects.all()[::-1]
    elif filter == 'active':
        surveyor = Author.objects.filter(status=1)[::-1]
    elif filter == 'inactive':
        surveyor = Author.objects.filter(status=0)[::-1]
    paginator = Paginator(surveyor, 25)
    page = request.GET.get('page', )
    all_survey = paginator.get_page(page)
    context = {
        "surveyor": all_survey,
        'isact_surveyorlist': 'active',
    }
    return render(request, 'sadmin_templates/user/user_list.html', context)


def view_user(request, id):
    single_surveyor = get_object_or_404(Author, id=id)
    context={
        "single_surveyor":single_surveyor,
        'isact_surveyorlist': 'active',

    }
    return render(request, 'sadmin_templates/user/view_user.html', context)


def update_user(request, username):
    s_user = Author.objects.get(username=username)
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        country = request.POST.get('country')
        division = request.POST.get('division')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')
        designation = request.POST.get('designation')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        status = request.POST.get('status')
        update_user = Author.objects.filter(username=username) \
            .update(first_name=fname, last_name=lname, username=username, email=email, phone=phone,
                             password=password, present_address=present_address, country=country, permanent_address=permanent_address,
                             designation=designation, division=division,status=status)
        messages.success(request, 'User Profile Update Successfully')
        return redirect('user_update',username=username)
    context = {
        's_user': s_user
    }
    return render(request,'sadmin_templates/user/user_update.html',context)

def user_delete(request, id):
    user = get_object_or_404(Author, id=id)
    user.delete()
    messages.warning(request, 'Profile Delete successfully !!')
    return redirect('user_list', filter=None)


def all_blog(request):
    article_obj = Article.objects.all()
    context = {
        'article': article_obj
    }
    return render(request, 'sadmin_templates/blog/blog_list.html', context)


def contacts_list(request):
    contact_obj = Contact.objects.all()
    context={
        "contact_obj":contact_obj
    }
    return render(request, 'sadmin_templates/contact/contact_list.html', context)


def view_contact(request, id):
    contact_obj = get_object_or_404(Contact, id=id)
    context = {
        'contact_obj': contact_obj
    }
    return render(request, 'sadmin_templates/contact/view_contact.html', context)

def delete_contact(request, id):
    contact_obj = get_object_or_404(Contact, id=id)
    contact_obj.delete()
    return redirect('contact_list')


def add_new_blog(request):
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        second_body_title = request.POST.get('second_body_title')
        second_body = request.POST.get('second_body')
        article_pic = request.POST.get('article_pic')
        category = request.POST.get('category')
        article_author = request.POST.get('article_author')
        blog_obj = Article(title=title, body=body, second_body_title=second_body_title,second_body=second_body,
                           article_pic=article_pic, category=category,article_author=article_author)
        blog_obj.save()
        messages.success(request, 'New Article Create Successfully !!')
    return render(request, 'sadmin_templates/blog/create_blog.html')


def view_blog(request, id):
    article_obj = get_object_or_404(Article, id=id)
    context={
       "article_obj":article_obj
    }
    return render(request, 'sadmin_templates/blog/view_blog.html', context)


def update_blog(request, id):
    article_obj = get_object_or_404(Article, id=id)
    if request.method == "POST":
        article_obj.title = request.POST.get('title')
        article_obj.body = request.POST.get('body')
        article_obj.second_body_title = request.POST.get('second_body_title')
        article_obj.second_body = request.POST.get('second_body')
        article_obj.article_pic = request.POST.get('article_pic')
        article_obj.category = request.POST.get('category')
        article_obj.save()
    context = {
       "article_obj":article_obj
    }
    return render(request, 'sadmin_templates/blog/update_blog.html', context)


def delete_blog(request, id):
    article_obj = get_object_or_404(Article, id=id)
    article_obj.delete()
    return redirect('blog_list')

