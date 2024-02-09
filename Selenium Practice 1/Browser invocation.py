# 1
## For chrome 114  version

# from selenium import webdriver
# import time
# driver = webdriver.Chrome(executable_path="C:\\Users\\yusuf\\Downloads\\chromedriver_win32")
# driver.get("https://www.facebook.com/")
# time.sleep(5)

## For Chrome 120 version

## chromedriver invocation from downloads
# from selenium import webdriver
# import time
# driver = webdriver.Chrome(executable_path="C:\\Users\\Akshay\\Downloads\\chromedriver-win64\\chromedriver-win64")
# driver.get("https://www.facebook.com/")
# time.sleep(5)

# chromedriver invocation from pycharm
#
# from selenium import webdriver
# import time
# # driver = webdriver.Chrome(executable_path="C:\\Users\\yusuf\\Downloads\\chromedriver-win64\\chromedriver-win64")
#
# driver = webdriver.Chrome(executable_path="D:\\CT16 17 PYTHON AUTOMATION\\Selenium Practice 1\\chromedriver.exe")
# driver.get("https://www.facebook.com/")
# time.sleep(5)

# 2
#
# from selenium import webdriver
# #
# import time
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# browser = webdriver.Chrome(options=options)
#
# browser.get("https://www.facebook.com/")
# browser.maximize_window()

# 3
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# import time
#
# browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
# url = 'http://automation.credence.in'
# browser.get(url)
# time.sleep(5)



# 4

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options
# import time
# firefox_options = Options()
# browser = webdriver.Firefox(options=firefox_options)
#
# url = 'http://automation.credence.in'
# browser.get(url)
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
# from selenium import webdriver
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
#
# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
#
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#
#
#
# url = 'http://automation.credence.in'
# driver.get(url)


