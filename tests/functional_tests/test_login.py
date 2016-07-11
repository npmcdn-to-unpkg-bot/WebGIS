import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.core import mail

from .base import BaseLiveTest

TEST_EMAIL = 'testperson@example.com'
SUBJECT = 'Your login link for the Tropical Marina Data Portal'


class LoginTest(BaseLiveTest):

    def test_can_get_email_link_to_log_in(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_name('email').send_keys(
            TEST_EMAIL + '\n'
        )

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Check your email', body.text)

