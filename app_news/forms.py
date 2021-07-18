from django import forms
from app_news.models import New, Comment


class NewCreate(forms.ModelForm):
    class Meta:
        model = New
        fields = '__all__'


class UserComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user_name', 'comment_text']
