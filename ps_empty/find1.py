import requests
from bs4 import BeautifulSoup

# url = 'https://practiscore.com/world-speed-shooting-championship-2020/squadding'
url = 'https://practiscore.com/steel-challenge-practice-match-march-3/squadding'
res = requests.get(url)
html_page = res.content

import time

print "Start : %s" % time.ctime()

import sys
from os import system

#system('say Counting the times Empty appears on  squad list ')

for x in range(0, 9999):
    print("We're on loop %d" % (x))

    
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')

    text = soup.get_text()
    jcount = text.count('Empty')
    
    fcount = jcount
   # if fcount <>4:
    #     system ( 'say ding ding ding yo yo yo hey hey hey jim jim jim  ' + str ( fcount))
        


    #  system ( 'say Empty equals ' + str ( jcount))
    print(  "\n Number of times Empty on squad page: " + str( text.count('Empty') ) )

    time.sleep( 1 )
    
print "End : %s" % time.ctime()


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
   

