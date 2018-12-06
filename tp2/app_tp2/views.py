from django.shortcuts import render
from django.db.models import F,ExpressionWrapper,DecimalField
from django.http import HttpResponseRedirect
from django.views import View
from django.forms import ModelForm
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import  ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Estoque
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
# Create your views here.

class ListarProdutos(LoginRequiredMixin,ListView):
   
     model = Estoque
     template_name = "lista_produtos.html"
     @cache_page(60 * 10)
     def get_queryset(self):
         return Estoque.objects.filter(usuario=self.request.user)


class BuscarProdutos(LoginRequiredMixin,ListView):
   
     model = Estoque
     template_name = "buscar.html"

     def get(self, request):
         return render(
            request,
            template_name='buscar.html')
     
     def post(self, request):
         return Estoque.objects.filter(nome=request.POST.busca)
          
     
         

class DetalharProduto(LoginRequiredMixin,DetailView):
   
     model = Estoque
     template_name = "detalhes_produto.html"
     
                       

class EstoqueForm(LoginRequiredMixin,ModelForm):
    class Meta:
        model = Estoque
        fields = ['nome','descricao', 'quantidade', 'preco',]
        

class SalvarProduto(LoginRequiredMixin,View):
    model = Estoque
    fields = ['nome','descricao', 'quantidade', 'preco',]
    template_name = "inserir.html"
    success_url = reverse_lazy('lista_produtos')

class InserirProduto(SalvarProduto,CreateView):
    def form_valid(self, form):
        produto = form.save(commit=False)
        produto.usuario = self.request.user
        produto.save()
        return super(SalvarProduto, self).form_valid(form)

class AtualizarProduto(SalvarProduto,UpdateView):
    pass

class RemoverProduto(DeleteView):
    model = Estoque
    success_url = reverse_lazy('lista_produtos')