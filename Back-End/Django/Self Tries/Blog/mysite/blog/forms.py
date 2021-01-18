# import form class from django 
from django import forms 
  
# import GeeksModel from models.py 
from .models import * 
  
# create a ModelForm 
class PostForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = Post 
        fields = "__all__"


class CommentForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = Comment 
        fields = ('body',)


