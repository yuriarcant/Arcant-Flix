from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from .forms import CriarContaForm, FormHomePage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# def homepage(request):
#     return render(request, 'homepage.html')

class Homepage(FormView):
    template_name = 'homepage.html'
    form_class= FormHomePage

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated :
            return redirect('filme:homefilmes')
        else:
            return super().get(request, *args, **kwargs) #redireciona pra homepage
        
    def get_success_url(self) -> str:
        email= self.request.POST.get('email')
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')
        

# def homefilmes(request):
#     context = {}
#     lista_filmes= Filme.objects.all()
#     context['lista_filmes']= lista_filmes
#     return render (request, 'homefilmes.html', context)

class Homefilmes(LoginRequiredMixin, ListView):
    template_name = 'homefilmes.html'
    model = Filme



class Detalhesfilme(LoginRequiredMixin, DetailView):
    template_name = 'detalhesfilmes.html'
    model = Filme

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        filme = self.get_object()
        filme.vizualizacao += 1
        filme.save()
        usuario= request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context= super(Detalhesfilme, self).get_context_data(**kwargs)
        filmes_relacionados = self.model.objects.filter(categoria=self.get_object().categoria)[0:5]
        context['filmes_relacionados']= filmes_relacionados
        return context
    
class Pesquisafilme(LoginRequiredMixin, ListView):
    template_name = 'pesquisa.html'
    model = Filme


    def get_queryset(self) -> QuerySet[Any]:
        pesquisa = self.request.GET.get('query')
        if pesquisa:
            object_list= self.model.objects.filter(titulo__icontains= pesquisa)
            return  object_list
        else:
            return None


class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model= Usuario
    fields= ['first_name', 'last_name', 'email' ]
    
    def test_func(self):
        user = self.get_object()
        return self.request.user == user

    def get_success_url(self) -> str:
        return reverse('filme:homefilmes')


class Criarconta(FormView):
    template_name= 'criarconta.html'
    form_class= CriarContaForm

    def form_valid(self, form: Any) -> HttpResponse:
        form.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse('filme:login')
    
    

