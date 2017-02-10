from django.conf.urls import url, include
from camisetas.views import *

urlpatterns = [
    url(r'^camisetas_pendientes/$', camisetas_pendientes, name='camisetas_pendientes'),
    url(r'^delete_pedido/$', deletePedido, name='ajax_delete_pedido'),
    url(r'^agregar_pedido/$', agregar_pedido, name='ajax_agregar_pedido'),
    url(r'^pagar_pedido/(?P<pedido_id>[0-9]+)/$', pagarPedido, name='pagar_pedido'),
    url(r'^editar_pedido/$', editarPedido, name='editar_pedido'),
    url(r'^pagar_todos/$', pagarTodo, name='pagar_todo'),
    url(r'^carrito/$', Carrito.as_view(), name='carrito'),
    url(r'^(?P<style_id>[0-9]+)/encargar/$', createCamiseta.as_view(), name='encargar_camiseta'),
    url(r'^$', tshirt_list.as_view(), name='tshirt'),
    ]