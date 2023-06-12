#<span data-placement="top" title=

#  this pulls names of people's from the scsa world challenge squad list even if they say reserved when viewed in practiscore   .
import re
#import pprint
import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
from html.entities import name2codepoint

from copy import deepcopy

import time
import sys
from os import system
print ("jd starting jim1.py")


def Sort_Tuple(tup):
  
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    tup.sort(key = lambda x: x[0])
    return tup
    
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
class MyHTMLParser(HTMLParser):

        
    def __init__(self):
        HTMLParser.__init__(self)
        self.data = {}
        
        
    def handle_starttag(self, tag, attrs):
#        print("Start tag:", tag)
        for i in range(len(attrs)  )  :
#            if (i==2 or i==3 or i==7):
             if ( i==7):
                 #print( i  , attrs[i])
                 #print ( attrs[i] )  # output would be ('title', 'Mary Rollins (Rimfire Pistol Open)')
                        
                              
                 jd =  attrs[i]
                
                 if not jd[1]:  # when it says empty I think it is really a null value coming in html
                    #print ( "AAAAAA"+jd[1]+"BBBBBB")  #if not myString:
                     pass
                 else:
                    #print ( jd[1] )  #Mary Rollins (Rimfire Rifle Open)
                    strs = jd[1]
                    #print ( strs)
                    jrd= [" ".join(x.split()) for x in re.split(r'[()]',strs) if x.strip()]
                    #print ( jrd[0], jrd[1])   #('Bridget Cunningham', 'Carry Optics')
                    a= jrd[0] ; print (a)
                    b= jrd[1] ; print (b)
                    print ( jrd )
                    
                    #self.data[jrd[0]] = [jrd[1]]
                    self.data[a] = b
                    
                    
                    #print (" ")
        return (  self.handle_starttag )
               
            
#print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
#system('say emily  do you want dessert  ' + str(10)  )
print ("Start : %s"  % time.ctime())
url ='https://practiscore.com/world-speed-shooting-championship-2021-presented-by-psa/squadding'
print ( url +'\n')


html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')

"""
<span data-placement="top" disabled="disabled" id="squad_452038_1_117990" name="squad_452038_1_117990" placeholder="reserved" rel="1" style="background-color: #fcf8e3;" title="Zack Jones, JR (PCC Optic)">
<small class="text-muted">Reserved</small></span>
"""


# #print(soup.select_one("span[title*=Kurt]"))
# just a test to see if I could ifnd one;
#jjj =str ( soup.select_one('span[data-placement="top"]')  )

parser = MyHTMLParser()
my_list = []

#for kkk in soup.find_all('span', {'data-placement':'top'}):
for iteration, kkk in  enumerate ( soup.find_all('span', {'data-placement':'top'})  ) :

    #print kkk  # raw html with span tags
    parser.feed( str(kkk) )
    
    
    #print ( iteration )
    # end of loop







#   this prints the table / tuple  out but unsorted;
'''
print ( "\n\n\n\n")
for x in parser.data.items():
  #print(x )
  #print ( x[1], x[0])
  print ( "Shooter: {0:20} Division: {1}".format(x[0],x[1]))
'''


'''
print (" HHHHHHHHHH")

put = deepcopy(parser.data.items() )  #sort table
# printing the sorted list of tuples
Sort_Tuple(put )


#print ( "\n\n\n\n")
for x in put:
  #print(x )
  #print ( x[1], x[0])
  print ( "Shooter: {0:20} Division: {1}".format(x[0],x[1]))

  #  iteration is NOT ACCURATE GIVEN NULL VLUES;
print(bcolors.OKCYAN  + "\n   OVERSTATED NOT ACCURATE  Total Shooters: " +  str(iteration+1) + bcolors.ENDC)

'''

print(bcolors.OKCYAN  + "Finish : %s"  % time.ctime() + bcolors.ENDC)




quit()

"""

<span data-placement="top" disabled="disabled" id="squad_452038_1_117990" name="squad_452038_1_117990" placeholder="reserved" rel="1" style="background-color: #fcf8e3;" title="Zack Jones, JR (PCC Optic)">
<small class="text-muted">Reserved</small>
</span>
"""



"""
print ("aaaaa")
aa=soup.find('div', {'class' :'squadBox'}).text
print (aa )
"""


#print tag.find_parent('div')


"""
table = soup.find('div', attrs={'class': 'content'})

rows = table.findAll('tr')
for tr in rows:
    cols = tr.findAll('td')
    for td in cols:
        text = td.find(text=True) + ';'
        print text,
    print


tables = [
    [
        [td.get_text(strip=True) for td in tr.find_all('td')]
        for tr in table.find_all('tr')
    ]
    for table in soup.find_all('table')
]


#print(soup.title)
print (soup.title.text)

"""
