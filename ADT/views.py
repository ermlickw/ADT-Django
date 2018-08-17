from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# from ADT.models import Art
# from django.utils import timezone
# # from ADT.formFile ArtForm
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

class ClaimsView(CreateView):
    template_name = 'claims.html'
    form_class = FileForm
    Model = File,Nothing

    def form_valid(self,form):
        description = form.cleaned_data['description']  #magic
        super().form_valid(form)
        form.create_claims(self,description)
        return  super().form_valid(form)#continue as normal after you do the functions inside

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

# def model_form_upload(request):
#     if request.method == 'POST':
#         form = FileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = DocumentForm()
#     return render(request, 'core/model_form_upload.html', {
#         'form': form
#     })
