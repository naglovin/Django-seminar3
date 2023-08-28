from datetime import datetime

from django.core.management.base import BaseCommand
from home2_app.models import Client, Order


class Command(BaseCommand):
    help = "Generate fake client and orders."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='UserID')


    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'Name{i}', email=f'mail{i}@mail.ru', phone=f'908058995{i}', address=f'dont now{i}', date_of_registration=datetime.now())
            client.save()
        for j in range(1, count + 1):
            order = Order(client=f'customer{j}', products=f'products {j}', date_ordered=datetime.now(), total_price=f'100+{j}')
            order.save()
