from selenium import webdriver
from selenium.webdriver.common.keys import Keys
x=input("enter the song ")
driver=webdriver.Chrome("C:\\python\\chromedriver.exe")
driver.get('https://www.youtube.com')
driver.set_page_load_timeout(30)
driver.maximize_window()
driver.implicitly_wait(20)
#driver.get_screenshot_as_file(facebook.png)
search=driver.find_element_by_id('search')
search.send_keys(x)
search.send_keys(Keys.RETURN)
driver.implicitly_wait(50)
search1=driver.find_element_by_xpath('//div[@id="contents"]/ytd-video-renderer[1]')
search1.click()


