from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Are you sure you are registered? We cannot find this user.")
        return username

    def clean_password(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
            #raise forms.ValidationError("Are you sure you are registered? We cannot find this user.")
        if user is not None and not user.check_password(password):
            raise forms.ValidationError("Invalid Password")
        elif user is None:
            pass
        else:
            return password

class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())     
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email']       