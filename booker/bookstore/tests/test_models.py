from django.test import TestCase
from bookstore.models import Book, Category


class InventoryModelTest(TestCase):

    def test_book_is_related_to_category(self):
        test_category = Category.objects.create()
        books = Book()
        books.category = test_category
        books.save()
        self.assertIn(books, test_category.books__set.all())

    def test_string_representation_of_categories(self):
        category = Category.objects.create(name="health", description="health category")
        self.assertEqual(category.name, 'health')

