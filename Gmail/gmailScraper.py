from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class GmailNameScraper:
    def __init__(self):
        baseUrl = 'https://gmail.com'
        chrome_options = Options()

        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get(baseUrl)
        self.driver.implicitly_wait(3)

    def login(self):
        emailField = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        emailField.send_keys('###############-- ADD EMAIL ADDRESS HERE --###############')

        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()

        passField = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        passField.send_keys('##############-- ADD PASS HERE --################')

        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()

        time.sleep(1)

    def get_email_info(self):
        emailNames = filter(lambda x: x.get_attribute('email') != '#################-- ADD EMAIL ADDRESS HERE --###############',
                            self.driver.find_elements_by_xpath('//span[@email]'))

        emailNames = list(map(lambda x: x.get_attribute('name'), emailNames))[1::2]

        print(emailNames)

    def quit(self):
        self.driver.quit()


chrome = GmailNameScraper()
chrome.login()
chrome.get_email_info()
chrome.quit()
