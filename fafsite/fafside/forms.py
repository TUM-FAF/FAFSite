from django import forms


class Profile(forms.Form):
    name = forms.CharField(max_length=15)
    surname = forms.CharField(max_length=31)
    group = forms.CharField(max_length=15)
    photo = forms.ImageField(required=False)
    programming_skills = forms.Textarea()
    projects_involved = forms.Textarea()
    publications = forms.Textarea()
    diploma_topic = forms.CharField(max_length=127, required=False)
    current_job = forms.CharField(max_length=127, required=False)
    past_jobs = forms.Textarea()
    linkedin = forms.URLField(max_length=127, required=False)
    facebook = forms.URLField(max_length=127, required=False)
    googleplus = forms.URLField(max_length=127, required=False)
    skype = forms.URLField(max_length=127, required=False)
    phone_number = forms.CharField(max_length=127, required=False)

