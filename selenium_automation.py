from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_driver = os.path.join(os.getcwd(), "chromedriver_linux64/chromedriver")


driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("https://monitor.firefox.com/")
driver.maximize_window()
driver.implicitly_wait(10)
search_box = driver.find_element_by_css_selector(".fx-monitor-logotype")


search_box.send_keys('as112@gmail.com')
search_box.submit() 
