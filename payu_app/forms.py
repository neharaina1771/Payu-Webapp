from django.forms import ModelForm, PasswordInput
from payu_app.models import UserDetails, UserInput

class UserDetailsForm(ModelForm):
    class Meta:
        model = UserDetails
        fields = ['Email', 'Username', 'Password']
        widgets = {
            'Password': PasswordInput()
         }

class UserInputForm(ModelForm):
    class Meta:
        model = UserInput
        fields = ['A_Type', 'Refno', 'D_Type']
