import requests
from bs4 import BeautifulSoup

import time
import sys
from os import system


print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

numempty = int(sys.argv[1])



print "Start : %s" % time.ctime()
system('say Counting  Empty ')

# url =  'https://practiscore.com/world-speed-shooting-championship-2020/squadding'

url ='https://practiscore.com/world-speed-shooting-championship-2021-presented-by-psa/squadding'

print ( url )


for x in range(1, 9999):
#    print("We're on loop %d" % (x))


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
    text = soup.get_text()

    jcount = text.count('Empty')


    print ("  Lori   " + str(  text.count( 'Lori ' )))


    fcount = jcount
    if fcount <> numempty:
        system ( 'say ding ding ding yo yo yo  ' + str ( fcount))

        #  system ( 'say Empty equals ' + str ( jcount))
    print(  "On Loop %d " % (x) +"Num Empty on squad page: " + str( text.count('Empty') ) )
    print ("...")
    
    # every 100 times pause for 30 seconds to prevent DDOS;
    if (x % 100==0):
        print('100 interval pause')
        time.sleep(60)
    
    
    time.sleep( 5 )

print "End : %s" % time.ctime()



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
