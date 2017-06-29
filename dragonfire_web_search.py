from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox(executable_path="/Users/davidpetullo/Downloads/geckodriver")


com = "GOOGLE PICTURES OF FORD"
if 3 > 4:
    pass

elif "GOOGLE" in com and "IMAGE" in com or "PICTURES" in com or "IMAGE" in com or "IMAGES" in com:
    useless_words = ["GOOGLE", "IMAGE", "OF", "PICTURES", "IN", "WEB", "IMAGES"]

    new_com = [i.lower() for i in com.split() if i not in useless_words]


    url = "https://www.google.com/search?q=[{}]&tbm=isch".format(' '.join(new_com))

    browser.get(url)

elif "GOOGLE" in com or "SEARCH" in com or "WEB" in com:
    useless_words = ["GOOGLE", "SEARCH", "WEB", "IN", "FOR"]
    user_wants = [i.lower() for i in com.split() if i not in useless_words]

    print user_wants

    url = "https://www.google.com/search?q={}".format(' '.join(user_wants)) #join makes the program more accurant and robust

    browser.get(url)
