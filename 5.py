import pickle

fileP = open("5.txt","rb")
vals = pickle.load(fileP)
fileP.close()
for value in vals:
    for val in value:
        for x in range(int(val[1])):
            print(str(val[0]),end="")
    print("")
