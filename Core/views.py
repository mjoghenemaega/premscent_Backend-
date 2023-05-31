from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, ProfileForm

# Create your views here.
def home(request):

  return render(request, 'index.html')   

# def register(request):

#   return render(request, 'register.html')  

def employer(request):

  return render(request, 'employer_signup.html')  
 
def freelancer(request):

  return render(request, 'freelancer_signup.html')  


def login(request):

  return render(request, 'freelancer_signup.html')  










def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()
    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})
