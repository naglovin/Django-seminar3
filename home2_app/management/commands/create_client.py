from django.core.management.base import BaseCommand
from home2_app.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(name='John', email='john@example.com', phone='9080589950', address='Chaikovskogo 57/31')
        client.save()
        self.stdout.write(f'{client}')