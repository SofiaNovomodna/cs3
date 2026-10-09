from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse




def my_view(request):
    # View code here...
    return render(
        request,
        "main/index.html",

    )



def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully!")
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {
        "form": form
    })