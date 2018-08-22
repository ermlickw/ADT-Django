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
from ADT.forms import FileForm, ClaimForm, ClaimFormSet
from ADT.models import File, Claim
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView,
                                  View, FormView)

# from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin #class based requirement


# class HomeView(ListView):
#     template_name = 'base.html'
#     Model = Claim, File, Nothing
#     context_object_name = "CLAIMS"
#     def get_queryset(self):
#         return Claim.objects.all()

class ClaimsView(FormView):
    template_name = 'claimsview.html'
    Model = Claim
    form_class = ClaimFormSet
    # initial = {'number': ctx['CLAIMS'].number, 'dependentOn':ctx['CLAIMS'].dependentOn,
    #             'text':ctx['CLAIMS'].text,}

    # context_object_name = "CLAIMS"

    # def get(self, request, *args, **kwargs):
    #     context = locals()
    #     context['pk'] = self.kwargs['pk']
    #     context['CLAIMS']= Claim.objects.filter(appNumber = self.kwargs['pk'])
    #     return render(request,'claimsview.html',context)

    def get_context_data(self, **kwargs):
        ctx = super(ClaimsView, self).get_context_data(**kwargs)
        ctx['pk'] = self.kwargs['pk']
        ctx['CLAIMS']= Claim.objects.filter(appNumber = self.kwargs['pk'])
        return ctx

    def get_form_kwargs(self):
        kwargs = super(ClaimsView, self).get_form_kwargs()
        kwargs["queryset"] = Claim.objects.filter(appNumber = self.kwargs['pk'])
        return kwargs

  #   {% for claim in CLAIMS %}
  #    <!-- <li>{{ claim.text }}</li> -->
  #
  #       {{form}}
  #       <br>
  #
  #
  # {% endfor %}
  #
  # <button type="submit" >Update</button>



    # def get_queryset(self):
    #     return Claim.objects.filter(appNumber = self.kwargs['pk'])
    #
    # get_context_data(self, **kwargs):
    #     return self.kwargs['pk']

    def form_valid(self,form):
        for sub_form in form:
            # if sub_form.has_changed():
            sub_form.save()
        return redirect('claims', pk=self.kwargs['pk'])


    # def get_success_url(self):
    #     return redirect('claims', pk=self.kwargs['pk'])




class SelectAppView(CreateView):
    template_name = 'select.html'
    form_class = FileForm
    # initial = {'appNumber': '12341', 'document':None}
    Model = Claim, File

    # def get(self, request, *args, **kwargs):
    #     context = locals()
    #     context['pk'] = Claim.objects.all()[0].appNumber
    #     context['CLAIMS']= Claim.objects.all()[0]
    #     return render(request,'select.html',context)

    def get_context_data(self, **kwargs):
        ctx = super(SelectAppView, self).get_context_data(**kwargs)
        ctx['pk'] = File.objects.order_by('created_at')[0].appNumber
        ctx['CLAIMS']= File.objects.order_by('created_at')[0].appNumber
        return ctx

    def form_valid(self,form):
        # File.objects.all().delete()
        appNumber = re.sub(" ","",str(form.cleaned_data['appNumber']).translate(string.punctuation)  )     #magic
        super().form_valid(form)
        if form.cleaned_data['document']:
            form.create_claims(self,appNumber)
        return super().form_valid(form) #continue as normal after you do the functions inside



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
    def get(self, request, *args, **kwargs):
        context = locals()
        context['pk'] = self.kwargs['pk']
        context['CLAIMS']= Claim.objects.filter(appNumber = self.kwargs['pk'])
        return render(request,'one.html',context)

class TwelveView(ListView):
    template_name = 'twelve.html'
    Model = Claim
    context_object_name = "CLAIMS"
    def get_queryset(self):
        return Claim.objects.filter(appNumber= self.kwargs['pk'])

    def get(self, request, *args, **kwargs):
        context = locals()
        context['pk'] = self.kwargs['pk']
        context['CLAIMS']= Claim.objects.filter(appNumber = self.kwargs['pk'])
        return render(request,'twelve.html',context)

class ArtView(ListView):
    template_name = 'art.html'
    Model = Claim
    context_object_name = "CLAIMS"
    def get_queryset(self):
        return Claim.objects.filter(appNumber= self.kwargs['pk'])

    def get(self, request, *args, **kwargs):
        context = locals()
        context['pk'] = self.kwargs['pk']
        context['CLAIMS']= Claim.objects.filter(appNumber = self.kwargs['pk'])
        return render(request,'art.html',context)
