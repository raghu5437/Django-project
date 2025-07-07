from django.forms import ModelForm
from django import forms
from .models import *


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'body', 'tags']  # Use model's image field directly
        labels = {
            'title': 'Title',
            'image': 'Image URL',
            'body': 'Caption',
            'tags': 'Category'
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter post title',
                'class': 'border border-gray-300 rounded px-3 py-2 w-full mb-4'
            }),
            'image': forms.URLInput(attrs={
                'placeholder': 'Paste image URL from Flickr',
                'class': 'border border-gray-300 rounded px-3 py-2 w-full mb-4'
            }),
            'body': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Add a caption ....',
                'class': 'font text-4xl w-full'
            }),
            'tags': forms.CheckboxSelectMultiple(),
        }


class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags']  # Added title field
        labels = {
            'title': 'Title',
            'body': 'Caption',
            'tags': 'Category'
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter post title',
                'class': 'border border-gray-300 rounded px-3 py-2 w-full mb-2'
            }),
            'body': forms.Textarea(attrs={
                'rows': 3, 
                'class': 'font1 text-4xl'
            }),
            'tags': forms.CheckboxSelectMultiple(),
        }

class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={
                'placeholder': 'Add comment....',
                'class': 'w-full rounded-md border border-gray-300 px-4 py-2 bg-gray-100 text-gray-800 focus:outline-none focus:ring-2 focus:ring-violet-500 transition duration-150'
            })
        }
        labels = {
            'body': ''
        }

class ReplyCreateForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['body']
        widgets = {
            'body':forms.TextInput(attrs={'placeholder': 'Add reply ... ','class':"!text-sm"})
        }
        labels = {
            'body':''
        }