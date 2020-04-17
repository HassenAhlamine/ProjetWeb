from django.shortcuts import render
from .models import Cinema, Film

def home(request):
    return render(request, 'index.html', {})

def cinemas(request):
    cinemas = Cinema.objects.all()
    return render(request, 'cinemas.html', {'cinemas': cinemas})

def cinema(request, id_cinema):
    cinema = Cinema.objects.get(id=id_cinema)
    return render(request, 'cinema.html', {'cinema': cinema})

def films(request):
    films = Film.objects.all()
    return render(request, 'films.html', {'films': films})

def film(request, id_film):
    film = Film.objects.get(id=id_film)
    return render(request, 'film.html', {'film': film})


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from cineseries.forms import UserForm,UserProfileInfoForm

def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Compte inactif.")
        else:
            print("Tentative de login échoué.")
            print("Informations utilisées: login {} / password: {}".format(username,password))
            return HttpResponse("Informations d'authentification invalides")
    else:
        return render(request, 'login.html', {})

def enregistrement(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'avatar' in request.FILES:
                #print('found it')
                profile.avatar = request.FILES['avatar']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'enregistrement.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered
                           })

@login_required
def deconnexion(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def compte(request):
    return render(request, 'compte.html', {})

@login_required
def like(request, uid, toLike):
    if (toLike=='film'):
        film = Film.objects.get(id=uid)
    if (toLike=='cinema'):
        cinema = Cinema.objects.get(id=uid)
    user = request.user

    if (hasattr(user, 'user_profile')):
        userProfile = user.user_profile
        if (toLike=='film'):
            userProfile.films.add(film)
        if (toLike=='cinema'):
            userProfile.cinemas.add(cinema)

    return HttpResponseRedirect(reverse(toLike, args=[uid]))

@login_required
def unlike(request, uid, toLike):
    if (toLike=='film'):
        film = Film.objects.get(id=uid)
    if (toLike=='cinema'):
        cinema = Cinema.objects.get(id=uid)

    user = request.user

    if (hasattr(user, 'user_profile')):
        userProfile = user.user_profile
        if (toLike=='film'):
            userProfile.films.remove(film)
        if (toLike=='cinema'):
            userProfile.cinemas.remove(cinema)

    return HttpResponseRedirect(reverse(toLike, args=[uid]))
