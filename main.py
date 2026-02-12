import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import feedparser

to_send = ""
tc_url = "https://techcrunch.com/feed/"
feed = feedparser.parse(tc_url)

for entry in feed.entries[:1]:
    date = entry.published.split() #type:ignore
    cleaned_date = " ".join(date[:4]) #type:ignore 

    to_send = f"Title: {entry.title}""\n""\n"f"summary: {entry.summary}""\n""\n"f"Link: {entry.link}""\n""\n"f"Published: {cleaned_date}." 
    


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True, )
driver = webdriver.Chrome(chrome_options)

driver.get("https://x.com")

with open("twitter_cookies.json", "r") as f: 
    cookies = json.load(f)

# Injecting
for cookie in cookies:
    if 'sameSite' in cookie:
        if cookie['sameSite'] not in ["Strict", "Lax", "None"]:
            cookie['sameSite'] = "Lax"
    try:
        driver.add_cookie(cookie)
    except Exception as e:
        print(f"Skipping a cookie: {e}")

driver.refresh()
print("Home Page.")
time.sleep(10) 

driver.implicitly_wait(5)

x_to_post = driver.find_element(By.CLASS_NAME, value="public-DraftStyleDefault-ltr")
x_to_post.send_keys(to_send)
driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/div/span/span').click()

print("posted")