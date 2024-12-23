from selenium import webdriver

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://www.google.com")
print(driver.title)
driver.quit()
