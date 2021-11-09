from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# Config Change depending on your needs
options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
browser = webdriver.Firefox(options=options, executable_path="C:\programming\code_tests\Python\gecko\geckodriver.exe")

# Get the data
url = 'https://play.google.com/store/apps/details?id=com.google.android.googlequicksearchbox&hl=en'
browser.get(url)
res = browser.find_elements(By.XPATH, '//div[@class="d15Mdf bAhLNe"]')
print(res)

