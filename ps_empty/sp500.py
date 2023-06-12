import requests
from bs4 import BeautifulSoup

import time
import sys
from os import system

print "Start : %s" % time.ctime()

url = 'https://finance.yahoo.com/quote/SPY'
print ( url )


for x in range(1, 100):
    print("We're on loop %d" % (x))

    try:
        #res = requests.get(url)
        res = requests.get(url, timeout=5)
        res.raise_for_status()
    except requests.exceptions.RequestException as e:
        print e
        print(  "On Loop %d" % (x) +"  Connection failed")
        time.sleep(30)
        continue
    
    
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    #text = soup.get_text()

    #text = soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'  } )
    #print ( text )
    
    price = soup.find('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'  } ).find('span').text
     
    print ( "The current price is:  " + price )
    system (' say current price is' + price )
    
    iprice = float ( price )
    if iprice   > 233.0:
        print ("greater" )
    else:
        print ( "lesser" )
    
    
    # every 100 times pause for 30 seconds to prevent DDOS;
    if (x % 100==0):
        print('100 interval pause')
        time.sleep(60)
    
    
    # sleep loop iteration
    time.sleep( 2 )

print "End : %s" % time.ctime()


# sample junk snipets below
'''
    # import module sys to get the type of exception
    import sys

    randomList = ['a', 0, 2]

    for entry in randomList:
        try:
            print("The entry is", entry)
            r = 1/int(entry)
            break
        except:
            print("Oops!",sys.exc_info()[0],"occured.")
            print("Next entry.")
            print()
    print("The reciprocal of",entry,"is",r)
'''

'''
       if b > a:
         print("b is greater than a")
       else:
         print("b is not greater than a")

   count = 0
   while (count < 9):
      print 'The count is:', count
      count = count + 1

   print "Good bye!"
   '''
