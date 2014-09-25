import urllib
from urllib.request import urlopen
import urllib.request
import urllib.parse
import re


url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
values = {"nothing":"12345"}

values['nothing'] = str(16044/2)
values['nothing'] = str(82682)

for i in range(141,400):
    data = urllib.parse.urlencode(values)
    full_url = url + '?' + data
    text = str(urllib.request.urlopen(full_url).read())
    print(str(i)+ " :: "+ text+"  ",end="")
    number = re.search(r'next nothing is \d+', text).group()
    number = re.search(r'\d+', number).group()
    print (number)
    values['nothing'] = number
