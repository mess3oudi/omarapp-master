from django.core.management.base import BaseCommand
from core.models import Accessory

class Command(BaseCommand):
    help = 'Lists all accessory prices from the database'

    def handle(self, *args, **options):
        accessories = Accessory.objects.all()
        
        if not accessories.exists():
            self.stdout.write(self.style.WARNING('No accessories found in database'))
            return
            
        for accessory in accessories:
            self.stdout.write(f"{accessory.name} : {accessory.price}")
            
        self.stdout.write(self.style.SUCCESS(f'Successfully listed {accessories.count()} accessories'))
