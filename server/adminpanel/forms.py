from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from authsystem.models import User
from incommonpanel.models import Document, Catalog


###		Custom Inputs
class DateInput(forms.DateInput):
    input_type = 'date'

###		Forms
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = (
			"name", "middlename", "surname",
			"is_staff", "private_access", "birthsday",
			"department","email", "password1", "password2")
		widgets = {
            'birthsday': DateInput(),
        }

	def save(self, commit=True):
		user = super(UserRegisterForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class DocumentCreationalForm(forms.ModelForm):
	title = forms.CharField(required=True)
	file = forms.FileField(required=True,)

	class Meta:
		model = Document
		fields = ['title', 'file', 'private_access', 'catalog']

class CatalogCreationalForm(forms.ModelForm):
	title = forms.CharField(required=True)

	class Meta:
		model = Catalog
		fields = ['title',]



class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
		'name', 'middlename', 'surname',
		'department', 'birthsday', 'private_access',
		'is_active', 'is_staff',]
        widgets = {
            'birthsday': DateInput(),
        }
