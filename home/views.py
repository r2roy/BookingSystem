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

class AboutView(BaseView):
    def get(self, request):
        self.views

        return render(request, 'about.html',self.views)

class BookingView(BaseView):
    def get(self, request):
        self.views

        return render(request, 'booking.html',self.views)

class MenuView(BaseView):
    def get(self, request):
        self.views

        return render(request, 'menu.html',self.views)

class TeamView(BaseView):
    def get(self, request):
        self.views

        return render(request, 'team.html',self.views)

class ServiceView(BaseView):
    def get(self, request):
        self.views

        return render(request, 'service.html',self.views)

class TestimonialView(BaseView):
    def get(self, request):
        self.views

        return render(request, 'testimonial.html',self.views)
class ContactView(BaseView):
    def get(self, request):
        self.views

        return render(request, 'contact.html',self.views)

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
                return redirect('/signup')
            elif User.objects.filter(email = email).exists():
                messages.error(request, "Email already in use!")
                return redirect('/signup')
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


def booking(request):
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
                return redirect('/signup')
            elif User.objects.filter(email = email).exists():
                messages.error(request, "Email already in use!")
                return redirect('/signup')
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
