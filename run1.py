"""
2020/12/9
2:39 下午
name:bianer
project:test
"""
from selenium.webdriver import Chrome
driver=Chrome("/Library/Frameworks/Python.framework/Versions/3.7/bin/chromedriver")
driver.get("https://www.baidu.com/")
driver.quit()
