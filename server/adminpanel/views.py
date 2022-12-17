from django.contrib import messages
from django.shortcuts import  render, redirect
from django.views.generic import UpdateView, DetailView, CreateView, ListView

from authsystem.models import User
from incommonpanel.models import Document, Catalog
from .forms import (
	UserRegisterForm, UpdateUserForm,
	DocumentCreationalForm, CatalogCreationalForm)

from buisneslogic.tasks import mail_sending_task


class ModerUserListView(ListView):
	model = User
	template_name = 'user/moder/moder_user_list.html'
	context_object_name = 'users'

	def get(self, request, *args, **kwargs):
		if self.request.user.is_staff:
			return super().get(request, *args, **kwargs)
		else:
			return redirect('user_detail')

	def get_queryset(self):
		return self.model.objects.filter(is_superuser=False,)

class ModerHomeView(ListView):
	model = Catalog
	template_name = 'incommon_templates/moderator_homepage.html'

	def get(self, request, *args, **kwargs):
		if self.request.user.is_staff:
			return super().get(request, *args, **kwargs)
		else:
			return redirect('user_detail')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs) 
		context['user'] = self.request.user
		return context


class ModeratorUserDetailView(DetailView):
	model = User
	template_name = 'user/moder/moder_user_detail.html'
	context_object_name = 'user'

	def get(self, request, *args, **kwargs):
		if self.request.user.is_staff:
			return super().get(request, *args, **kwargs)
		else:
			return redirect('user_detail')

class ModeratorUserUpdateView(UpdateView):
	model = User
	form_class = UpdateUserForm
	context_object_name = 'user'
	template_name = 'user/moder/moder_user_update.html'

	def get(self, request, *args, **kwargs):
		if self.request.user.is_staff:
			return super().get(request, *args, **kwargs)
		else:
			return redirect('user_detail')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		print(context)
		return context

class DocumentCreationsView(CreateView):
	model = Document
	form_class = DocumentCreationalForm
	context_object_name = 'form'
	template_name = 'incommon_templates/document/document_create.html'
	
	def get(self, request, *args, **kwargs):
		if self.request.user.is_staff:
			return super().get(request, *args, **kwargs)
		else:
			return redirect('user_detail')

class CatalogCreationalView(CreateView):
	model = Catalog
	form_class = CatalogCreationalForm
	context_object_name = 'form'
	template_name = 'incommon_templates/catalog/catalog_create.html'

	def get(self, request, *args, **kwargs):
		if self.request.user.is_staff:
			return super().get(request, *args, **kwargs)
		else:
			return redirect('user_detail')


def user_register(request):
	if	request.user.is_staff:
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
		return render (request=request, template_name="user/moder/register.html", context={"register_form":form})
	else:
		return redirect('user_detail')