# from django.contrib import messages
from django.shortcuts import  render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import UpdateView, DetailView, ListView
from django.contrib.auth import login, authenticate, logout

from .models import User
from .forms import (
	UserRegisterForm, AuthenticationForm, 
	UpdateUserForm)

class UserDetailView(ListView):
	model = User
	template_name = 'user/user_detail.html'
	context_object_name = 'user'
	

	def get_queryset(self,):
		try:
			user = User.objects.get(pk=self.request.user.pk)
			return user
		except: 
			return []

	
class UserUpdateView(UpdateView):
	model = User
	form_class = UpdateUserForm
	context_object_name = 'user'
	template_name = 'user/user_update.html'
	success_url = '/authsystem/user/'

	def get_object(self):
		return self.request.user 

###			Authentication Functional
def user_login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(email=email, password=password)
			print(user)
			if user is not None:
				login(request, user)
				# messages.info(request, f"You are now logged in as {email}.")
				print('logged in')
				return redirect("home")
			else:
				# messages.error(request,"Invalid username or password.")
				print('invalid') 
		else:
			# messages.error(request,"Invalid username or password.")
			print('invalid')
	form = AuthenticationForm()
	return render(request=request, template_name="user/login.html", context={"login_form":form})

def user_logout(request):
	logout(request)
	# messages.info(request, "You have successfully logged out.") 
	return redirect("login")

# mytestp4ssword