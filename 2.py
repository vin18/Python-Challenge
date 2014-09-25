
fileP = open("2.txt","r")
data = fileP.read()
fileP.close()

fileP = open("2_commom.txt","r")
chars = fileP.read()
cList = chars.splitlines()
fileP.close()

for c in cList:
    data = data.replace(c,"")

data  = data.replace('\n',"")
print (data)
