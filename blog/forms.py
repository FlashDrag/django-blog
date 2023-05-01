from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    # override number of rows for the body field
    body = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    def __init__(self, *args, **kwargs):
        '''
        method overrides the parent class's method to add
        a FormHelper instance to the form, which defines
        the layout and behavior of the form's fields
        '''
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # compose the form's layout for the body field
        self.helper.layout = Layout(
            Field('body',)
        )

    class Meta:
        model = Comment
        fields = ('body',)
