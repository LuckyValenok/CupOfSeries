from django import forms


class FriendForm(forms.Form):
    username = forms.CharField(max_length=150)
