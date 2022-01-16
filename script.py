from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

PATH = "C:/Users/Dell/PycharmProjects/testing/chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://amazing-observers-frontend.herokuapp.com/")
driver.find_element(By.ID, "name").send_keys("host")
driver.find_element(By.CLASS_NAME, "inputs-btn").click()
code = driver.find_element(By.CLASS_NAME, "highlight-inputs").text

i = 1
while i < 5:
    driver.switch_to.new_window()
    driver.get("http://amazing-observers-frontend.herokuapp.com/join")
    driver.find_element(By.ID, "name").send_keys("Player" + str(i))
    driver.find_element(By.ID, "room-code").send_keys(code)
    driver.find_element(By.CLASS_NAME, "inputs-btn").click()
    i = i + 1

driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.CLASS_NAME, "inputs-btn").click()
driver.find_element(By.CLASS_NAME, "inputs-btn").click()

h = 1
while h < 5:
    driver.switch_to.window(driver.window_handles[h])

    j = 1
    while j < 6:
        checkboxes = driver.find_elements(By.CLASS_NAME, "list-group-item")
        random.shuffle(checkboxes)
        for each_checkbox in checkboxes:
            if not each_checkbox.is_selected():  # just to be sure that you make check, but not uncheck
                driver.execute_script('arguments[0].click()', each_checkbox)
        j = j + 1

    element = driver.find_element(By.CLASS_NAME, "inputs-btn")
    driver.execute_script("arguments[0].click();", element)
    h = h + 1

print(code)
print("test completed successfully")
