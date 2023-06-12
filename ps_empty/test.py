
import re
strs = "Mary Rollins (Rimfire Rifle Open)"
j= [" ".join(x.split()) for x in re.split(r'[()]',strs) if x.strip()]
#>>>['Hello', 'Test1, test2', 'Hello1, hello2', 'other_stuff']
print ("qqqqqq"+j[0]+"aaaa"+j[1]+"bbbb")
