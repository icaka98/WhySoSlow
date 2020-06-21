from selenium.webdriver import Chrome
import pandas as pd
import time as time

webdriver = "webdriver/chromedriver.exe"

driver = Chrome(webdriver)

url = "https://blog.deeplearning.ai/blog"
next_posts_btn_selector = 'next-posts-link'

driver.get(url)

load_more_btn = driver.find_element_by_class_name(next_posts_btn_selector)

while load_more_btn.is_displayed():
    load_more_btn.click()
    time.sleep(2)

posts = driver.find_elements_by_xpath('//h2[@class = "post-header"]/a[1]')
links = [post.get_attribute('href') for post in posts]

print('Number of posts: ', len(posts))

df = pd.DataFrame(links, columns=['link'])
df.to_csv('links.csv')

print('Successfully saved links to links.csv .')

driver.close()
