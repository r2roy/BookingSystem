from django.views import View
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from datetime import datetime
from django.conf import settings

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


def contact(request):
    if request.method == "POST":
        yname = request.POST['yname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # Compose the email content
        email_subject = f"Contact Form Submission: {subject}"
        email_message = f"Name: {yname}\nEmail: {email}\nMessage:\n{message}"

        # Send the email
        send_mail(
            email_subject,  # Subject of the email
            email_message,  # Message content
            settings.EMAIL_HOST_USER,  # From email (your configured email)
            ['prashantrai557@gmail.com', 'prashantrai5666@gmail.com'],  # Recipient email(s)
            fail_silently=False,
        )

        return render(request, 'contact.html',{'yname':yname})

    else:

        return render(request, 'contact.html',{})



def sucess(request):
    if request.method == "POST":
        yname = request.POST['yname']
        email = request.POST['email']
        date = request.POST['date']
        option = request.POST['option']
        text = request.POST['text']

        date = datetime.strptime(date, '%m/%d/%Y %I:%M %p')

        booking = Booking(
            name=yname,
            email=email,
            date=date,
            number_of_people=option,
            special_request=text
        )
        booking.save()

        # Send an email notification
        send_mail(
            subject='Booking Request Received',
            message=f'New booking request:\n\n'
                    f'Name: {yname}\n'
                    f'Email: {email}\n'
                    f'Date: {date.strftime("%Y-%m-%d %H:%M:%S")}\n'
                    f'Number of People: {option}\n'
                    f'Special Request: {text}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['your-email@example.com'],  # Replace with the email where you want to receive notifications
            fail_silently=False,
        )

        return render(request, 'sucess.html',
                      {'yname': yname,
                       'email' : email,
                       'date' : date,
                       'option': option,
                       'text' : text},
                      )
    else:

        return render(request, 'booking.html',{})


