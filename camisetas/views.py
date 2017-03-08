from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from camisetas.models import *
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseBadRequest
from camisetas.forms import TshirtForm
from django.utils.timezone import now
from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404


@method_decorator(login_required, name='dispatch')
class tshirt_list(ListView):
    template_name = 'camisetas/Tshirt.html'
    context_object_name = 'camisetas'

    def get_context_data(self, **kwargs):
        context = super(tshirt_list, self).get_context_data(**kwargs)
        context['form'] = TshirtForm
        return context

    def get_queryset(self):
        return TshirtStyle.objects.filter(sites=get_current_site(self.request))

    def get(self, request, *arg, **kwargs):
        if get_current_site(request).domain == 'localhost:8000':
            raise Http404
        return super(tshirt_list, self).get(request, *arg, **kwargs)

class createCamiseta(CreateView, LoginRequiredMixin):
    template_name = 'camisetas/crear_camiseta.html'
    model = Tshirt
    fields = ['size', 'amount', ]
    success_url = '/tshirt'

    def form_valid(self, form):
        form.instance.style_id = self.kwargs['style_id']
        form.instance.user = self.request.user
        form.instance.last_update = now()
        return super(createCamiseta, self).form_valid(form)

    def get(self, request, *arg, **kwargs):
        if get_current_site(request).domain == 'localhost:8000':
            raise Http404
        return super(createCamiseta, self).get(request, *arg, **kwargs)

class Carrito(ListView, LoginRequiredMixin):
    template_name = 'camisetas/carrito.html'
    context_object_name = 'camisetas'

    def get_queryset(self):
        return Tshirt.objects.filter(pagada=False, style__sites=get_current_site(self.request))

    def get(self, request, *arg, **kwargs):
        if get_current_site(request).domain == 'localhost:8000':
            raise Http404
        return super(Carrito, self).get(request, *arg, **kwargs)


# pagar un solo pedido
@login_required()
def pagarPedido(request, pedido_id):
    tshirt = Tshirt.objects.get(pk=pedido_id, style__sites=get_current_site(request))
    # Aqui debe ir la funcion qu permite pagar por PayPal
    tshirt.pagada = True
    tshirt.save()
    messages.add_message(request, messages.SUCCESS, 'Gracias por comprar las camisetas del evento')
    return redirect('tshirts:carrito')


@login_required()
def editarPedido(request):
    id_pedido = request.POST['id_pedido']
    elemento = Tshirt.objects.get(pk=id_pedido, style__sites=get_current_site(request))
    elemento.amount = request.POST['amount']
    elemento.save()
    return JsonResponse({'mensaje': "Pedido eliminado"})

# pagar todos los pedidos del usuario autenticado
@login_required()
def pagarTodo(request):
    camisetas = Tshirt.objects.filter(user=request.user, style__sites=get_current_site(request))
    # Aqui debe ir la funcion qu permite pagar por PayPal
    for tshirt in camisetas:
        tshirt.pagada = True
        tshirt.save()
    messages.add_message(request, messages.SUCCESS, 'Gracias por comprar las camisetas del evento')
    return redirect('tshirts:tshirt')


@login_required()
def deletePedido(request):
    user = request.user
    id_pedido = request.POST['id_pedido']
    camiseta = get_object_or_404(Tshirt, pk=id_pedido)
    if user != camiseta.user:
        return HttpResponseBadRequest()
    else:
        camiseta.delete()
    return JsonResponse({'mensaje': "Pedido eliminado"})


@login_required()
def agregar_pedido(request):
    user = request.user
    amount = request.POST['amount']
    talla = request.POST['talla']

    id_sty = request.POST['id_style']

    obj = TshirtStyle.objects.get(pk=id_sty, sites=get_current_site(request))
    Tshirt.objects.create(user=user, style=obj, amount=amount, last_update=now(), size=talla)
    return JsonResponse({'id_camiseta': Tshirt.objects.last().pk})


# para poder saber las camisetas sin pagar mediante ajax pa los fronten cuando eliminen un pedido
# por ajax actualicen el indice de camisetas pendientes en el base
@login_required()
def camisetas_pendientes(request):
    user = request.user
    pendientes = user.profile.camisetas_sin_pagar
    return JsonResponse({'camisetas_pendientes': pendientes})
