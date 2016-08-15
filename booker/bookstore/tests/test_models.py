from django.test import TestCase
from bookstore.models import Book, Category


class InventoryModelTest(TestCase):

    def test_book_is_related_to_category(self):
        test_category = Category.objects.create()
        books = Book()
        books.category = test_category
        books.save()
        self.assertIn(books, test_category.books_set.all())
