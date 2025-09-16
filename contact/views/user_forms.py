from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso')
            return redirect('contact:login')

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )

@login_required(login_url='contact:login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method == "POST":
        form = RegisterUpdateForm(data=request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            login(request, request.user)  # New Login
            messages.success(request, "Atualizado com sucesso.")
            return redirect("contact:user_update")

    return render(
        request,
        "contact/user_update.html",
        {
            "site_title": "Update User - ",
            "form": form,
        },
    )


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login realizado com sucesso')
            return redirect('contact:index')
        else:
            messages.error(request, 'Login inválido')

    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }
    )

@login_required(login_url='contact:login')
def logout_view(request):
    logout(request)
    return redirect('contact:login')
