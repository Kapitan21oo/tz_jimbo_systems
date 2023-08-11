from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Loads initial data'

    def handle(self, *args, **kwargs):
        call_command('loaddata', 'load_data.json')
