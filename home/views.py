from django.views import View
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
class BaseView(View):
    views = {}
    views['services'] = Services.objects.all()
    views['menu'] = Menu.objects.all()
    views['product'] = Product.objects.all()
    views['chef'] = Chef.objects.all()
    views['feedback'] = Feedback.objects.all()


class HomeView(BaseView):
    def get(self, request):
        self.views

        return render(request, 'index.html',self.views)


def signup(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.error(request, "Username already exists!")
                return redirect('/sighup')
            elif User.objects.filter(email = email).exists():
                messages.error(request, "Email already in use!")
                return redirect('/sighup')
            else:
                User.objects.create_user(
                    first_name = fname,
                    last_name = lname,
                    username = username,
                    email = email,
                    password = password
                ).save()
        else:
            messages.error(request, "Password does not match!")
            return redirect('/signup')
    return render(request,'signup.html')
