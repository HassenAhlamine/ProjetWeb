from django.shortcuts import redirect

def home(request):
    response = redirect('/cineseries/')
    return response
