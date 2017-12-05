from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment

FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue apple'),
    ('green', 'Green bananas'),
    ('black', 'Black'),
)

RATING_CHOICES = (
    ('1', 'Very Poor - 1'),
    ('2', 'Poor 2'),
    ('3', 'Average 3'),
)

class SignUpForm(UserCreationForm):
    bio = forms.CharField(widget=forms.Textarea, required=False, help_text='Describe yourself to us.')
    avatar = forms.ImageField(required=False, help_text='Your avatar.')
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2','bio', 'avatar')

class SampleForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )

class CommentForm(forms.ModelForm):
     def clean_body(self):
            comment = self.cleaned_data['body']
            if comment.find("shit") != -1 :
                raise forms.ValidationError("Please be nice. No vulgar words.")

            # Always return a value to use as the new cleaned data, even if
            # this method didn't change it.
            return comment

     class Meta:
         model = Comment
         # exclude = []
         fields = '__all__'
         widgets = {
             'rating': forms.RadioSelect(choices=RATING_CHOICES),
         }
         labels = {
             'body': 'Comment',
         }
         # fields = ["body"]
