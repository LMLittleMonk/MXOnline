from django import forms
from apps.users.models import UserProfile
class LoginForm(forms.Form):
    username = forms.CharField(required=True,min_length=2)
    password = forms.CharField(required=True,min_length=3)

class RegisterForm(forms.ModelForm):
    username = forms.CharField(required=True,min_length=8)
    password = forms.CharField(required=True,min_length=8)
    email = forms.EmailField(required=True)
    class Meta:
        model = UserProfile
        fields = ['username','password','email']

class ImageUploadForm(forms.Form):

    class Meta:
        model = UserProfile
        fields = ['image']

class UserInfoForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['nick_name','gender','birthday','address','mobile']

class PwdChangeForm(forms.Form):
    password1 = forms.CharField(required=True,min_length=6)
    password2 = forms.CharField(required=True,min_length=6)


