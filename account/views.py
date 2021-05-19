from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
def loginform(request):
	return render(request,'account/login.html')
def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		User = authenticate(username=username,password=password)
		if User is not None:
			login(request,User)
			print("userlogin")
			return redirect('quiz_index')
		else:
			print("no such user")
			messages.info(request,'incorect username and password')
			return redirect('loginform')
	else:
		return redirect('loginform')

def signout_user(request):
	logout(request)
	return redirect('loginform') 