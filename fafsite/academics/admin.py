import json

from django.contrib import admin
from django import forms
from .models import Course
from general.models import FAFUser, UserMetaType, UserMeta, UserExtended


def getMetaTypes():
    result = {}
    meta_types = UserMetaType.objects.all()
    for meta in meta_types:
        try:
            data = json.loads(meta.data)
        except:
            data = meta.data
        result[meta.key] = {'type': meta.type, 'data': data, 'value': ''}
    return result


class UserAdminForm(forms.ModelForm):
    userExtended = None

    class Meta:
        model = FAFUser

    def __init__(self, *args, **kwargs):
        super(UserAdminForm, self).__init__(*args, **kwargs)
        # Set the form fields based on the model object
        if 'instance' in kwargs:
            instance = kwargs['instance']   # FAFUser instance
            self.userExtended = UserExtended(instance.id)

    def getAdditionalFieldsets(self):
        if self.userExtended is not None:
            meta_types = getMetaTypes()
            user_meta_types = self.userExtended.getAttributes()
            result = dict()
            for key in meta_types:
                if key in user_meta_types:
                    result[key] = user_meta_types[key]
                else:
                    result[key] = meta_types[key]
            return result
        else:
            return getMetaTypes()


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')
    search_fields = ('name', 'surname')
    form = UserAdminForm

    def save_model(self, request, obj, form, change):
        obj.save()  # FAFUser save
        userExtended = UserExtended(obj.id)
        for userMetaType in UserMetaType.objects.all():
            if userMetaType.key in request.POST and request.POST[userMetaType.key] != '':
                if userMetaType.multiple:
                    setattr(userExtended, userMetaType.key,
                            request.POST.getlist(userMetaType.key))
                else:
                    setattr(userExtended, userMetaType.key,
                            request.POST[userMetaType.key])
                userExtended.save()
            else:
                userExtended.delMeta(userMetaType.key)


class UserMetaTypeAdmin(admin.ModelAdmin):
    list_display = ('key', 'type', 'multiple', 'data')
    search_fields = ('key', 'type')

    # save as a JSON object
    def save_model(self, request, obj, form, change):
        if obj.data:
            try:
                json.loads(obj.data)
            except ValueError:
                data = obj.data
                data = data.split(',')
                data = json.dumps(data)
                obj.data = data
        obj.save()


class UserMetaAdmin(admin.ModelAdmin):
    list_display = ('user', 'meta', 'value')


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        users = FAFUser.objects.all()
        usersExtended = []
        for user in users:
            usersExtended.append(UserExtended(user.id))

        filter = ['professor']
        choices = []
        for userExtended in usersExtended:
            type = userExtended.type
            if type:
                if set(filter).issubset(set(type)):
                    userId = FAFUser.objects.get(id=userExtended.id)
                    choices.append((userId.id, userId))
        w = self.fields['professors'].widget
        w.choices = choices
        print choices


class CourseAdmin(admin.ModelAdmin):
    list_display = ('subject_en', 'subject_ro', 'semester')
    search_fields = ('subject',)
    form = CourseForm


admin.site.register(FAFUser, UserAdmin)
admin.site.register(UserMetaType, UserMetaTypeAdmin)
admin.site.register(UserMeta, UserMetaAdmin)
admin.site.register(Course, CourseAdmin)
