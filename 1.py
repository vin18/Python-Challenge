import sys
strMain =  "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
strMain = strMain.lower()
from string import maketrans

strL = strMain.split(" ")

# for x in strL:
# 	xList = list(x)
# 	for ch in xList:
# 		if ord(ch) >= 97 and ord(ch) <=122:
# 			ch = str(unichr((ord(ch)-97+2)%26+97))
# 		sys.stdout.write(ch)
# 	sys.stdout.write(" ")

print

intab = []
outtab = []
for x in range(26):
	intab.append(str(unichr(x+97)))
	outtab.append(str(unichr((x+2)%26+97)))

trantab = maketrans("".join(intab), "".join(outtab))
print "map".translate(trantab);

# print str("".join(intab))
# print str("".join(outtab))



