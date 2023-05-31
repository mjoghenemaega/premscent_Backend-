from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import login


# Create your views here.
def home(request):

  return render(request, 'index.html')   

# def register(request):

#   return render(request, 'register.html')  

def employer(request):

  return render(request, 'employer_signup.html')  
 
def freelancer(request):

  return render(request, 'freelancer_signup.html')  


# def login(request):

#   return render(request, 'freelancer_signup.html')  




class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user =True
    
    def get_success_url(self):
        return reverse_lazy('home')    



class register(FormView):
    template_name= 'register.html'
    fields = '__all__'
    form_class = CustomUserCreationForm
    redirect_authenticated_user =True
    success_url = reverse_lazy('freelancer')
  
   
    def form_valid(self, form ):
        user =form.save()
        num_fields = len(form.fields)
        print(num_fields)
        if user is not None:
            login(self.request, user) 
        return super(register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('freelancer')
        return super(register, self).get(*args, **kwargs)
