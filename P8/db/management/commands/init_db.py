from django.core.management.base import BaseCommand, CommandError
from ...openfoodfact.constants import CATEGORY_LIST
from ... models import Category, Product
from ...openfoodfact.openfoodfact import get_products_by_category

class Command(BaseCommand):
    help = "Initialize db with products from OpenFoodFact API"

    def handle(self, *args, **options):
        self.__create_categories_and_products()
        self.stdout.write(
            self.style.SUCCESS('Successfully loaded'))

    def __create_categories_and_products(self):
        for c in CATEGORY_LIST:
            category = Category()
            category.name = c
            category.save()
            products = get_products_by_category(c)
            if products is not None:
                for p in products:
                    product = Product()
                    product.name = p.get('name')
                    product.id_category = category
                    product.nutriscore = p.get('nutriscore')
                    product.image_url = p.get('image')
                    product.save()

