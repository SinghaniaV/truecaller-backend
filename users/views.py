from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.db import IntegrityError
from django.urls import reverse
from django.http import HttpResponseRedirect
from identities.models import Identity, Registered, RegisteredToSaved
from .forms import UserRegisterForm, AddToGlobalForm, SearchForm


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")


def register_view(request):  # Redirect to login page after successful registration
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('username')

            Registered.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
            )

            return render(request, "users/login.html", {
                "message": "Account Created."
            })
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def form_view(request):
    if request.method == 'POST':
        form = AddToGlobalForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            is_spam = form.cleaned_data.get('mark_spam')

            try:
                Identity.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    is_spam=is_spam
                )

            except IntegrityError:
                return render(request, "users/add.html", {
                "message": "Duplicate Entry NOT Allowed.",
                "form": form
            })
            
            registered_user = Registered.objects.get(pk=request.user.username)
            contact_saved = Identity.objects.get(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                is_spam=is_spam
            )

            RegisteredToSaved.objects.create(
                phone=registered_user,
                contact_saved=contact_saved
            )
            
            return render(request, "users/add.html", {
                "message": f"Marked {phone} as Spam! by user {request.user.username}",
                "form": form
            })
    else:
        form = AddToGlobalForm()
    return render(request, 'users/add.html', {'form': form})


def search_users(request):
    form = SearchForm(request.GET or None)
    identity = Identity.objects.all()
    registered_users = Registered.objects.all()
    registered_to_saved = Registered.objects.all() 
    
        # TODO: the person’s email is only displayed if the person is a registered user and the user who is searching is in the person’s contact list. We have to search registered_to_saved for this.

    if form.is_valid():
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        phone = form.cleaned_data.get('phone')

        if phone:
            users = registered_users.filter(phone__icontains=phone)
            if users:
                return render(request, 'users/search_users.html', {
                'form': form,
                'users': users
            })

            else:
                users = identity.filter(first_name__icontains=first_name)
                return render(request, 'users/search_users.html', {
                    'form': form,
                    'users': users
                })
            
        if first_name:
            users = identity.filter(first_name__icontains=first_name)
            return render(request, 'users/search_users.html', {
                    'form': form,
                    'users': users
                })

        if last_name:
            users = identity.filter(last_name__icontains=last_name)
            return render(request, 'users/search_users.html', {
                    'form': form,
                    'users': users
                })


    return render(request, 'users/search_users.html', {
        'form': form,
    })


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid Credentials."
            })
    else:
        return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out."
    })
