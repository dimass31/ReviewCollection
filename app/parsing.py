from selenium import webdriver
import selenium
from time import sleep
import os

#Путь до дравейра
cur_path = os.path.dirname(__file__)
path = os.path.join(cur_path, 'chromedriver.exe')
os.path.normpath(path)

#Функция удаления одинаковых отзывов
def f(l):
   n = []
   for i in l:
      if i not in n:
         n.append(i)
   return n

class Parser():

    #Конструктор
    def __init__(self, url):
        self.url = url #Ссылка на входящий фильм
        self.positiv_spis = []
        self.negativ_spis = []
        self.neutral_spis = []

    def start(self):
        self.driver = webdriver.Chrome(path)
        self.driver.get(self.url)
        sleep(3) #Время для прогрузки элементов

    #Метод сбора позитивных отзывов
    def positiv(self):

        try:
            #Узнаю количество таких отзывов
            count = self.driver.find_element_by_xpath("//li[@class='pos']/b")
            print(count.text)
            count = int(count.text)

            if count > 0:
                #Открываю раздел с положительными отзывами, если они есть
                iter = self.driver.find_element_by_xpath(("//li[@class='pos']/a"))
                print(iter.text)
                iter.click()
            else:
                return self.positiv_spis

        except selenium.common.exceptions.NoSuchElementException:
            self.positiv_spis = []
        except selenium.common.exceptions.WebDriverException:
            self.positiv_spis = []
        else:
            #Цикл сбора всех уникальных отзывов данного типа
            while (len(self.positiv_spis) != count):
                pos_feedbak = self.driver.find_elements_by_xpath(
                    "//div[@class='response good']//div[@class='brand_words']")
                for elem in pos_feedbak:
                    self.positiv_spis.append(elem.text)

                #Удаляю повторные отзыввы
                self.positiv_spis = f(self.positiv_spis)
                print(len(self.positiv_spis))

                if (len(self.positiv_spis) != count):
                    self.clicker()
        return self.positiv_spis

    # Метод сбора негативных отзывов
    def negativ(self):

        try:
            # Узнаю количество таких отзывов
            count = self.driver.find_element_by_xpath("//li[@class='neg']/b")
            count = int(count.text)

            if count > 0:
                # Открываю раздел с негативными отзывами, если они есть
                iter = self.driver.find_element_by_xpath(("//li[@class='neg']/a"))
                print(iter.text)
                iter.click()
            else:
                return self.negativ_spis

        except selenium.common.exceptions.NoSuchElementException:
            self.negativ_spis = []
        except selenium.common.exceptions.WebDriverException:
            self.negativ_spis = []
        else:
            # Цикл сбора всех уникальных отзывов данного типа
            while (len(self.negativ_spis) != count):
                neg_feedbak = self.driver.find_elements_by_xpath("//div[@class='response bad']//div[@class='brand_words']")
                for elem in neg_feedbak:
                    self.negativ_spis.append(elem.text)

                # Удаляю повторные отзыввы
                self.negativ_spis = f(self.negativ_spis)
                print(len(self.negativ_spis))

                if (len(self.negativ_spis) != count):
                    self.clicker()

        return self.negativ_spis

    # Метод сбора нейтральных отзывов
    def neutral(self):

        try:
            # Узнаю количество таких отзывов
            count = self.driver.find_element_by_xpath("//li[@class='neut']/b")
            count = int(count.text)

            if count > 0:
                # Открываю раздел с нейтральными отзывами, если они есть
                iter = self.driver.find_element_by_xpath(("//li[@class='neut']/a"))
                print(iter.text)
                iter.click()
            else:
                return self.neutral_spis

        except selenium.common.exceptions.NoSuchElementException:
            self.neutral_spis = []
        except selenium.common.exceptions.WebDriverException:
            self.neutral_spis = []
        else:
            # Цикл сбора всех уникальных отзывов данного типа
            while (len(self.neutral_spis) != count):
                net_feedbak = self.driver.find_elements_by_xpath("//div[@class='response neutral']//div[@class='brand_words']")
                for elem in net_feedbak:
                    self.neutral_spis.append(elem.text)

                # Удаляю повторные отзыввы
                self.neutral_spis = f(self.neutral_spis)
                print(len(self.neutral_spis))

                if (len(self.neutral_spis) != count):
                    self.clicker()
        return self.neutral_spis

    #Метод получения страницы с новыми отзывами
    def clicker(self):
        button = self.driver.find_element_by_xpath("//p[@class='more_random random_bottom']/a")
        button.click()

    #Закрытие окна
    def close(self):
        self.driver.close()