from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


###		Custom Inputs
class DateInput(forms.DateInput):
    input_type = 'date'

###		Forms
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("email", "password1", "password2")

	def save(self, commit=True):
		user = super(UserRegisterForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
		'name', 'middlename', 'surname',
		'birthsday', ]
        widgets = {
            'birthsday': DateInput(),
        }
