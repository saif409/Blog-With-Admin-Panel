from django.shortcuts import render,redirect
from sadmin.models import Contact,Category,Comment,Article,Author
from django.contrib import messages

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('user')
            password = request.POST.get('pass')
            auth = Author.objects.filter(username=username, password=password).exists()
            print('login auth', auth)
            if auth:
                statuscheck = Author.objects.filter(username=username, status=1).exists()
                if statuscheck:
                    request.session['agent_username'] = username
                    return redirect('agentshome')
                else:
                    messages.add_message(request, messages.INFO, 'Your account is not active! Contact Admin!')

            else:
                messages.add_message(request, messages.INFO, 'Username or password missmatch !!')

    return render(request, 'user_templates/login.html')


def home(request):
    if request.user.is_authenticated:
        return redirect('user-home')
    else:
        return redirect('login')

    return render(request, 'user_templates/index.html')

def user_contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        get_contact = Contact(name=name, email=email, message=message)
        get_contact.save()
        messages.success(request, 'User Profile Update Successfully')
    return render(request, 'user_templates/contact.html')
