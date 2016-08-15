from django.test import TestCase, Client
from bookstore.models import Book, Category
from django.core.urlresolvers import reverse


class BookStoreViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'bookstore/index.html')

    def test_search_book_returns_appropriate_response(self):
        pass

    def test_empty_result_for_category_that_does_not_exist(self):
        pass

    def test_empty_result_for_book_that_does_not_exist(self):
        pass

