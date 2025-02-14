from django import forms
from rango.models import Page, Category, UserProfile
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
    """ Handles the category form """
    name = forms.CharField(
        max_length=128,
        help_text="Please enter the category name."
    )

    class Meta:
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    """ Handles the page form """
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
        """ Ensure the URL starts with http:// or https:// """
        url = self.cleaned_data.get('url')
        if url and not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        return url


class UserForm(forms.ModelForm):
    """ User registration form with password confirmation """
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
        """ Ensure the two entered passwords match """
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        return cleaned_data


class UserProfileForm(forms.ModelForm):
    """ User profile form including website and profile picture """
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

    def clean_website(self):
        """ Ensure the website URL starts with http:// or https:// """
        website = self.cleaned_data.get('website')
        if website and not website.startswith(('http://', 'https://')):
            website = 'http://' + website
        return website