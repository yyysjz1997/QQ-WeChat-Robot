import time


#使用web浏览器自动化框架，实现登录
import selenium.webdriver

#C:\Program Files\Mozilla Firefox

driver = selenium.webdriver.Firefox()
login_url = "http://web.qq.com"
driver.get(login_url)

input("Please press enter to continue.")
friend_list = []
for eve_friend in driver.find_elements_by_class_name("list_item"):
    friend_list.append(eve_friend.find_element_by_xpath('a/@_uin').text)

print(friend_list)
print(driver.get_cookies())

#通过urllib进行信息发送
import urllib.parse
import urllib.request






'''
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from pprint import pprint
username="username"
passwd="password"

class WebQQ:
    def __init__(self):
        self.browser = webdriver.Firefox() # Get local session of firefox
        self.browser.set_window_position(800,0)
        self.browser.get("http://web.qq.com") # Load page
        while True:
            try:
                elem = self.browser.find_element_by_id("alloy_icon_app_50_3") # Find the qq button
                elem.click()
                print ("click qq button")
                break
            except NoSuchElementException:
                print ("element not loaded yet")
            time.sleep(0.1) # Let the page load, will be added to the API
    def login(self):
        self.browser.switch_to_frame("ifram_login")
# Find the loginState option
        elem = self.browser.find_element_by_id("loginState")
        elem.click()
        print("click loginState")
# choose hidden state
        elem = self.browser.find_element_by_id("loginStatePanel")
        elems = elem.find_elements_by_class_name("statePanel_li")
        elems[0].click()
        print ("choose online state")
# login
        elem = self.browser.find_element_by_id("u") # user name
        elem.send_keys(username)
        elem = self.browser.find_element_by_id("p") # passwd
        elem.send_keys(passwd)
        elem = self.browser.find_element_by_id("login_button") # login button
        elem.click()
def main():
    webqq = WebQQ()
    webqq.login()
if __name__ == "__main__":
    main()
'''