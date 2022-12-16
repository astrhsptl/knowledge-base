# from django.contrib import messages
from django.shortcuts import  render, redirect
from django.views.generic import UpdateView, DetailView
from django.contrib.auth import login

from authsystem.models import User
from .forms import (
	UserRegisterForm, UpdateUserForm)
# Create your views here.

class ModeratorUserDetailView(DetailView):
    model = User
    template_name = 'user/user_detail.html'
    context_object_name = 'user'

class ModeratorUserUpdateView(UpdateView):
	model = User
	form_class = UpdateUserForm
	context_object_name = 'user'
	template_name = 'user/user_update.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		print(context)
		return context

def user_register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			# messages.success(request, "Registration successful." )
			print("Registration successful.")
			return redirect("home")
		# messages.error(request, "Unsuccessful registration. Invalid information.")
		print('Unsuccessful registration.')
	form = UserRegisterForm()
	return render (request=request, template_name="user/register.html", context={"register_form":form})