# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://credence.in/")
# driver.implicitly_wait(10)
# driver.find_element(By.XPATH, "//img[@src='/website/images/enquiry.png']").click()
#
# l = len(driver.find_elements(By.XPATH, "//div[@class='quickfinder-description gem-text-output']/p/a[1]"))
# # l=6
#
# for r in range(1, 1 + l):
#     number = driver.find_element(By.XPATH,
#                                  "//div[@class='quickfinder-description gem-text-output']/p/a[" + str(r) + "]").text
#     print(number)
#
# # +91 9091929355 --> present or not and find its position #5
# # loop 1
# # //div[@class='quickfinder-description gem-text-output']/p/a[1] # r =1
# # loop 2
# # //div[@class='quickfinder-description gem-text-output']/p/a[2]# r =2
# # loop 3
# # //div[@class='quickfinder-description gem-text-output']/p/a[3]# r =3
