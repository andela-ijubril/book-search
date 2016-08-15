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

        self.assertIn('Booker:: Book search made easy', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Search books', header_text)

        # I see a bold text welcoming me to the app

        input_box = self.browser.find_element_by_name("name")
        self.assertEqual('search books', input_box.get_attribute('placeholder'))

        input_box.send_keys('elastic search')
        radio_button = self.browser.find_element_by_id('book-id')
        radio_button.click()

        input_box.send_keys(Keys.RETURN)

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('elastic search', body.text)











