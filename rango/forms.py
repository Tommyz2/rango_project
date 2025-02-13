from django import forms
from rango.models import Page, Category, UserProfile
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        max_length=128,
        help_text="Please enter the category name."
    )

    class Meta:
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(
        max_length=128,
        help_text="Please enter the title of the page."
    )
    url = forms.URLField(
        max_length=200,
        help_text="Please enter the URL of the page."
    )

    class Meta:
        model = Page
        exclude = ('category',)

    def clean_url(self):
        """ 确保 URL 以 http:// 或 https:// 开头 """
        url = self.cleaned_data.get('url')
        if url and not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        return url


class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        help_text="Enter your password."
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        help_text="Re-enter your password."
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean(self):
        """ 确保两次输入的密码一致 """
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data


class UserProfileForm(forms.ModelForm):
    website = forms.URLField(
        required=False,
        help_text="Enter your website URL (optional)."
    )
    picture = forms.ImageField(
        required=False,
        help_text="Upload your profile picture (optional)."
    )

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')