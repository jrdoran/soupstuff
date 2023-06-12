
# Jim Doran    Jan / 2023 to scrape pickleball signup genius registration openings

import time
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#print ("Start : %s" % time.ctime())

import sys
from os import system
print(" ");print(" ")

  
#url of the page we want to scrape
url = "https://app.courtreserve.com/Online/Events/Details/2490/6F1X9XP249062"
print(url)



  
  
# function to extract html document from given url
def getHTMLdocument(url):
      
    # request for HTML document of given url
    response = requests.get(url)
      
    # response will be provided in JSON format
    return response.text
  
    
url_to_scrape = url
  
# create document
html_document = getHTMLdocument(url_to_scrape)
  
soup = BeautifulSoup(html_document, 'html.parser')

print ("aaaa")
print (soup(text=re.compile('WAITLISTED')))

print ("bbbbbbb")
print (soup(text=re.compile('FULL - ')))


spans = soup.find_all('span', {'class' : 'title-part'})

# create a list of lines corresponding to element texts
lines = [span.get_text() for span in spans]

# collect the dates from the list of lines using regex matching groups
i=0
for line in lines:
   print ( i )
   i=i+1
   print ( line)
        
        
print ("****************")
        
spans = soup.find_all('div', {'class' : 'table-responsive job_review_table mt0'})

# create a list of lines corresponding to element texts
lines = [span.get_text() for span in spans]

# collect the dates from the list of lines using regex matching groups
i=0
for line in lines:
   print ( i )
   i=i+1
   print ( line)
     
     
     
     
        


""" <span class="title-part text-uppercase">
                                    Full

                                                 - <b>7 REGISTRANT(S) WAITLISTED</b>
                                </span>
                                
"""
exit()





print ("Start : %s" % time.ctime() +" ---"+ title["content"] )




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
