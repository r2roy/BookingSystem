from django.views import View
from django.shortcuts import render
from .models import *

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




