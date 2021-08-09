from .models import Post, Group
from django import forms
from .models import Post
from django.forms import ModelForm


class PostForm(ModelForm):
    text = forms.CharField(widget=forms.Textarea(
        attrs={"rows": 10, "cols": 40}), required=True)

    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   to_field_name="title",
                                   required=False)

    class Meta:
        model = Post
        fields = ('text', 'group')
