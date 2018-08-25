from django import forms
from django.http import HttpResponse
from .models import File, Claim
from docx import Document
import os
from django.conf import settings
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
import re
import string
import json
#


def add_update_parents(appNumber):
    for claim in Claim.objects.filter(appNumber = appNumber).order_by('number'):
        print(claim.number)
        if claim.dependentOn != 0:
            claim.parents = ""
            claim.parents = str(claim.parents)
            claim_parents_list = claim.parents.split()
            parentclaim = Claim.objects.filter(appNumber = appNumber, number=int(claim.dependentOn))[0]
            claim_parents_list.append(parentclaim.number)
            while int(parentclaim.dependentOn) != 0:
                    parentclaim = Claim.objects.filter(appNumber = appNumber, number=parentclaim.dependentOn)[0]
                    claim_parents_list.append(parentclaim.number)
            claim.parents = claim_parents_list
            claim.save()
        print(claim.parents)
        pass

def add_update_children(appNumber):
    for claim in Claim.objects.filter(appNumber = appNumber).order_by('number'):
        print (claim.number)
        claim.children = ""
        claim.children = str(claim.children)
        claim_children_list = claim.children.split()
        for subclaim in Claim.objects.filter(appNumber = appNumber).order_by('number'):
            if subclaim.number != claim.number:  #for all claims other than the claim itself
                if str(subclaim.parents).find(str(claim.number)) != -1:  #if the subclaim has the claim as a parents
                    if not(subclaim.number in claim_children_list):
                        claim_children_list.append(subclaim.number)
        print (claim_children_list)
        claim.children = claim_children_list
        claim.save()

        pass




    # for claim in Claim.objects.filter(appNumber = appNumber, dependentOn = 0):
    #     claim.children = str(claim.children)
    #     claim_children_list = claim.children.split()
    #
    #     for child in Claim.objects.filter(appNumber = appNumber, dependentOn = claim.number):
    #         child.children = str(child.children)
    #         child_children_list = child.children.split()
    #         claim_children_list.append(child.number)
    #
    #         for subchild in Claim.objects.filter(appNumber = appNumber, dependentOn = child.number):
    #             subchild.children = str(subchild.children)
    #             subchild_children_list = subchild.children.split()
    #             claim_children_list.append(subchild.number)
    #             subchild_children_list.append(subchild.number)
    #
    #
    #     claimset.append(claim.number)
    #
    #
    #     claim.save()
    pass




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
        for para in doc.paragraphs:
            numb = para.text.split('.')[0]
            numb= int(re.sub(" ","",str(numb).translate(string.punctuation)))
            list_of_words = para.text.split()
            if 'claim' in list_of_words: #if it's a dependent claim
                depend = int(list_of_words[list_of_words.index('claim') + 1])
                txt = " ".join(list_of_words[list_of_words.index('claim')+2:])
                Claim.objects.create(number=numb, dependentOn=depend, text=txt,citedText=txt, appNumber = appNumber, parents = 0,
                                    parent=Claim.objects.filter(appNumber = appNumber, number=depend)[0])
            else:
                depend = 0
                txt = ".".join(para.text.split('.')[1:]).lstrip().rstrip()
                Claim.objects.create(number=numb, dependentOn=depend, text=txt,citedText=txt, appNumber = appNumber, parents = 0,
                                    parent=None)

        #add parents and dependnts
        add_update_parents(appNumber)
        add_update_children(appNumber)


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

    def update_claims(nothin,appno):
        print(appno)
        add_update_parents(appno)
        add_update_children(appno)
        pass

        #basic form to select application
# class AppnoForm(forms.Form):
#     # ids = forms.ModelChoiceField(queryset=Paper.objects.all())
#     appNumber = forms.CharField(label="sdf",max_length='10')
