__author__ = 'asistente'
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("E:\\MISO\\Procesos agiles\\chromedriver.exe")
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

   
