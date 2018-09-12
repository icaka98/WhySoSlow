from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

from jobsbg.parser import parse_job_element


class JobsScraper:
    def __init__(self):
        baseUrl = 'https://www.jobs.bg/'
        chrome_options = Options()

        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get(baseUrl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def click_it_category(self):
        self.driver.find_element_by_xpath('//*[@id="search_frm"]/table/tbody/tr[3]/td/a').click()
        self.driver.find_element_by_xpath('//*[@id="category_15"]').click() # default IT is 15
        self.driver.find_element_by_xpath('//*[@id="categories_tr"]/table/tbody/tr[2]/td/a').click()

    def write_search_town_salary(self, town='София', only_salary=False):
        self.driver.find_element_by_xpath('//*[@id="location"]').send_keys(town)
        time.sleep(1)

        if only_salary:
            self.driver.find_element_by_xpath('//*[@id="enable_salary"]').click()

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def search(self):
        self.driver.find_element_by_xpath('//*[@id="search_frm"]/table/tbody/tr[12]/td/a').click()

        if self.check_exists_by_xpath('//*[@id="closeSalaryAlertBtn"]'):
            self.driver.find_element_by_xpath('//*[@id="closeSalaryAlertBtn"]').click()

    def explore_pages(self):
        page_idx = 1
        all_jobs = []

        while True:
            jobs_elements = self.driver.find_elements_by_xpath(
                '//*[@id="search_results_div"]/table/tbody/tr/td/table/tbody/tr['
                '4]/td/table/tbody/tr/td[1]/table/tbody/tr/td[1][not(@colspan)]')

            jobs = []
            for job in jobs_elements:
                jobs.append(parse_job_element(job))

            all_jobs.extend(jobs)

            page_idx += 1

            if not self.check_exists_by_xpath('(//a[text() = \'>>\'])[1]'):
                break
            else:
                self.driver.find_element_by_xpath('(//*[text() = \'>>\'])[1]').click()

        all_jobs = sorted(all_jobs, key=lambda x: -x.salary)

        return all_jobs

    def quit(self):
        self.driver.quit()
