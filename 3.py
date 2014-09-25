import re

fileP = open("3.txt","r")
data = fileP.read()
fileP.close()

data = data.replace('\n',"")

searchObj = re.findall( r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', data)

for x in  searchObj:
   print ( x[4],sep="",end="" )
