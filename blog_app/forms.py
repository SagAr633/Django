from django import forms
from blog_app.models import Blogs,UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]



class UserLoginForm(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(widget=forms.PasswordInput())

class AddBlogForm(forms.ModelForm):
    options=(
        ('News','News'),
        ('Politics','Politics'),
        ('Sports','Sports'),
        ('Entertainment','Entertainment'),
        ('Tech','Tech')
             )
    topic=forms.ChoiceField(choices=options)
    class Meta:
        model=Blogs
        fields=[

            'topic',
            'blog_title',
            'blog_image',
            'content',
        ]

class UserProfileForm(forms.ModelForm):
    options1=(
        ('Single','Single'),
        ('Married','Married'),
        ('Divorced', 'Divorced'),
        ('Separated', 'Separated'),
        ('Widowed', 'Widowed'),
    )
    marital_status=forms.ChoiceField(choices=options1)

    options2=(
        ('Australia', 'Australia'),
        ('Brazil', 'Brazil'),
        ('Canada', 'Canada'),
        ('Germany', 'Germany'),
        ('India', 'India'),
        ('Italy', 'Italy'),
        ('UK', 'UK'),
        ('USA', 'USA')
    )
    country=forms.ChoiceField(choices=options2)

    class Meta:
        model=UserProfile
        fields=[
            'pro_pic',
            'date_of_birth',
            'country',
            'state',
            'marital_status',
            'phone'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }