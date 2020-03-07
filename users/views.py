from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.s


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(
                request, 'Account created for {}!'.format(username))
            return redirect('blog-home')
    else:
        form = UserCreationForm()

    form = {'form': form}

    return render(request, 'users/register.html', form)
