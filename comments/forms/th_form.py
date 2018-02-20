from django import forms
from django_comments.forms import CommentForm
from comments.models import *


class ThCommentForm(CommentForm):
    parent = forms.ModelChoiceField(queryset=ThComment.objects.all(), required=False, widget=forms.HiddenInput)

    def get_comment_model(self):
        return ThComment

    def get_comment_create_data(self, site_id=None):
        data = super(ThCommentForm, self).get_comment_create_data()
        data['parent'] = self.cleaned_data['parent']
        return data
