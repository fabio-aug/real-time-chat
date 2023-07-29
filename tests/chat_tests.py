import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class ChatTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_seila(self):
        self.driver.get("http://localhost:3000/")
        

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
