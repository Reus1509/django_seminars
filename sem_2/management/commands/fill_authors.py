import datetime
from django.core.management.base import BaseCommand
from typing import Any
from sem_2.models import Author


class Command(BaseCommand):
    help = 'Creates new users'

    def handle(self, *args: Any, **options: Any):
        for i in range(1, 11):
            author = Author(name=f'Author {i}',
                            last_name=f'LastName {i}',
                            email=f'Email{i}@mail.ru',
                            bio=f'biobiobio{1}',
                            birthday=datetime.date(2000, 1, 1))
            self.stdout.write(self.style.SUCCESS(f'Автор {author} создан!'))
            author.save()

