from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# from ADT.models import Art
# from django.utils import timezone
# # from ADT.formFile ArtForm
import string
import re
from django.conf import settings
import os
from ADT.forms import FileForm
from ADT.models import File, Claim, Nothing
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

# from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin #class based requirement


class HomeView(ListView):
    template_name = 'base.html'
    Model = Claim, File, Nothing
    context_object_name = "CLAIMS"
    def get_queryset(self):
        return Claim.objects.all()

class SpecificHomeView(ListView):
    template_name = 'apphome.html'
    Model = Claim
    context_object_name = "CLAIMS"
    def get_queryset(self):
        return Claim.objects.filter(appNumber= self.kwargs['pk'])

class ClaimsView(CreateView):
    template_name = 'claims.html'
    form_class = FileForm
    Model = File

    def form_valid(self,form):
        File.objects.all().delete()
        appNumber = re.sub(" ","",str(form.cleaned_data['appNumber']).translate(string.punctuation)  )     #magic
        if 'upload' in form.data:
            super().form_valid(form)
            if form.cleaned_data['document']:
                form.create_claims(self,appNumber)
        return super().form_valid(form)#continue as normal after you do the functions inside

# def get_appno(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             appNumber = form.cleaned_data['appno']
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect(reverse("apphome",kwargs={'pk':self.appNumber}))
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()
#
#     return render(request, 'claims.html', {'form': form})


    # def post(request,instance):
    #     data = instance.POST.copy()
    #     form.create_claims(self)
    #     return super().post(form)


#could jsut add fields= here and not useforms at all

class OneView(TemplateView):
    template_name = 'one.html'

class TwelveView(TemplateView):
    template_name = 'twelve.html'

class ArtView(TemplateView):
    template_name = 'art.html'
