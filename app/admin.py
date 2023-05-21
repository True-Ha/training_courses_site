from django import forms
from django.contrib import admin


from .models import Training
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class TrainingAdminForm(forms.ModelForm):
    description_week = forms.CharField(widget=CKEditorUploadingWidget())
    train1 = forms.CharField(widget=CKEditorUploadingWidget())
    train2 = forms.CharField(widget=CKEditorUploadingWidget())
    train3 = forms.CharField(widget=CKEditorUploadingWidget())
    train4 = forms.CharField(widget=CKEditorUploadingWidget())
    train5 = forms.CharField(widget=CKEditorUploadingWidget())
    train6 = forms.CharField(widget=CKEditorUploadingWidget())
    text_after_train = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Training
        fields = '__all__'


class TrainingAdmin(admin.ModelAdmin):
    list_display = ('name', 'description_week', 'train1', 'train2',
                    'train3', 'train4', 'train5', 'train6', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    save_on_top = True
    save_as = True
    form = TrainingAdminForm


admin.site.register(Training, TrainingAdmin)
