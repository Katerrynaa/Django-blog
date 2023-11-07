from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import Comment, AddArticle

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save_data(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class SignInForm(forms.Form):
    class Meta:
        model = User
        fields = ['username', 'password']

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea())
    class Meta:
        model = Comment
        fields =['body']

class ArticleForm(forms.ModelForm):
    new_author = forms.CharField(max_length=200, required=False) 

    class Meta:
        model = AddArticle
        fields = ['title', 'new_author', 'content']

    def clean(self):
        cleaned_data = super().clean()
        new_author = cleaned_data.get('new_author')

        if not new_author:
            raise forms.ValidationError("You must select an author or enter your name")
        return cleaned_data