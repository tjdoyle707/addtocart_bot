from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('/mnt/c/Users/tjdoy/Desktop/repos/addtocart_bot/bin/chromedriver.exe')

driver.get("https://www.nike.com")

print(driver.title)

#sign_in=driver.find_element(by=By.ID, value="hf_title_signin_memberships")
sign_in=driver.find_element(By.XPATH, '//*[@id="gen-nav-commerce-header-v2"]/div[3]/div[1]/div/div/div[4]/div/button ')
#time.sleep(5)
sign_in.click()
#sign_in.send_keys("tjdoyle707@gmail.com")
#sign_in.send_keys(Keys.RETURN)


#//*[@id="hf_title_signin_membership"] 