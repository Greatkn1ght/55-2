from django import forms
from posts.models import Post

class PostForm(forms.Form):
    image = forms.ImageField(required=False)
    player = forms.CharField(max_length=256)
    definition = forms.CharField(max_length=559)
    
    def clean_title(self):
        cleaned_date = super().clean()
        player = cleaned_date.get("player")
        if player.lower() == "javascript":
            raise forms.ValidationError("Javascript is not allowed!")
        return player
    
    def clean(self):
        cleaned_data = super().clean()
        player = cleaned_data.get("player")
        definition = cleaned_data.get("definition")
        if player and definition and (player.lower() == definition.lower()):
            raise forms.ValidationError("Player and its definition should not be the same!")
        return cleaned_data