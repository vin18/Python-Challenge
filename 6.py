


import zipfile
import re


fh = open('channel.zip', 'rb')
z = zipfile.ZipFile(fh)
for name in z.namelist():
    outpath = "tmp/"
    z.extract(name, outpath)
fh.close()


nothings = []
nextFile = "90052"
sumN = int(nextFile)
while nextFile:
    nothings.append(nextFile)
    fd = open("tmp/" + nextFile + ".txt")
    #zip.getinfo("tmp/" + nextFile + ".txt")
    data = fd.read()
    print(data)
    try:
        nextFile = re.search(r'nothing is \d+', data).group()
    except:
        print(str(sumN))
        break
    #print (nextFile,end="")
    nextFile = re.search(r'\d+', nextFile ).group()
    sumN += int(nextFile)
    #print ("  ", nextFile)


comment = ""
fh = open('channel.zip', 'rb')
z = zipfile.ZipFile(fh)
for n in nothings:        
    comment += (z.getinfo(n+".txt").comment).decode("utf-8")
fh.close()
print (comment)



##import os
##from os import walk
##
##f = []
##for (dirpath, dirnames, filenames) in walk("tmp/"):
##    f.extend(filenames)
##    break
##for x in f:
##    #print (x)
##    st = os.stat("tmp/"+x)
##    print (st)
