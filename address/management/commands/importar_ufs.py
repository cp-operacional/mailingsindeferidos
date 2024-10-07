from django.core.management.base import BaseCommand
from address.models import Estados
import csv
from django.db import transaction

class Command(BaseCommand):
    help = 'Importa dados de indeferidos de um arquivo CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Caminho para o arquivo CSV')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            with transaction.atomic():
                for row in csv_reader:
                    # Cria um dicionário com todos os campos do CSV
                    indeferido_data = {key: value for key, value in row.items() if value}
                    
                    # Cria o objeto Indeferido com todos os campos do CSV
                    Estados.objects.create(**indeferido_data)
        
        self.stdout.write(self.style.SUCCESS('Importação concluída com sucesso!'))