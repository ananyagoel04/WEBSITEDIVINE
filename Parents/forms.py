from django import forms
from .models import News
from tinymce.widgets import TinyMCE

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['Heading', 'News']
        widgets = {
            'News': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }
