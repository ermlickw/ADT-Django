from django import forms
from django.http import HttpResponse
from .models import File, Nothing, Claim
from docx import Document
import os
from django.conf import settings
#
#
# class ArtForm(forms.ModelForm):
#     #customvalidation would go here
#     class Meta:
#         model = Post
#         fields = "__all__" #"('text',)" [] is for exclude instead
#
#         widgets = {
#             'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
#         }
class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('appNumber', 'document', )

        widgets = {

            'appNumber': forms.Textarea(attrs={'style': 'border-color: blue;',
                                                 'placeholder': 'e.g., 14/595,458'}),
        } #add css to the fields here

    def create_nothing(self):
        instance = Nothing.objects.create(text='df')
        return HttpResponse('df')


    def create_claims(self,something,appNumber):
                                  #File.objects.get(pk=1).document filed file cannot be read...
        filepath = os.path.join(settings.MEDIA_ROOT,appNumber + ".docx")
        doc = Document(filepath)
        fullText=[]
        for para in doc.paragraphs:
            fullText.append(para.text)
        Claim.objects.create(text=fullText, appNumber = appNumber)

        return print(self)

        #basic form to select application
# class AppnoForm(forms.Form):
#     # ids = forms.ModelChoiceField(queryset=Paper.objects.all())
#     appNumber = forms.CharField(label="sdf",max_length='10')
