from django.core.management.base import BaseCommand
from sem_2.models import Author

class Command(BaseCommand):
    help = 'Delete author by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='author_id')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']

        author = Author.objects.filter(pk=pk).first()
        author.delete()
        self.stdout.write(self.style.SUCCESS(f'Deleted author: {author}'))
