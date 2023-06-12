
print ( " starting ")
html =' <span data-placement="top" disabled="disabled" id="squad_452038_1_117990" name="squad_452038_1_117990" placeholder="reserved" rel="1" style="background-color: #fcf8e3;" title="Zack Jones, JR (PCC Optic)"> <small class="text-muted">   Reserved    </small>  </span>  '




from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
#        print("Start tag:", tag)
        for i in range(len(attrs))  :
                if (i==2 or i==3 or i==7):
                    print( i  , attrs[i])
                


"""
    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)
  
    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)
"""
parser = MyHTMLParser()


parser.feed( html )











"""

#print ( dict1 )
#print ( dict1['author'] )

"""

quit()
