
# Jim Doran    Jan / 2023 to scrape pickleball signup genius registration openings

import time 
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#print ("Start : %s" % time.ctime())

import sys
from os import system
print(" ");print(" ")

  
#url of the page we want to scrape
url = "https://www.signupgenius.com/go/70a0e4fa5aa2cabfc1-everglades60#"

#  47 url is one that is NOT FULL; 
#url ="https://www.signupgenius.com/go/70a0e4fa5aa2cabfc1-everglades60#"
print(url)


# initiating the webdriver. Parameter includes the path of the webdriver.

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)



#driver = webdriver.Chrome('./chromedriver') 
driver.get(url) 
  
# this is just to ensure that the page is loaded
time.sleep(5) 
  
html = driver.page_source

  
# this renders the JS code and stores all
# of the information in static HTML code.  
# Now, we could simply apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")



title = soup.find("meta", property="og:title")
url = soup.find("meta", property="og:url")

print(title["content"] if title else "No meta title given")
#print(url["content"] if url else "No meta url given")



# old way --> sometimes fails;    title = soup.select('h1.signup--title-text')[0].text.strip()


print ("Start : %s" % time.ctime() +" ---"+ title["content"] )



all_divs = soup.find('div', {'class' : 'alert alert-danger feedback-error fade-in-up black-shadow-active'})

s =        soup.find('div', {'class' : 'alert alert-danger feedback-error fade-in-up black-shadow-active'})

if s is not None:
    job_profiles = all_divs.find_all('span')

    for job_profile in job_profiles :
        if (job_profile.text == 'This sign up is full and has no more available slots. Please contact the sign up creator for more info.'):
            print('Signup is Full')
    driver.close() # closing the webdriver
else:
    print("Signup is NOT FULL")
    for x in range(22):
        print('\a')


exit()
