import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class SelenideSearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_google(self):
        driver = self.driver

        # 1. Открыть страницу http://google.com/ncr
        driver.get('http://google.com/ncr')

        # 2. Выполнить поиск слова “selenide”
        search = driver.find_element(By.NAME, 'q')
        search.send_keys('selenide' + Keys.RETURN)

        # 3. Проверить, что первый результат – ссылка на сайт selenide.org
        assert 'selenide.org' in driver.find_element(By.TAG_NAME, 'cite').text

        # 4. Перейти в раздел поиска изображений
        driver.find_element(By.XPATH, '//div[@role="navigation"]//*[text()="Картинки" or text()="Images"]').click()

        # 5. Проверить, что первое изображение неким образом связано с сайтом selenide.org
        assert 'Selenide' in driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/h3').text

        # 6. Вернуться в раздел поиска Все
        driver.find_element(By.XPATH, '//span[@aria-current="page"]/..//*[text()="Все" or text()="All"]').click()

        # 7. Проверить, что первый результат такой же, как и на шаге 3.
        assert 'selenide.org' in driver.find_element(By.TAG_NAME, 'cite').text

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
