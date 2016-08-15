from django.test import TestCase, Client
from bookstore.models import Book, Category
from django.core.urlresolvers import reverse


class BookStoreViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="programming", description="for the geeks")
        self.book = Book.objects.create(name="elastic search", description="An intro", author="jubril", category=self.category)

    def tearDown(self):
        Category.objects.all().delete()
        Book.objects.all().delete()

    def test_home_page_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'bookstore/index.html')

    def test_user_can_search_by_category(self):
        data = {'bookerOptions': 'category', 'name': 'programming'
        }
        response = self.client.get(reverse('result'), data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('programming', response.content)

    def test_can_search_by_book_title(self):
        data = {'bookerOptions': 'book', 'name': 'elastic search'}
        response = self.client.get(reverse('result'), data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('elastic search', response.content)




