from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from.models import Author,Contact,Comment,Category,Article
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator


# Create your views here.

def admin_home(request):
    total_survey_create = Author.objects.all().count()
    context={

    }
    return render(request, 'sadmin_templates/admin_home.html',context)
def admin_home(request):
    return render(request, 'sadmin_templates/index.html')

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
    context={
        's_user': s_user
    }
    return render(request,'sadmin_templates/user/user_update.html',context)

def user_delete(request, pid):
    user = get_object_or_404(Author, id=pid)
    user.delete()
    messages.warning(request, 'Profile Delete successfully !!')
    return redirect('user_list', filter=None)

def all_blog(request):
    return render(request, 'sadmin_templates/blog/blog_list.html')

def contacts_list(request):
    get_message = Contact.objects.all()
    context={
        "get_message":get_message
    }
    return render(request, 'sadmin_templates/contact/contact_list.html', context)