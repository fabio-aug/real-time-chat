import unittest
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ChatTests(unittest.TestCase):
    def setUp(self):
        self.process = subprocess.Popen(["python", "./../main.py"])
        self.driver = webdriver.Firefox()

    def test_latency(self):
        latency_is_valid = True

        for i in range(0, 10, 1):
            try:
                self.driver.get("http://localhost:3000/")
                has_been_rendered = ec.presence_of_element_located((By.ID, 'ftl-announcement-polite'))
                WebDriverWait(self.driver, 5).until(has_been_rendered)
            except TimeoutException:
                latency_is_valid = False
                break

        self.assertTrue(latency_is_valid)

    def tearDown(self):
        self.process.kill()
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
