"""
2020/12/9
2:39 下午
name:bianer
project:test
"""
from selenium.webdriver import Chrome
driver=Chrome('/usr/local/bin/chromedriver')
driver.get("https://www.baidu.com/")
driver.quit()
