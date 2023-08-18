from django.core.management.base import BaseCommand, CommandError
from ... models import Category,Product


class Command(BaseCommand):
    help = "Delete db from postgresql"

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(
            self.style.SUCCESS('Successfully Deleted'))
