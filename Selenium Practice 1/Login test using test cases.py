## LOGIN TEST SCRIPT USING CHROME BROWSER
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# import time
# browser = webdriver.Chrome()
#
# url = 'https://www.facebook.com/'
# browser.get(url)
#
# browser.find_element(By.NAME, "email").send_keys("yusitamboli")
# browser.find_element(By.NAME, "pass").send_keys("yusuf123@")
# time.sleep(5)
# browser.find_element(By.NAME,"login").click()
# #
# browser.maximize_window()
# time.sleep(5)
# browser.close()




## LOGIN TEST SCRIPT USING FIREFOX BROWSER

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options
# import time
# firefox_options = Options()
#
# browser = webdriver.Firefox(options=firefox_options)
#
#
# url = 'http://automation.credence.in'
# browser.get(url)
# browser.find_element(By.LINK_TEXT, "Login").click()
# browser.find_element(By.NAME, "email").send_keys("test@credence.in")
# time.sleep(2)
# browser.find_element(By.NAME, "password").send_keys("test@123")
# time.sleep(2)
# browser.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
#
# browser.maximize_window()
# print("Login Test Successfully Passed")
# browser.close()
