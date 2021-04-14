from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if (not user) or (not user.check_password(password)):
                raise forms.ValidationError('Невірний пароль або логін')
            return super().clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self, *args, **kwargs):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Паролі не співпадають')
        return data['password2']