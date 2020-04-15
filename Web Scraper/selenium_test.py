from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary, executable_path=r'C:\\Webdrivers\\geckodriver.exe')
driver.get('https://www.duckduckgo.com')