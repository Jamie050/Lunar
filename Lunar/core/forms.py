from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].labal = 'What would you like to be called'
        self.fields['email'].labal = 'Enter your email'
        self.fields['password1'].label = 'Enter a password'
        self.fields['password2'].label = 'Retype your password'

        self.fields['username'].help_text = ''
        self.fields['email'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

        