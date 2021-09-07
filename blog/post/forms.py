from django import forms
from post.models import Post


class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(
        min_length=8, widget=forms.PasswordInput()
    )
    age = forms.IntegerField(min_value=18, required=False)



# add form for Post without fields:
# author(will be added automatically in add_post function)
# image (can't do it)
# created_ad(field is created automatically)
class AddPostForm(forms.Form):
    title = forms.CharField(max_length=200)
    slug = forms.SlugField()
    text = forms.CharField()
    test = forms.CharField()
    # image = forms.ImageField() - don't work


