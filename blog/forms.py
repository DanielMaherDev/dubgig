from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
	    model = Comment
	    fields = ('body',)

class ProfileForm(forms.ModelForm):
    class Meta:
	    model = Comment
	    fields = ('email',)		