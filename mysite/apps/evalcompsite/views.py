from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from evalcompsite.models import Application, Apartment, House, Land, Comment


# Create your views here.
def home (request):
	comments_list = Comment.objects.order_by('-id')[:10]
	return render(request, 'home.html', {'comments_list' : comments_list})

def requestpage (request):
	return render(request, 'request.html')

def price (request):
	apartments = Apartment.objects.all()
	houses = House.objects.all()
	land_plot = Land.objects.all()
	context = {
		"apartments": apartments,
		"houses": houses,
		"land_plot": land_plot
	}
	return render(request, 'price.html', context)

def about (request):
	return render(request, 'about.html')

def createrequest(request):
	if request.method == "POST":
		app = Application()
		app.last_name = request.POST.get("last_name")
		app.first_name = request.POST.get("first_name")
		app.patronymic = request.POST.get("patronymic")
		app.email = request.POST.get("email")
		app.phone_number = request.POST.get("phone_number")
		app.eval_object = request.POST.get("eval_object")
		app.aim = request.POST.get("aim")
		app.address = request.POST.get("address")
		app.price = request.POST.get("price")
		app.comment = request.POST.get("comment")	
		app.save()
	return HttpResponseRedirect(reverse('evalcompsite:requestpage'))

def createcomment(request):
	if request.method == "POST":
		app = Comment()
		app.name = request.POST.get("name")
		app.comment = request.POST.get("comment")
		app.save()
	return HttpResponseRedirect(reverse('evalcompsite:home'))
