from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
 
driver.get('https://dbd.tricky.lol/shrine')
 
driver.save_screenshot('screenshot.png')
 
driver.quit()