from .models import Contact
from django import forms
from .models import PostComment

class AddcntForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = '__all__'


