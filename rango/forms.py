from django import forms
from rango.models import Page, Category, UserProfile
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
    """ 处理分类表单 """
    name = forms.CharField(
        max_length=128,
        help_text="Please enter the category name."
    )

    class Meta:
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    """ 处理页面表单 """
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
    """ 用户注册表单，包含密码确认 """
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
            self.add_error('confirm_password', "Passwords do not match.")

        return cleaned_data


class UserProfileForm(forms.ModelForm):
    """ 用户资料表单，包含网站和头像 """
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
        """ 确保网站 URL 以 http:// 或 https:// 开头 """
        website = self.cleaned_data.get('website')
        if website and not website.startswith(('http://', 'https://')):
            website = 'http://' + website
        return website