from django import forms

from .models import (
    ContactModel, CommentModel
)


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        # fields = ['name', 'email', 'message']
        fields = '__all__'


class CommentForm(forms.ModelForm):

    class Meta:
        model = CommentModel
        fields = ['body']