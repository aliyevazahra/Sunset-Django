from captcha.fields import ReCaptchaField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

from .models import *
from django import forms


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
            'title': forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Title Name'}),
            'content': forms.Textarea(attrs={'class': 'single-input', 'placeholder': 'Content'}),
        }

        fields = [
            'title',
            'category',
            'content',
            'image',
        ]


class PostUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.field_class = 'mt-10'
        self.helper.layout = Layout(
            Field("title", css_class="single-input", style="margin-bottom:10px;", placeholder="Title"),
            Field("category", css_class="single-input", style="margin-bottom:10px;"),
            Field("content", css_class="single-input", style="margin-bottom:10px;", placeholder="Add content"),
            Field("image", css_class="single-input", style="margin-bottom:10px;"),
            Field("tag", css_class="single-input", style="margin-bottom:10px;", placeholder="Tags", value=self.instance.post_tag()),
        )

        self.helper.add_input(Submit('submit', "Update Post", css_class="genric-btn success circle"))

    tag = forms.CharField()

    class Meta:
        model = Post
        fields = [
            'title',
            'category',
            'content',
            'image',
        ]

class CreateCommentForm(forms.ModelForm):
    captcha = ReCaptchaField()
    def __init__(self, *args, **kwargs):
        super(CreateCommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field("name", css_class="form-control"),
            Field("email", css_class="form-control"),
            Field("content", css_class="form-control mb-10"),
            Field("captcha"),

        )

        self.helper.add_input(Submit('submit', 'Add Comment', css_class="genric-btn success circle"))


    class Meta:
        model = Comment
        fields =[
            'name',
            'email',
            'content',
        ]
