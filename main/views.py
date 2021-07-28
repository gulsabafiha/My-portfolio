from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request,'main/base.html')

def about(request):
    return render(request,'main/about.html')

def service(request):
    return render(request,'main/service.html')

    
def portfolio(request):
    return render(request,'main/portfolio.html')

def contact(request):
    if request.method == 'POST':
        form= ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form=ContactForm()
    else:
        form=ContactForm()
    return render (request,'main/contact.html',{'form':form})
    