
# Jim Doran   5/23 screen scrapes pickleball registrations for oxford pickleball signups
import time
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
from os import system
start_time = time.time()
print ("Start : %s" % time.ctime() )
#import os


#url of the page we want to scrape
url ="https://app.courtreserve.com/Online/Events/Details/2490/7O4N7CB2490147"
url ="https://app.courtreserve.com/Online/Events/Details/2490/SG8IOUW2490366"
url = "https://app.courtreserve.com/Online/Events/Details/2490/RFDYZRO2490814"

print(url)



# todo add ability to pass phone number as parameter to the procedure; maybe as a list; 

cmd =  """osascript<<END

tell application "Messages"

send "Oxford Registration has opening" to buddy "18606719963" of (service 1 whose service type is iMessage)

end tell

END"""
new_string = cmd.replace("opening", "opening " + url  )

def send_Message():
    os.system(new_string)
  
def NotFull():
    print("session is NOT FULL")
    send_Message()
    for x in range(11):
     print('\a')



# initiating the webdriver. Parameter includes the path of the webdriver.
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)
#driver = webdriver.Chrome('./chromedriver') 
driver.get(url) 
  
# this is just to ensure that the page is loaded
time.sleep(1)
  
html = driver.page_source

# this renders the JS code and stores all
# of the information in static HTML code.  
soup = BeautifulSoup(html,"html.parser")

spans = soup.find_all('span', {'class' : 'title-part'})

# create a list of lines corresponding to element texts
lines = [span.get_text() for span in spans]

i=0
for line in lines:
   print (i, line.strip())
   i+=1

print ( "date",lines[0].strip())
print ( "time",lines[1].strip())
print ( "price",lines[2].strip())
print ( "registration status",lines[3].strip())
print(" ")

status = lines[3].strip().upper() 
#print (status)

if (status.find('FULL') != -1):
    print("Contains substring 'FULL,'")
else:
    NotFull()



exit()

# below is to get list of wait list and registered people; 

headers = [th.get_text(strip=True) for th in soup.select('table-responsive job_review_table mt0')]
rows = []
for row in soup.select('table'):
    data = [d.get_text(strip=True) for d in row.select('th, td')]
    rows.append(data)

print ("1111111")
print ( rows[1])
print ("1111111")
print ("2222")
print ( rows[0])
print ("2222")


dicts = {}
count=1
for i in range(len(rows)):
    for j in range(len(rows[i])):
        if  rows[i][j].strip() and  rows[i][j].strip() != "Name" and  rows[i][j].strip()!="Court":
            dicts[count] =  rows[i][j]
            count = count+1
#print(dicts)

print (" jjjjjjjjj");print (" ");print ("")
for x in dicts:
    print (dicts[x])
    print (x)
    


print("--- %s seconds ---" % (time.time() - start_time))
print ("Finish : %s" % time.ctime())
exit()
