from django import forms
from django.http import HttpResponse
from .models import File, Claim
from docx import Document
import os
from django.conf import settings
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
#
#


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('appNumber', 'document', )

        widgets = {

            'appNumber': forms.Textarea(attrs={'style': 'border-color: blue;',
                                                 'placeholder': 'e.g., 14/595,458'}),
        } #add css to the fields here


    def create_claims(self,something,appNumber):
                                  #File.objects.get(pk=1).document filed file cannot be read...
        filepath = os.path.join(settings.MEDIA_ROOT,appNumber + ".docx")
        doc = Document(filepath)
        fullText=[]
        for para in doc.paragraphs:
            fullText.append(para.text)
        Claim.objects.create(text=fullText, appNumber = appNumber)
        Claim.objects.create(text='second paragraph', appNumber = appNumber)
        pass


class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ('appNumber', 'text','dependentOn', 'number' )
        widgets = {
            'dependentOn': forms.Textarea(attrs={'style': 'border-color: blue;',
                                                 'placeholder': 'dependent?'}),

            'number': forms.Textarea(attrs={'style': 'border-color: blue;',
                                                 'placeholder': 'number?'}),

            'text': forms.Textarea(attrs={'style': 'border-color: blue;',
                                                 'placeholder': 'claim text should be here?'}),
        } #add css to the fields here
        def __init__(self, *args, **kwargs):
                # self.pk = kwargs.pop('pk')
                super(ClaimForm, self).__init__(*args, **kwargs)
                self.kwargs['queryset'] = None

BaseClaimFormSet = modelformset_factory(Claim,exclude=(), form=ClaimForm, extra=1)

class ClaimFormSet(BaseClaimFormSet):
    def __init__(self, *args, **kwargs):
        #  create a user attribute and take it out from kwargs
        # so it doesn't messes up with the other formset kwargs
        # self.pk = kwargs.pop('pk')
        super(ClaimFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = True

    def _construct_form(self, *args, **kwargs):
        # inject user in each form on the formset
        # kwargs['pk'] = self.appNumber
        # kwargs["queryset"] = Claim.objects.filter(appNumber = self.kwargs['pk'])
        return super(ClaimFormSet, self)._construct_form(*args, **kwargs)










        #basic form to select application
# class AppnoForm(forms.Form):
#     # ids = forms.ModelChoiceField(queryset=Paper.objects.all())
#     appNumber = forms.CharField(label="sdf",max_length='10')
