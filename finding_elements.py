import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20) #read more about this





driver.get("http://google.com")
print("opened the browser and google website")
time.sleep(3)

buttons = driver.find_element_by_xpath('//button')
#button.text this is incorrect
for button in buttons:
    print("text of button: ', button.text")


search_text_box = driver.find_element_by_name("q")
print("identified google search")

search_text_box.clear()
search_text_box.send_keys("python selenium")

print("now closing the browser...")
driver.close()
print()