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
from ADT.forms import FileForm, ClaimForm
from ADT.models import File, Claim
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

# from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin #class based requirement


# class HomeView(ListView):
#     template_name = 'base.html'
#     Model = Claim, File, Nothing
#     context_object_name = "CLAIMS"
#     def get_queryset(self):
#         return Claim.objects.all()

class ClaimsView(ListView):
    template_name = 'claimsview.html'
    form_class = ClaimForm
    Model = Claim
    context_object_name = "CLAIMS"

    def get_queryset(self):
        return Claim.objects.filter(appNumber = self.kwargs['pk'])

    # def form_valid(self,form):
    #     post = form.save(commit=False)
    #     post.updated_by = self.request.user
    #     post.updated_at = timezone.now()
    #     post.save()
    #     return redirect('topic_posts', pk=post.topic.board.pk, topic_pk=post.topic.pk)

class SelectAppView(CreateView):
    template_name = 'select.html'
    form_class = FileForm
    Model = File
    context_object_name = "file_list"

    def get_queryset(self):
        return File.objects.all()[0]

    def form_valid(self,form):
        # File.objects.all().delete()
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

class OneView(ListView):
    template_name = 'one.html'
    Model = Claim
    context_object_name = "CLAIMS"
    def get_queryset(self):
        return Claim.objects.filter(appNumber= self.kwargs['pk'])

class TwelveView(ListView):
    template_name = 'twelve.html'
    Model = Claim
    context_object_name = "CLAIMS"
    def get_queryset(self):
        return Claim.objects.filter(appNumber= self.kwargs['pk'])

class ArtView(ListView):
    template_name = 'art.html'
    Model = Claim
    context_object_name = "CLAIMS"
    def get_queryset(self):
        return Claim.objects.filter(appNumber= self.kwargs['pk'])
