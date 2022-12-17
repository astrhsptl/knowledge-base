# from django.contrib import messages
import os
from django.contrib.auth import login
from django.shortcuts import  render, redirect
from django.views.generic import UpdateView, DetailView, CreateView

from authsystem.models import User
from incommonpanel.models import Document, Catalog
from .forms import (
	UserRegisterForm, UpdateUserForm,
	DocumentCreationalForm, CatalogCreationalForm)

from buisneslogic.send_email import mail_sending
from buisneslogic.tasks import mail_sending_task

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

class DocumentCreationsView(CreateView):
	model = Document
	form_class = DocumentCreationalForm
	context_object_name = 'form'
	template_name = 'incommon_templates/document/document_create.html'

class CatalogCreationalView(CreateView):
	model = Catalog
	form_class = CatalogCreationalForm
	context_object_name = 'form'
	template_name = 'incommon_templates/catalog/catalog_create.html'


def user_register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			
			# login(request, user)
			# messages.success(request, "Registration successful." )
			try:
				mail_sending_task.delay(form.cleaned_data['email'], form.cleaned_data['password1'])
			except:
				print('invalid recipier')
			return redirect("home")
		# messages.error(request, "Unsuccessful registration. Invalid information.")
		print('Unsuccessful registration.')
	form = UserRegisterForm()
	return render (request=request, template_name="user/register.html", context={"register_form":form})