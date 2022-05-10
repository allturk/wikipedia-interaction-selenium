from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = r"C:\Development\chromedriver.exe"
s = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

statistic = driver.find_element(By.CSS_SELECTOR, '[title="Special:Statistics"]')
print(f"{statistic.text} articles in English")
driver.get("https://tr.wikipedia.org/wiki/Anasayfa")
t_statistic = driver.find_element(By.CSS_SELECTOR, '[title="Özel:İstatistikler"]')
print(f"{t_statistic.text} articles in Turkish")

driver.quit()
