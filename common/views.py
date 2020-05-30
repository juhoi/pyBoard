from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from common.forms import UserForm


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


def bad_request_page(request, exception):
    response = render(request, 'common/400.html', {})

    response.status_code = 400
    return response


def page_not_found_page(request, exception):
    response = render(request, 'common/404.html', {})

    response.status_code = 404
    return response


def server_error_page(request):
    response = render(request, 'common/500.html', {})

    response.status_code = 500
    return response
