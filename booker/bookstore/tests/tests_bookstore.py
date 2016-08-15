from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.


class BookStoreTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.set_window_size(1400, 1000)
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_book_app(self):

        # As a user i go to the home page of my app
        self.browser.get('http:127.0.0.1:8000/')

        # I see a bold text welcoming me to the app

        # I am prompted to enter a search parameter

        # I enter the name of my book elasticsearch and hit on enter

        #  I get a response of the with books similar to my search

        # I click to go back to search by category

        # I enter the name of the category and i hit on enter

        # I get a response of the books in the category

        # I click on one of the book to view the book details










