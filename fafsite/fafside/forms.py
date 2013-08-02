from django import forms


class Profile(forms.Form):
    name = forms.CharField(max_length=15)
    surname = forms.CharField(max_length=31)
    group = forms.CharField(max_length=15)
    photo = forms.ImageField(required=False)
    programming_skills = forms.CharField(widget=forms.Textarea, required=False)
    projects_involved = forms.CharField(widget=forms.Textarea, required=False)
    publications = forms.CharField(widget=forms.Textarea, required=False)
    diploma_topic = forms.CharField(max_length=127, required=False)
    current_job = forms.CharField(max_length=127, required=False)
    past_jobs = forms.CharField(widget=forms.Textarea, required=False)
    linkedin = forms.URLField(max_length=127, required=False)
    facebook = forms.URLField(max_length=127, required=False)
    googleplus = forms.URLField(max_length=127, required=False)
    skype = forms.CharField(max_length=127, required=False)
    phone = forms.CharField(max_length=127, required=False)
