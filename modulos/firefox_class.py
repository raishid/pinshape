from seleniumwire import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class Firefox_driver:
    def __init__(self):
        options = {
            'proxy': {
                'http': 'http://192.168.10.100:8888',
                'https': 'https://192.168.10.100:8888',
                'no_proxy': 'localhost,127.0.0.1'
            }
        }
        driver = webdriver.Firefox(executable_path="driver/geckodriver.exe", seleniumwire_options=options)#, firefox_profile=perfil)
        self.driver = driver

    def Iniciar_registro(self, email, user, web, bio):
        self.driver.get("https://pinshape.com/users/join")
        self.driver.find_element_by_xpath('//a[@id="email-form"]').click()
        self.driver.find_element_by_xpath('//input[@id="user_email"]').send_keys(email)
        self.driver.find_element_by_xpath('//input[@id="user_password"]').send_keys(email)
        self.driver.execute_script('document.querySelector("#new_user").submit()')

        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//h1[text()='Welcome to Pinshape!']")
            )
        )
        self.driver.find_element_by_xpath('//input[@id="username"]').clear()
        self.driver.find_element_by_xpath('//input[@id="username"]').send_keys(user)
        sleep(3)
        self.driver.find_element_by_xpath('//a[@class="button button-submit"]').click()

        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//h2[text()='Tell us about yourself:']")
            )
        )
        sleep(1)
        self.driver.execute_script('document.querySelector("#designer").click()')
        self.driver.find_element_by_xpath('//a[@class="select2-choice"]').click()
        sleep(1)
        opciones = self.driver.find_elements_by_xpath('//ul[@id="select2-results-1"]//li')
        opciones[2].click()
        self.driver.find_elements_by_xpath('//a[@class="select2-choice"]')[1].click()
        sleep(1)
        opciones = self.driver.find_elements_by_xpath('//ul[@id="select2-results-2"]//li')
        opciones[4].click()

        self.driver.find_element_by_xpath('//a[@class="button button-submit"]').click()

        sleep(1)

        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//h1[text()='Designers Are Awesome!']")
            )
        )

        self.driver.find_element_by_xpath('//input[@id="user_webpage"]').send_keys(web)
        sleep(1)
        self.driver.find_element_by_xpath('//input[@id="user_webpage"]').send_keys(Keys.ENTER)

        sleep(3)

        self.driver.get('https://pinshape.com/users/edit')

        self.driver.find_element_by_xpath('//textarea[@id="user_description"]').send_keys(bio)
        self.driver.execute_script('document.querySelector("#user_available_for_hire_false").click()')
        self.driver.execute_script('document.querySelector("#edit_user").submit()')
        link = self.driver.find_element_by_xpath('//a[@class="username"]').get_attribute('href')
        self.driver.quit()
        return link