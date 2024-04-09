from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import GraphicDesign
from .forms import UIUXUpdateForm
from .forms import ImageForm


def home(request):


    #return HttpResponse('hello world')

    return render(request, 'MyPortfolio/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_page = request.POST.get('next', '')  # Get the value of 'next' parameter
            if next_page:  # If 'next' parameter exists, redirect to it
                return redirect(next_page)
            else:  # Otherwise, redirect to a default page
                return render(request, 'MyPortfolio/admin.html')
        else:
            # Add a Bootstrap alert indicating wrong password
            messages.error(request, 'Wrong password. Please try again.')
    return render(request, 'MyPortfolio/admin.html')

def user_view(request):
    images = GraphicDesign.objects.all()
    return render(request, 'MyPortfolio/admin.html', {'images': images})

def add_project(request):
    if request.POST:
        form = ImageForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()

    return render(request, 'MyPortfolio/addproject.html',context={'form' : ImageForm})

def delete_project(request, id):
    project = GraphicDesign.objects.get(id=id)

    if request.method == "POST" and "confirm_delete" in request.POST:
        project.delete()
        return redirect('PORTFOLIO:user')

    return render(request, 'MyPortfolio/deleteproject.html', {'project': project})

def update_project(request, id):
    image = GraphicDesign.objects.get(id=id)  # Fetch a single Uiux object based on id
    if request.method == "POST":
        form = UIUXUpdateForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('PORTFOLIO:user')
    else:
        form = UIUXUpdateForm(instance=image)
    return render(request, 'MyPortfolio/updateproject.html', {'form': form, 'image': image})

def custom_logout(request):
    logout(request)
    # Redirect to a desired page after logout
    return redirect('PORTFOLIO:home')  # Replace 'home' with the name of your desired URL pattern