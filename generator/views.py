from django.shortcuts import render
from django.http import HttpResponse
import random
import string
# Create your views here.

def home(request):
	return render(request, 'generator/home.html')


def password(request):

	length = int(request.GET.get('length', 7))

	password = "".join(random.choice(string.ascii_lowercase) for x in range(length))

	if request.GET.get('uppercase'):
		password = "".join(random.choice(string.ascii_letters) for x in range(length))

	if request.GET.get('special'):
		password = "".join(random.choice(string.ascii_lowercase + string.punctuation) for x in range(length))

	if request.GET.get('numbers'):
		password = "".join(random.choice(string.ascii_lowercase + string.digits) for x in range(length))

	if request.GET.get('numbers') and request.GET.get('special') and request.GET.get('uppercase'):
		password = password = "".join(random.choice(string.ascii_letters + string.punctuation  + string.digits) for x in range(length))
	
	if request.GET.get('numbers') and request.GET.get('uppercase'):
		password = password = "".join(random.choice(string.ascii_letters + string.digits) for x in range(length))

	if request.GET.get('numbers') and request.GET.get('special'):
		password = password = "".join(random.choice(string.ascii_lowercase + string.digits + string.punctuation) for x in range(length))

	if request.GET.get('special') and request.GET.get('uppercase'):
		password = password = "".join(random.choice(string.ascii_letters + string.punctuation) for x in range(length))

	return render(request, 'generator/password.html', {'password': password })


def about(request):
	return render(request, 'generator/about.html')