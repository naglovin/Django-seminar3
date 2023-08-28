from django.urls import path
from .views import index, view_for, client_order, order_full

urlpatterns = [
    path('', index, name='index'),
    path('goods/', view_for, name='templ_for'),
    path('client/<int:client_id>/', client_order, name='client_order'), # если пользователь введет client а после <int:client_id> то сработает представление client_order которое вернет заказы
    path('order/<int:order_id>/', order_full, name='order_full'),
]